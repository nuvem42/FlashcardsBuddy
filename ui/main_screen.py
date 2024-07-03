from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Study by Difficulty', on_press=self.go_to_flashcard))
        layout.add_widget(Button(text='Study by Topic', on_press=self.go_to_topic))
        layout.add_widget(Button(text='Edit Flashcards', on_press=self.go_to_edit_flashcard))
        self.add_widget(layout)

    def go_to_flashcard(self, instance):
        self.manager.current = 'flashcard'

    def go_to_topic(self, instance):
        self.manager.current = 'topic'

    def go_to_edit_flashcard(self, instance):
        self.manager.current = 'edit_flashcard'
