from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.uix.behaviors import ButtonBehavior

import urllib.request
import urllib.error
import urllib.parse
import json

from widget.ConsulDetails import ConsulDetailsApp
from widget.ConsulDetailsModel import ConsulDetailsModel
from widget.ConsulDetailsModel import ConsulChecksModel

Builder.load_file("widget/template/ConsulWidget.kv")


class DetailButton(ButtonBehavior, Label):

    def __init__(self, **kwargs):
        super(DetailButton, self).__init__(**kwargs)

    def display_details(self, name):
        print("Show details for %s" % name)
        details_model = self.__make_details_object(name)
        popup = ConsulDetailsApp(details_model).build()
        popup.open()

    @staticmethod
    def __make_details_object(name):
        details_model = ConsulDetailsModel()
        details_model.name = name
        req = urllib.request.Request('http://localhost:8500/v1/health/service/%s?dc=dc1&token=' % name)
        try:
            response = urllib.request.urlopen(req)
            data = json.loads(response.read().decode('utf-8'))
            details_model.service_id = data[0]['Service']['ID']
            details_model.service_name = data[0]['Service']['Service']
            details_model.service_adres = data[0]['Service']['Address']
            details_model.service_port = data[0]['Service']['Port']
            for check in data[0]['Checks']:
                checkObject = ConsulChecksModel()
                checkObject.check_id = check['CheckID']
                checkObject.name = check['Name']
                checkObject.status = check['Status']
                checkObject.output = check['Output']
                checkObject.service_id = check['ServiceID']
                checkObject.service_name = check['ServiceName']
                checkObject.status_color(check['Status'])
                details_model.checks.append(checkObject)
        except urllib.error.URLError as e:
            print(e.reason)
        return details_model

class ConsulWidget(BoxLayout):
    state = 'all'
    data = ListProperty([])
    rv_data = ListProperty([])

    def __init__(self, **kwargs):
        super(ConsulWidget, self).__init__(**kwargs)

    def on_enter(self):
        print('on_enter')
        self.make_data_request()
        self.start()

    def on_leave(self):
        print('on_leave')
        self.stop()

    def make_data_request(self):
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
        print('Start data refresh timer')
        Clock.schedule_interval(self.refresh_data, 5)

    def stop(self):
        print('Stop data refresh timer')
        Clock.unschedule(self.refresh_data)

    def refresh_data(self, dt):
        print('refresh consul data')
        self.data = []
        self.make_data_request()

class Consul(App):

    def build(self):
        return ConsulWidget()
