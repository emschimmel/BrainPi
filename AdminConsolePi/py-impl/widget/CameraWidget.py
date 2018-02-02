from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("widget/template/CameraWidget.kv")

class CameraWidget(BoxLayout):
    pass

class Camera(App):

    def build(self):
        return CameraWidget()

