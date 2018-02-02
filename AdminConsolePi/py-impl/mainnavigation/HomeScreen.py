from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.HomeWidget import Home

Builder.load_file("mainnavigation/template/HomeScreen.kv")

class HomeScreen(Screen):
    pass

class HomeWidget(BoxLayout):
    pass

class Home(App):
    def build(self):
        return HomeScreen()


