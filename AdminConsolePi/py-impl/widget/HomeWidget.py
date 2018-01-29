from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

import widget.ConsulWidget

Builder.load_file("widget/template/HomeWidget.kv")

class HomeWidget(BoxLayout):
    pass

class Home(App):

    def build(self):
        return HomeWidget()

