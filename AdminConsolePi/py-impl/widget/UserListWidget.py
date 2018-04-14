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

from ConnectionHelpers.ConnectEarPi import ConnectEarPi

from EarPi.ttypes import EarPiAuthObject

from widget.ConsulDetails import ConsulDetailsApp
from widget.ConsulDetailsModel import ConsulDetailsModel
from widget.ConsulDetailsModel import ConsulChecksModel

from thrift import Thrift

Builder.load_file("widget/template/UserListWidget.kv")


class DetailButton(ButtonBehavior, Label):

    def __init__(self, **kwargs):
        super(DetailButton, self).__init__(**kwargs)

class UserListWidget(BoxLayout):
    state = 'all'
    data = ListProperty([])
    rv_data = ListProperty([])

    def __init__(self, **kwargs):
        super(UserListWidget, self).__init__(**kwargs)

    def on_enter(self):
        print('on_enter')
        self.getUserList()

    def on_leave(self):
        print('on_leave')

    # def make_data_request(self):
    #     req = urllib.request.Request('http://localhost:8500/v1/internal/ui/services?dc=dc1&token=')
    #     try:
    #         response = urllib.request.urlopen(req)
    #         self.data = json.loads(response.read().decode('utf-8'))
    #         self.test_subset()
    #     except urllib.error.URLError as e:
    #         print(e.reason)
    #
    # def test_subset(self, state=state):
    #     if not len(self.data):
    #         self.make_data_request()
    #     else:
    #         self.state = state
    #
    #         self.rv_data = [{'name': str(item['Name']), 'passing' : str(item['ChecksPassing']), 'warning' : str(item['ChecksWarning']), 'critical': str(item['ChecksCritical']), 'statuscolor' : self.__setColor(item)} for item in self.data if self.__match_state(state, item)]


    def getUserList(self):
        try:
            tokenInput = self.createEarPiAuthObject()
            output = ConnectEarPi().getUserList(tokenInput)
            app = App.get_running_app()
            app.token = output.token
            if output.personList:
                print("%d items" % len(output.personList))
            else:
                print("test fail 0 items")
            if self.__displayLists:
                for item in output.personList:
                    print(item)
        except Thrift.TException as tx:
            print("%s" % (tx.message))


    def createEarPiAuthObject(self):
        app = App.get_running_app()

        tokenObject = EarPiAuthObject()
        tokenObject.token = app.token
        tokenObject.deviceToken = app.deviceToken
        return tokenObject

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

class UserList(App):

    def build(self):
        return UserListWidget()
