from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from models import FlashcardManager
from ai import AIModel

class FlashcardScreen(Screen):
    def __init__(self, **kwargs):
        super(FlashcardScreen, self).__init__(**kwargs)
        self.manager = FlashcardManager()
        self.ai_model = AIModel(self.manager.flashcards)
        self.layout = BoxLayout(orientation='vertical')
        self.flashcard_label = Label(text='Welcome to Flashcard Study')
        self.layout.add_widget(self.flashcard_label)
        self.easy_button = Button(text='Easy', on_press=self.mark_easy)
        self.medium_button = Button(text='Medium', on_press=self.mark_medium)
        self.hard_button = Button(text='Hard', on_press=self.mark_hard)
        self.layout.add_widget(self.easy_button)
        self.layout.add_widget(self.medium_button)
        self.layout.add_widget(self.hard_button)
        self.add_widget(self.layout)
        self.show_flashcard()

    def show_flashcard(self):
        flashcard = self.ai_model.get_recommendation()
        if flashcard:
            self.flashcard_label.text = flashcard.question
            self.current_flashcard = flashcard
        else:
            self.flashcard_label.text = 'No flashcards available'

    def mark_easy(self, instance):
        self.ai_model.update_difficulty(self.current_flashcard, 'easy')
        self.manager.save_flashcards()
        self.show_flashcard()

    def mark_medium(self, instance):
        self.ai_model.update_difficulty(self.current_flashcard, 'medium')
        self.manager.save_flashcards()
        self.show_flashcard()

    def mark_hard(self, instance):
        self.ai_model.update_difficulty(self.current_flashcard, 'hard')
        self.manager.save_flashcards()
        self.show_flashcard()
