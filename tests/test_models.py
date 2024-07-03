import unittest
import sys
import os

# Adjust the path to import the models module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../flashcards_app')))

from models import FlashcardManager

class TestFlashcardManager(unittest.TestCase):

    def setUp(self):
        self.manager = FlashcardManager(data_file='test_flashcards.json')
        self.manager.flashcards = []

    def tearDown(self):
        self.manager.flashcards = []
        self.manager.save_flashcards()

    def test_add_flashcard(self):
        self.manager.add_flashcard('Question 1', 'Answer 1', 'Topic 1', 'easy')
        self.assertEqual(len(self.manager.flashcards), 1)
        self.assertEqual(self.manager.flashcards[0].question, 'Question 1')

    def test_edit_flashcard(self):
        self.manager.add_flashcard('Question 1', 'Answer 1', 'Topic 1', 'easy')
        self.manager.edit_flashcard(1, 'New Question', 'New Answer', 'New Topic', 'medium')
        self.assertEqual(self.manager.flashcards[0].question, 'New Question')

    def test_delete_flashcard(self):
        self.manager.add_flashcard('Question 1', 'Answer 1', 'Topic 1', 'easy')
        self.manager.delete_flashcard(1)
        self.assertEqual(len(self.manager.flashcards), 0)

    def test_get_flashcards_by_topic(self):
        self.manager.add_flashcard('Question 1', 'Answer 1', 'Topic 1', 'easy')
        self.manager.add_flashcard('Question 2', 'Answer 2', 'Topic 2', 'medium')
        flashcards = self.manager.get_flashcards_by_topic('Topic 1')
        self.assertEqual(len(flashcards), 1)
        self.assertEqual(flashcards[0].question, 'Question 1')

    def test_get_flashcards_by_difficulty(self):
        self.manager.add_flashcard('Question 1', 'Answer 1', 'Topic 1', 'easy')
        self.manager.add_flashcard('Question 2', 'Answer 2', 'Topic 2', 'medium')
        flashcards = self.manager.get_flashcards_by_difficulty('easy')
        self.assertEqual(len(flashcards), 1)
        self.assertEqual(flashcards[0].question, 'Question 1')

if __name__ == '__main__':
    unittest.main()
