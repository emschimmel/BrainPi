from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.screenmanager import Screen

from NavigationPanelApp import NavigationPanel

from mainscreen.ConsulScreen import ConsulScreen
from mainscreen.UserScreen import UserScreen
from mainscreen.UserListScreen import UserListScreen
from mainscreen.WeatherScreen import WeatherScreen
from mainscreen.CameraScreen import CameraScreen

Builder.load_file("template/MainView.kv")

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
