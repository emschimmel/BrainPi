from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("mainnavigation/template/NavigationPanel.kv")

class NavigationPanel(BoxLayout):
    pass

class NavigationPanelApp(App):

    def build(self):
        return NavigationPanel()
