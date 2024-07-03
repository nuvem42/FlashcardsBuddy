from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ui.main_screen import MainScreen
from ui.flashcard_screen import FlashcardScreen
from ui.topic_screen import TopicScreen
from ui.edit_flashcard_screen import EditFlashcardScreen

class FlashcardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FlashcardScreen(name='flashcard'))
        sm.add_widget(TopicScreen(name='topic'))
        sm.add_widget(EditFlashcardScreen(name='edit_flashcard'))
        return sm

if __name__ == '__main__':
    FlashcardApp().run()
