from kivy.app import App

from mainnavigation.MainViewApp import MainView
from authentication.LoginViewApp import LoginViewApp

import i18n


class AdminConsoleApp(App):
    def build(self):
        self.load_translations()
        config = self.config
        print(config)
        deviceToken = config.get('application', 'devicetoken')

        if deviceToken:
            self.get_running_app().deviceToken = deviceToken
        else:
            self.get_running_app().deviceToken = None

        return MainView.build(self)

    def build_config(self, config):
        config.setdefaults('consul', {
            'host': '127.0.0.1',
            'port': '8600'
        })
        config.setdefaults('application', {
            'devicetoken': 'None'
        })

    def get_application_config(self):
        return super(AdminConsoleApp, self).get_application_config(
            'adminconsole.ini')

    def on_start(self, **kwargs):
        popup = LoginViewApp.build(self)
        popup.open()

    def load_translations(self):
        i18n.load_path.append('translations')
        i18n.set('locale', 'en')
        i18n.set('fallback', 'en')
        self.get_running_app().i18n = i18n

AdminConsoleApp().run()