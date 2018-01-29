from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.UserListWidget import UserList

Builder.load_file("mainnavigation/template/UserListScreen.kv")

class UserListScreen(Screen):
    pass

class UserListWidget(BoxLayout):
    pass


class UserList(App):
    def build(self):
        return UserListScreen()


