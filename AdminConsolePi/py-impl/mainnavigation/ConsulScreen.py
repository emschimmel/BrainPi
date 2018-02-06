from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.ConsulWidget import Consul


Builder.load_file("mainnavigation/template/ConsulScreen.kv")

class ConsulScreen(Screen):
    def on_enter(self, *args):
        self.ids.widget.on_enter()

    def on_leave(self, *args):
        self.ids.widget.on_leave()

class ConsulWidget(BoxLayout):
    def __init__(self):
        super(ConsulWidget, self).__init__()

class Consul(App):
    def build(self):
        return ConsulScreen()


