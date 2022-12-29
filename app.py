from flask import Flask, render_template, request
from sklearn.svm import SVC
import re
import os
import json
import googleapiclient.discovery

app = Flask(__name__)
# home route
@app.route("/")
def hello():
    return render_template('index.html', name = 'Jane', gender = 'Female')

# serving form web page
@app.route("/my-form")
def form():
    return render_template('form.html')

# handling form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    # since we sent the data using POST, we'll use request.form
    print('URL: ', request.form['url'])
    comments = find_comments(extract_video_id(request.form['url']))
    results = run_NLP(comments)
    analysis = analyze(results)
    processed_text = final_output(analysis)
    return render_template('index.html', processed_text=processed_text)
def extract_video_id(url):
    match = re.search(r"youtube\.com/.*v=([^&]*)", url)
    if match:
        result = match.group(1)
    else:
        result = ""
    print(result)
    return str(result)
    
def find_comments(video_id):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyDG-4Z-b1Nc2MY5n4VOekotqalDGJDXUZo"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=100,
        moderationStatus="published",
        order="relevance",
        textFormat="plainText",
        videoId= video_id,
        prettyPrint=True
    )
    response = request.execute()
    comments = []
    for comment in response["items"]:
        comments.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])
    return comments
def run_NLP(comments):
    # take in list of posts (iterable)
    # generate all vectors not including LIWC inline
    # run and return success to ensure it is possible
    # then take a crack at InLine LIWC, if it is possible add that feature, else retrain a model without LIWC 

    import pandas as pd
    from nrclex import NRCLex
    new_cols = ['fear', 'anger', 'anticip', 'trust', 'surprise', 'positive', 'negative', 'sadness', 'disgust', 'joy']
    emolex_vector = pd.DataFrame(columns=new_cols)
    for comment in comments:
      temp = NRCLex(str(comment)).affect_frequencies
      emolex_vector.loc[len(emolex_vector.index)] = [temp['fear'], temp['anger'], temp['anticip'], temp['trust'], temp['surprise'], temp['positive'], temp['negative'], temp['sadness'], temp['disgust'], temp['joy']]
    return emolex_vector

def analyze(emolex_vector):
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline

    pipeline = Pipeline([
        ('std_scalar', StandardScaler())
    ])

    emolex_vector = pipeline.fit_transform(emolex_vector)
    import pickle
    dimensions = ['E-I', 'N-S', 'T-F', 'J-P']
    states = {'E':0, 'I':0, 'N':0, 'S':0, 'T':0, 'F':0, 'J':0, 'P':0,}
    for dimension in dimensions:
      path = 'models/{}_SVC_model.pickle'.format(dimension)
      pickle_in = open(path,'rb')
      classifier = pickle.load(pickle_in)
      predictions = classifier.predict(emolex_vector)
      for prediction in predictions:
        if dimension == 'E-I' and prediction == 1:
          states['E'] = states['E'] + 1
        if dimension == 'E-I' and prediction == 0:
          states['I'] = states['I'] + 1
        if dimension == 'N-S' and prediction == 1:
          states['N'] = states['N'] + 1
        if dimension == 'N-S' and prediction == 0:
          states['S'] = states['S'] + 1
        if dimension == 'T-F' and prediction == 1:
          states['T'] = states['T'] + 1
        if dimension == 'T-F' and prediction == 0:
          states['F'] = states['F'] + 1
        if dimension == 'J-P' and prediction == 1:
          states['J'] = states['J'] + 1
        if dimension == 'J-P' and prediction == 0:
          states['P'] = states['P'] + 1
    return(states)
def final_output(states):
    return states
app.run(debug = True) 
