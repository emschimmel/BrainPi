from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("widget/template/CameraWidget.kv")

class CameraWidget(BoxLayout):

    def on_enter(self):
        print('on_enter')
        self.ids.camera.play = True

    def on_leave(self):
        print('on_leave')
        self.ids.camera.play = False

class Camera(App):

    def build(self):
        return CameraWidget()

