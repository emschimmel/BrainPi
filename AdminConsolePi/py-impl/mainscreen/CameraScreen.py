from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.CameraWidget import Camera

Builder.load_file("mainscreen/template/CameraScreen.kv")

class CameraScreen(Screen):
    pass

class CameraWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraWidget.build(self), self).__init__(**kwargs)

class Camera(App):
    def build(self):
        return CameraScreen()


