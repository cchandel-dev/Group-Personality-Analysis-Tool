# MBTI-Analysis

The Internet is a vibrant landscape which hosts many subcultures, ideologies and schools of thought. I became interested in learning about whether or not these communities have "Group Personalities" because individuals self-select for communities based on personality type. One commonly used metric for measuring personality is the MBTI personality scale. Using four different NLP models - one for each of the four axis's of the MBTI scale - we can now use this free tool to analyze the top 100 comments for any input YouTube video with visible comments. The top 100 comments are grabbed using the Youtube API (owned by Google) and they are all classified by all four of these models and this data is aggregated to deliver a general breakdown of the "group personality" associated with a video. This is a tool that can be used to generate one point of data in measuring the "group personality" of any Internet Subculture with a presence on YouTube, more work is needed to generate a more detailed and data rich view of Internet Community.

In the example I show below I am grabbing the top 100 comments from Harvard's famous CS50 – Full Computer Science University Course. 
The results that were obtained are shown in the gif below and reveal a group personality that leans towards INTP. 

![](https://github.com/cchandel-dev/Group-Personality-Analysis-Tool/blob/main/read%20me%20assets/demo.gif)

Interestingly I asked OpenAI a follow-up question and got the following result, note that it actually points to Computer Programmers!

![](https://github.com/cchandel-dev/Group-Personality-Analysis-Tool/blob/main/read%20me%20assets/OpenAI-response.png)


To run this program follow these steps.

    1. clone this repo locally and enter the directory
    2. open up your terminal in this directory
    3. create a python virtual environment and install all of the modules listed in requirements.txt
    3. run the following commands one at a time in your terminal to set up the flask server
          set FLASK_APP = app.py
          set FLASK_ENV = development
          flask run
    4. go to your choice of web browser and enter http://127.0.0.1:5000/


In developing this program - four NLP ML models were used. The development workflow is described visually below - but is not included in the code within this repository.

![](https://github.com/cchandel-dev/Group-Personality-Analysis-Tool/blob/main/read%20me%20assets/training-workflow.png) 
