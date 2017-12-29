from kivy.app import App

from MainViewApp import MainView
from LoginViewApp import LoginViewApp
from AppConfig import AppConfig


class AdminConsoleApp(App):
    def build(self):
        return MainView.build(self)

    def build_config(self, config):
        config.setdefaults('consul', {
            'host': '127.0.0.1',
            'port': '8600'
        })

    def get_application_config(self):
        return super(AdminConsoleApp, self).get_application_config(
            'adminconsole.ini')

    def on_start(self, **kwargs):
        ip, port = AppConfig().resolve_config(self.config.get('consul', 'host'), self.config.getint('consul', 'port'))

        print(ip)
        print(port)

        popup = LoginViewApp.build(self)
        popup.open()

AdminConsoleApp().run()