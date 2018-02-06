from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.CameraWidget import Camera


Builder.load_file("mainnavigation/template/CameraScreen.kv")

class CameraScreen(Screen):

    def on_enter(self, *args):
        self.ids.widget.on_enter()

    def on_leave(self, *args):
        self.ids.widget.on_leave()

class CameraWidget(BoxLayout):
    def __init__(self):
        super(CameraWidget, self).__init__()

class Camera(App):
    def build(self):
        return CameraScreen()


