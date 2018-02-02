from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.CameraWidget import Camera


Builder.load_file("mainnavigation/template/CameraScreen.kv")

class CameraScreen(Screen):
    pass

class CameraWidget(BoxLayout):
    pass

class Camera(App):
    def build(self):
        return CameraScreen()


