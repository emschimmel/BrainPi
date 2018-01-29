from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.UserWidget import User

Builder.load_file("mainnavigation/template/UserScreen.kv")

class UserScreen(Screen):
    pass

class UserWidget(BoxLayout):
    pass


class User(App):
    def build(self):
        return UserScreen()


