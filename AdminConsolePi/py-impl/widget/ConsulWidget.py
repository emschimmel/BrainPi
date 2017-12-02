from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

root = Builder.load_string('''
<ConsulWidget>:    
    orientation: 'vertical'
    padding: 5
    Button:
        id: execute1
        text: 'Execute 1'    
''')

class ConsulWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConsulWidget, self).__init__(**kwargs)

class Consul(App):

    def build(self):
        return ConsulWidget()
