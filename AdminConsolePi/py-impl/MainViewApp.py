from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from WidgetPanelApp import WidgetPanelApp

root = Builder.load_string('''
<ContainerBox>:
    canvas:
        Rectangle:
            size: self.size
            source: '../assets/background.png'

    rows: 1
    WidgetPanel:
        rows: 1
        row_force_default: True
''')

class WidgetPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(WidgetPanelApp.build(self), self).__init__(**kwargs)

class ContainerBox(GridLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class MainView(App):

    def build(self):
        return ContainerBox()
