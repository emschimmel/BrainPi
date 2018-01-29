from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.UserWidget import User

Builder.load_file("mainscreen/template/UserScreen.kv")

class UserScreen(Screen):
    pass

class UserWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(UserWidget.build(self), self).__init__(**kwargs)

class User(App):
    def build(self):
        return UserScreen()


