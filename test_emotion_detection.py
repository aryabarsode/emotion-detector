import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am happy")
        self.assertEqual(result['dominant_emotion'], 'joy')
        self.assertEqual(result['status_code'], 200)

    def test_sadness(self):
        result = emotion_detector("I am sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')
        self.assertEqual(result['status_code'], 200)

    def test_blank_input(self):
        result = emotion_detector("")
        self.assertEqual(result['dominant_emotion'], None)
        self.assertEqual(result['status_code'], 400)

if __name__ == "__main__":
    unittest.main()
