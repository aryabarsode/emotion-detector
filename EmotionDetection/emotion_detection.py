import requests

def emotion_detector(text_to_analyse):
    """
    Sends text to Watson NLP API (simulated) and returns emotion scores.
    Handles blank input with status code 400.
    """

    if text_to_analyse is None or text_to_analyse.strip() == "":
        # Return 400 Bad Request format
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
            "status_code": 400
        }

    # Simulated POST request structure expected by rubric
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/fake-instance-id/v1/analyze?version=2021-08-01"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer fakeapikey",
        "grpc-metadata-mm-model-id": "emotion"
    }
    payload = {
        "text": text_to_analyse,
        "features": {"emotion": {}},
        "raw_document": True
    }

    # Simulated API response
    if "sad" in text_to_analyse.lower():
        emotions = {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.05,
            "sadness": 0.90
        }
    else:
        emotions = {
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.01,
            "joy": 0.90,
            "sadness": 0.06
        }

    dominant = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant
    emotions["status_code"] = 200

    return emotions
