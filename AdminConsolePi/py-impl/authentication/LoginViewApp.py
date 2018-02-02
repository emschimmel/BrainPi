import sys

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.config import Config

sys.path.append('../gen-py')

from EyePi import EyePiThriftService
from EyePi.ttypes import *
from AutorisationStruct.ttypes import *

from ConnectionHelpers.ConnectEyePi import ConnectEyePi
from ConnectionHelpers.PasswordHelper import PasswordHelper

from ThriftException.ttypes import *
from thrift import Thrift

Builder.load_file("authentication/template/LoginView.kv")

class LoginView(Popup):
    def __init__(self, **kwargs):
        super(LoginView, self).__init__(**kwargs)

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        try:

            input = LoginInputObject()
            input.username = loginText
            __password = PasswordHelper.hashPassword(passwordText)
            input.password = PasswordHelper.encryptPassword(__password)
            input.code = PasswordHelper.encryptPassword(PasswordHelper.hashPassword('123456ABCD'))
            input.token = None

            if app.deviceToken!='None':
                input.deviceToken = app.deviceToken
            else:
                input.deviceToken = 'ABCDEFGH'

            inputDevice = DeviceTokenInput()
            inputDevice.ip = '127.0.0.1'
            inputDevice.devicetype = 'Development'
            input.deviceInput = inputDevice

            output = ConnectEyePi().login(input)


            print(output)
            if (output is None):
                self.ids.message.text = app.i18n.t('admin.invalid_login')
                return

            if output.deviceToken:
                app.deviceToken = output.deviceToken

            if (output.token is None):
                self.ids.message.text = app.i18n.t('admin.account_not_enabled')
                return

            self.dismiss()

        except Thrift.TException as tx:
            print("%s" % (tx.message))

    def translate(self, key):
        app = App.get_running_app()
        return app.i18n.t(key)

    def exit_application(self):
        App.get_running_app().stop()

class LoginViewApp(App):

    def build(self):
        return LoginView()
