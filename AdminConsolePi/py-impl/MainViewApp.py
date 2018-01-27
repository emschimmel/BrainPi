from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from NavigationPanelApp import NavigationPanel

from widget.ConsulWidget import Consul
from widget.UserWidget import User
from widget.UserListWidget import UserList
from widget.WeatherWidget import Weather
from widget.CameraWidget import Camera

Builder.load_file("template/MainView.kv")

class ConsulWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConsulWidget.build(self), self).__init__(**kwargs)

class UserWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(UserWidget.build(self), self).__init__(**kwargs)

class UserListWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(UserListWidget.build(self), self).__init__(**kwargs)

class WeatherWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(WeatherWidget.build(self), self).__init__(**kwargs)

class CameraWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraWidget.build(self), self).__init__(**kwargs)

class NavigationPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(NavigationPanel.build(self), self).__init__(**kwargs)

class ContainerBox(FloatLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class MainView(App):

    def build(self):
        return ContainerBox()
