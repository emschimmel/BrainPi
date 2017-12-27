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
            rectangle: self.x+0.015*self.width, self.y+0.02*self.height, 0.97*self.width, 0.96*self.height
        Color:
            rgba: 1, 1, 1, 0.3
        Rectangle:
            size: 0.976*self.width, 0.96*self.height
            pos: self.x+0.012*self.width, self.y+0.022*self.height
            
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

