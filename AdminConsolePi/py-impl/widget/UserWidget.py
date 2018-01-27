from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty

Builder.load_file("widget/template/UserWidget.kv")

class UserWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(UserWidget, self).__init__(**kwargs)

    is_active = BooleanProperty(True)


class User(App):

    def build(self):
        return UserWidget()

