''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request


# Import the emotion_detector function from the package created: 
from EmotionDetection.emotion_detection import emotion_detector


#Initiate the flask app : 
app = Flask(“Emotion Detector”)


@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using the emotion_detector()
        function. The output returned shows the emotion and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again."
    return f'''For the given statement, the system response is 'anger': {anger},
    'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}.
    The dominant emotion is {dominant_emotion}.'''


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(debug=True, host="0.0.0.0", port=5000)
