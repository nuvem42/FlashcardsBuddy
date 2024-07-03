from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from models import FlashcardManager

class EditFlashcardScreen(Screen):
    def __init__(self, **kwargs):
        super(EditFlashcardScreen, self).__init__(**kwargs)
        self.manager = FlashcardManager()
        self.layout = BoxLayout(orientation='vertical')
        
        # Input fields for adding/editing flashcards
        self.question_input = TextInput(hint_text='Question')
        self.answer_input = TextInput(hint_text='Answer')
        self.topic_input = TextInput(hint_text='Topic')
        self.difficulty_input = TextInput(hint_text='Difficulty')
        
        self.layout.add_widget(self.question_input)
        self.layout.add_widget(self.answer_input)
        self.layout.add_widget(self.topic_input)
        self.layout.add_widget(self.difficulty_input)
        
        self.add_button = Button(text='Add Flashcard', on_press=self.add_flashcard)
        self.layout.add_widget(self.add_button)
        
        # Scroll view for existing flashcards
        self.scroll_view = ScrollView()
        self.flashcards_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.flashcards_layout.bind(minimum_height=self.flashcards_layout.setter('height'))
        self.scroll_view.add_widget(self.flashcards_layout)
        self.layout.add_widget(self.scroll_view)
        
        self.add_widget(self.layout)
        self.display_flashcards()

    def add_flashcard(self, instance):
        question = self.question_input.text
        answer = self.answer_input.text
        topic = self.topic_input.text
        difficulty = self.difficulty_input.text
        
        self.manager.add_flashcard(question, answer, topic, difficulty)
        # Clear input fields after adding
        self.question_input.text = ''
        self.answer_input.text = ''
        self.topic_input.text = ''
        self.difficulty_input.text = ''
        # Feedback to user
        print('Flashcard added successfully')
        self.display_flashcards()

    def display_flashcards(self):
        self.flashcards_layout.clear_widgets()
        for flashcard in self.manager.flashcards:
            card_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            card_layout.add_widget(Label(text=flashcard.question))
            edit_button = Button(text='Edit', size_hint_x=None, width=60, on_press=lambda instance, fc=flashcard: self.edit_flashcard(fc))
            delete_button = Button(text='Delete', size_hint_x=None, width=60, on_press=lambda instance, id=flashcard.id: self.delete_flashcard(id))
            card_layout.add_widget(edit_button)
            card_layout.add_widget(delete_button)
            self.flashcards_layout.add_widget(card_layout)

    def edit_flashcard(self, flashcard):
        self.question_input.text = flashcard.question
        self.answer_input.text = flashcard.answer
        self.topic_input.text = flashcard.topic
        self.difficulty_input.text = flashcard.difficulty
        self.add_button.text = 'Update Flashcard'
        self.add_button.unbind(on_press=self.add_flashcard)
        self.add_button.bind(on_press=lambda instance: self.update_flashcard(flashcard.id))

    def update_flashcard(self, id):
        question = self.question_input.text
        answer = self.answer_input.text
        topic = self.topic_input.text
        difficulty = self.difficulty_input.text
        self.manager.edit_flashcard(id, question, answer, topic, difficulty)
        # Clear input fields and reset button
        self.question_input.text = ''
        self.answer_input.text = ''
        self.topic_input.text = ''
        self.difficulty_input.text = ''
        self.add_button.text = 'Add Flashcard'
        self.add_button.unbind(on_press=self.update_flashcard)
        self.add_button.bind(on_press=self.add_flashcard)
        print('Flashcard updated successfully')
        self.display_flashcards()

    def delete_flashcard(self, id):
        self.manager.delete_flashcard(id)
        print('Flashcard deleted successfully')
        self.display_flashcards()
