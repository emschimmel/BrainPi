from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup

Builder.load_file("template/ErrorView.kv")

class ErrorView(Popup):
    def __init__(self, **kwargs):
        super(ErrorView, self).__init__(**kwargs)

    def exit_application(self):
        App.get_running_app().stop()

class ErrorViewApp(App):

    def build(self):
        return ErrorView()
