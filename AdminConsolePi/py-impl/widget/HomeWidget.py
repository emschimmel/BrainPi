from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("widget/template/HomeWidget.kv")

class HomeWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(HomeWidget, self).__init__(**kwargs)


class Home(App):

    def build(self):
        return HomeWidget()

