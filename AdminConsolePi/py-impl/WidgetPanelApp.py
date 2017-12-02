from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from widget.ConsulWidget import Consul

root = Builder.load_string('''
<WidgetPanel>:
    canvas.before:    
        Color:
            rgba: 1, 1, 1, 0.8    
        Line:
            rectangle: self.x+0.02*self.width, self.y+0.02*self.height, 0.96*self.width, 0.96*self.height
            
        Color:
            rgba: 1, 1, 1, 0.3
        Rectangle:
            size: 0.956*self.width, 0.956*self.height
            pos: self.x+0.022*self.width, self.y+0.022*self.height
            
	padding: 20
	spacing: 20
    
    orientation: 'horizontal'
    ConsulWidget:    
''')

class ConsulWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(Consul.build(self), self).__init__(**kwargs)

class WidgetPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(WidgetPanel, self).__init__(**kwargs)

class WidgetPanelApp(App):

    def build(self):
        return WidgetPanel()
