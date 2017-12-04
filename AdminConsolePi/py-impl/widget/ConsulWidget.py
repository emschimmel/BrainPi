from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from kivy.network.urlrequest import UrlRequest

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
            
    Label:
        text: root.random_number
''')

class ConsulWidget(BoxLayout):
    def __init__(self, **kwargs):
        self.random_number = 'Loading data, please wait......'
        super(ConsulWidget, self).__init__(**kwargs)

    def got_json(self, request, data):
        print(data)
        self.random_number = 'data'

    def got_data(self, dt):
        UrlRequest('http://localhost:8500/v1/catalog/services', self.got_json)

    def start(self):
        print('start')
        Clock.schedule_interval(self.got_data, 2)

class Consul(App):

    def build(self):
        return ConsulWidget()

ConsulWidget().start()

