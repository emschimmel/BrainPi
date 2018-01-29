from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.UserListWidget import UserList

Builder.load_file("mainnavigation/template/UserListScreen.kv")

class UserListScreen(Screen):
    pass

class UserListWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(UserListWidget.build(self), self).__init__(**kwargs)

class UserList(App):
    def build(self):
        return UserListScreen()


