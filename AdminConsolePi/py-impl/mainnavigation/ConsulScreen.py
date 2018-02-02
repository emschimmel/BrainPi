from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.ConsulWidget import Consul


Builder.load_file("mainnavigation/template/ConsulScreen.kv")

class ConsulScreen(Screen):
    pass

class ConsulWidget(BoxLayout):
    pass

class Consul(App):
    def build(self):
        return ConsulScreen()


