"""Server module for Emotion Detection Flask application."""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """Route to analyze emotions from query parameter 'textToAnalyze'."""
    text = request.args.get('textToAnalyze')

    result = emotion_detector(text)

    # Format output exactly with all fields
    response = {
        "anger": result.get("anger"),
        "disgust": result.get("disgust"),
        "fear": result.get("fear"),
        "joy": result.get("joy"),
        "sadness": result.get("sadness"),
        "dominant_emotion": result.get("dominant_emotion"),
        "status_code": result.get("status_code")
    }

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
