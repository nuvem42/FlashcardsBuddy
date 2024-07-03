import unittest
import sys
import os

# Adjust the path to import the models module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../flashcards_app')))

from models import Flashcard
from ai import AIModel

class TestAIModel(unittest.TestCase):

    def setUp(self):
        flashcards = [
            Flashcard(1, 'Q1', 'A1', 'Topic1', 'easy'),
            Flashcard(2, 'Q2', 'A2', 'Topic2', 'medium'),
            Flashcard(3, 'Q3', 'A3', 'Topic3', 'hard')
        ]
        self.ai_model = AIModel(flashcards)

    def test_get_recommendation(self):
        recommendations = [self.ai_model.get_recommendation().id for _ in range(1000)]
        self.assertTrue(1 in recommendations)
        self.assertTrue(2 in recommendations)
        self.assertTrue(3 in recommendations)

    def test_update_difficulty(self):
        flashcard = self.ai_model.flashcards[0]
        self.ai_model.update_difficulty(flashcard, 'hard')
        self.assertEqual(flashcard.difficulty, 'hard')

if __name__ == '__main__':
    unittest.main()
