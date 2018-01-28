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
from kivy.uix.button import Button

from random import sample
from string import ascii_lowercase
import time
import urllib.request
import urllib.error
import urllib.parse
import json
from kivy.graphics import Color

Builder.load_file("widget/template/ConsulWidget.kv")

class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        print('hey touch')
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        print('apply selection')
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

class ConsulWidget(BoxLayout):
    state = 'all'
    data = ListProperty([])
    rv_data = ListProperty([])

    def __init__(self, **kwargs):
        self.random_number = 'Loading data, please wait......'
        super(ConsulWidget, self).__init__(**kwargs)
        self.make_data_request()

    def make_data_request(self):
        print('make data request')
        req = urllib.request.Request('http://localhost:8500/v1/internal/ui/services?dc=dc1&token=')
        try:
            response = urllib.request.urlopen(req)
            self.data = json.loads(response.read().decode('utf-8'))
            self.test_subset()
        except urllib.error.URLError as e:
            print(e.reason)

    def test_subset(self, state=state):
        if not len(self.data):
            self.make_data_request()
        else:
            self.state = state

            self.rv_data = [{'name': str(item['Name']), 'passing' : str(item['ChecksPassing']), 'warning' : str(item['ChecksWarning']), 'critical': str(item['ChecksCritical']), 'statuscolor' : self.__setColor(item)} for item in self.data if self.__match_state(state, item)]

    @staticmethod
    def __match_state(state, item):
        if state is 'all':
            return True
        elif state is 'failing' and item['ChecksCritical'] or item['ChecksWarning']:
            return True
        elif state is 'succes' and not item['ChecksCritical'] and not item['ChecksWarning']:
            return True


    @staticmethod
    def __setColor(item):
        c = [0, 1, 0.3, 0.2]
        if item['ChecksCritical']:
            c = [1, 0, 0, 0.2]
        elif item['ChecksWarning']:
            c = [1, 0.6, 0, 0.2]
        return c

    def start(self):
        pass
        # Clock.schedule_interval(self.make_data_request, 2000)


class Consul(App):

    def build(self):
        return ConsulWidget()


widget = ConsulWidget()
widget.start()


