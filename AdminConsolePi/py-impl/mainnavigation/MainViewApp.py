from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.screenmanager import Screen

from mainnavigation.NavigationPanelApp import NavigationPanel

from mainnavigation.HomeScreen import HomeScreen
from mainnavigation.ConsulScreen import ConsulScreen
from mainnavigation.UserScreen import UserScreen
from mainnavigation.UserListScreen import UserListScreen
from mainnavigation.WeatherScreen import WeatherScreen
from mainnavigation.CameraScreen import CameraScreen

Builder.load_file("mainnavigation/template/MainView.kv")

class HomeScreen(Screen):
    pass

class ConsulScreen(Screen):
    pass


class UserScreen(Screen):
    pass

class UserListScreen(Screen):
    pass

class WeatherScreen(Screen):
    pass

class CameraScreen(Screen):
    pass

class NavigationPanel(BoxLayout):
    pass

class ContainerBox(FloatLayout):
    pass

class MainView(App):

    def build(self):
        return ContainerBox()
