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

root = Builder.load_string('''
#:import Factory kivy.factory.Factory
<LoginView@Popup>:
    title: 'Login to the admin console'
    auto_dismiss: False
    size_hint: None, None
    size: 500, 300

    BoxLayout
        orientation: 'vertical'
        padding: [10,30,10,30]
        spacing: 20           
                                
        BoxLayout:
            Label:
                width: 20
                text: 'Username'
                font_size: 16
                halign: 'left'
                align: 'left'
            TextInput:
                id: login
                multiline:False
                font_size: 16

        BoxLayout:
            Label:
                text: 'Password'
                halign: 'left'
                font_size: 16
            TextInput:
                id: password
                multiline:False
                password:True
                font_size: 16

        BoxLayout:
            Label:
                id: message
                color: 0.988, 0.388, 0.365

        BoxLayout:
            Button:
                text: root.translate('admin.exit')
                on_press: root.exit_application()
            Button:
                text: root.translate('admin.test')
                on_press: root.dismiss()
            Button:
                text: root.translate('admin.login')
                font_size: 16
                on_press: root.do_login(login.text, password.text)
''')

class LoginView(Popup):
    def __init__(self, **kwargs):
        super(LoginView, self).__init__(**kwargs)

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        try:

            input = LoginInputObject()
            input.username = loginText
            input.password = PasswordHelper.encryptPassword(PasswordHelper.hashPassword(passwordText))
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

            if (output is None):
                self.ids.message.text = app.i18n.t('admin.invalid_login')
                return

            if output.deviceToken:
                app.deviceToken = output.deviceToken

            if (output.token is None):
                self.ids.message.text = app.i18n.t('admin.account_not_enabled')
                return

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
