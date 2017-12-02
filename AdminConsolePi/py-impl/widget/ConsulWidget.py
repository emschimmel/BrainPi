from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

root = Builder.load_string('''
<ConsulWidget>:    
    canvas.before:    
        Color:
            rgba: 1, 1, 1, 0.8    
        Line:
            rectangle: self.x, self.y, self.width, self.height
            
        Color:
            rgba: 1, 1, 1, 0.3
        Rectangle:
            size: 0.995*self.width, 0.995*self.height
            pos: self.x+0.0025*self.width, self.y+0.0025*self.height
''')

class ConsulWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConsulWidget, self).__init__(**kwargs)

class Consul(App):

    def build(self):
        return ConsulWidget()
