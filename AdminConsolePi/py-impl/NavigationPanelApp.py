from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("template/NavigationPanel.kv")

class NavigationPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(NavigationPanel, self).__init__(**kwargs)

class NavigationPanelApp(App):

    def build(self):
        return NavigationPanel()
