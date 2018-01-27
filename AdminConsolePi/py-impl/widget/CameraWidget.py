from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from kivy.network.urlrequest import UrlRequest

Builder.load_file("widget/template/CameraWidget.kv")

class CameraWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraWidget, self).__init__(**kwargs)


class Camera(App):

    def build(self):
        return CameraWidget()

