from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.ConsulWidget import Consul


Builder.load_file("mainscreen/template/ConsulScreen.kv")

class ConsulScreen(Screen):
    pass

class ConsulWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConsulWidget.build(self), self).__init__(**kwargs)

class Consul(App):
    def build(self):
        return ConsulScreen()


