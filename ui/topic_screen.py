from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from models import FlashcardManager

class TopicScreen(Screen):
    def __init__(self, **kwargs):
        super(TopicScreen, self).__init__(**kwargs)
        self.manager = FlashcardManager()
        self.layout = BoxLayout(orientation='vertical')
        
        # Scroll view for topics
        self.scroll_view = ScrollView(size_hint=(1, None), size=(self.width, self.height / 2))
        self.topics_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.topics_layout.bind(minimum_height=self.topics_layout.setter('height'))
        self.scroll_view.add_widget(self.topics_layout)
        self.layout.add_widget(self.scroll_view)
        
        self.add_widget(self.layout)
        
        # Placeholder for flashcards layout
        self.flashcards_layout = BoxLayout(orientation='vertical')
        
        # Load topics
        self.load_topics()
    
    def load_topics(self):
        self.topics_layout.clear_widgets()
        self.layout.remove_widget(self.flashcards_layout)
        self.layout.add_widget(self.scroll_view)
        
        topics = set(fc.topic for fc in self.manager.flashcards)
        for topic in topics:
            topic_button = Button(text=topic, size_hint_y=None, height=40, on_press=self.select_topic)
            self.topics_layout.add_widget(topic_button)
    
    def select_topic(self, instance):
        selected_topic = instance.text
        flashcards = self.manager.get_flashcards_by_topic(selected_topic)
        
        # Remove topics view and show flashcards for the selected topic
        self.layout.remove_widget(self.scroll_view)
        self.flashcards_layout.clear_widgets()
        
        for flashcard in flashcards:
            flashcard_label = Label(text=f"Q: {flashcard.question}\nA: {flashcard.answer}")
            self.flashcards_layout.add_widget(flashcard_label)
        
        back_button = Button(text='Back to Topics', size_hint_y=None, height=40, on_press=self.load_topics)
        self.flashcards_layout.add_widget(back_button)
        
        self.layout.add_widget(self.flashcards_layout)

# main.py (For reference)
if __name__ == '__main__':
    FlashcardApp().run()
