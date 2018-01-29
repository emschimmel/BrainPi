from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.screenmanager import Screen

from mainnavigation.NavigationPanelApp import NavigationPanel

from mainnavigation.ConsulScreen import ConsulScreen
from mainnavigation.UserScreen import UserScreen
from mainnavigation.UserListScreen import UserListScreen
from mainnavigation.WeatherScreen import WeatherScreen
from mainnavigation.CameraScreen import CameraScreen

Builder.load_file("mainnavigation/template/MainView.kv")

class ConsulScreen(Screen):
    def __init__(self, **kwargs):
        super(ConsulScreen.build(self), self).__init__(**kwargs)

class UserScreen(Screen):
    def __init__(self, **kwargs):
        super(UserScreen.build(self), self).__init__(**kwargs)

class UserListScreen(Screen):
    def __init__(self, **kwargs):
        super(UserListScreen.build(self), self).__init__(**kwargs)

class WeatherScreen(Screen):
    def __init__(self, **kwargs):
        super(WeatherScreen.build(self), self).__init__(**kwargs)

class CameraScreen(Screen):
    def __init__(self, **kwargs):
        super(CameraScreen.build(self), self).__init__(**kwargs)

class NavigationPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(NavigationPanel.build(self), self).__init__(**kwargs)

class ContainerBox(FloatLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class MainView(App):

    def build(self):
        return ContainerBox()
