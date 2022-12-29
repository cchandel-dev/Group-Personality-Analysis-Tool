import os
import json
import googleapiclient.discovery

def main():
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
        videoId="JXRN_LkCa_o",
        prettyPrint=True
    )
    response = request.execute()
   # data = json.loads(response)
    comments = []
    for comment in response["items"]:
        comments.append(comment['snippet']['topLevelComment']['snippet']['textOriginal'])
    for comment in comments:
        print(comment)
if __name__ == "__main__":
    main()
