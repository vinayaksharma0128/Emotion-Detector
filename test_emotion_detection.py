import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am very happy")
        self.assertIn("joy", result)

    def test_anger(self):
        result = emotion_detector("I am very angry")
        self.assertIn("anger", result)

    def test_sadness(self):
        result = emotion_detector("I am very sad")
        self.assertIn("sadness", result)

if __name__ == "__main__":
    unittest.main()
