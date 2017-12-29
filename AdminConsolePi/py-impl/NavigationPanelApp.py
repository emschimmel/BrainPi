from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


root = Builder.load_string('''
<NavigationPanel>:
    
    canvas.before:            
        Color:
            rgba: 1, 1, 1, 0.3
        Rectangle:
            size: 0.976*self.width, 100
            pos: self.x+0.012*self.width, self.y+0.022*self.height
        
    Button:
        size: 100, 100
        text: 'Config'    
    Button:
        size: 100, 100
        text: 'Consul'   
''')

class NavigationPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(NavigationPanel, self).__init__(**kwargs)

class NavigationPanelApp(App):

    def build(self):
        return NavigationPanel()
