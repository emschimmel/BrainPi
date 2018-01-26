from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from kivy.network.urlrequest import UrlRequest

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, ListProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

from random import sample
from string import ascii_lowercase
import time
import urllib.request
import urllib.error
import urllib.parse
import json

root = Builder.load_string('''
<Row@BoxLayout>:
    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        Rectangle:
            size: self.size
            pos: self.pos
    name: ''
    Label:
        text: root.name
        
<ConsulWidget>:    
    canvas:
        Color:
            rgba: 0.3, 0.3, 0.3, 1
        Rectangle:
            size: self.size
            pos: self.pos
    rv: rv
    orientation: 'vertical'
    GridLayout:
        cols: 3
        rows: 1
        size_hint_y: None
        height: dp(108)
        padding: dp(8)
        spacing: dp(16)
        Button:
            text: 'All services'
            on_press: root.test_subset('all')
        Button:
            text: 'Failing services'
            on_press: root.test_subset('failing')
        Button:
            text: 'Success services'
            on_press: root.test_subset('succes')

    RecycleView:
        id: rv
        scroll_type: ['bars', 'content']
        scroll_wheel_distance: dp(114)
        bar_width: dp(10)
        viewclass: 'Row'
        RecycleBoxLayout:
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            spacing: dp(2)
            
''')

class ConsulWidget(BoxLayout):
    state = 'all'
    data = ListProperty([])

    def __init__(self, **kwargs):
        self.random_number = 'Loading data, please wait......'
        super(ConsulWidget, self).__init__(**kwargs)

    def make_data_request(self):
        print('make data request')
        req = urllib.request.Request('http://localhost:8500/v1/internal/ui/services?dc=dc1&token=')
        try:
            response = urllib.request.urlopen(req)
            self.data = json.loads(response.read().decode('utf-8'))
            self.test_subset()
        except urllib.error.URLError as e:
            print(e.reason)

    def test_data(self):
        self.rv.data = [{'value': ''.join(sample(ascii_lowercase, 6))} for x in range(50)]

    def test_subset(self, state=state):
        if not len(self.data):
            self.make_data_request()
        else:
            self.state = state
            self.rv.data = [{'name': item['Name'], 'ChecksPassing' : item['ChecksPassing'], 'ChecksWarning' : item['ChecksWarning'], 'ChecksCritical': item['ChecksCritical']} for item in self.data]

    def start(self):
        pass
        #Clock.schedule_interval(self.make_data_request, 2000)


class Consul(App):

    def build(self):
        return ConsulWidget()

widget = ConsulWidget()
widget.start()
widget.make_data_request()

