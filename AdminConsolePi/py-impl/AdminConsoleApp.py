from kivy.app import App

from MainViewApp import MainView
from LoginViewApp import LoginViewApp

class AdminConsoleApp(App):
    def build(self):
        return MainView.build(self)

    def get_application_config(self):
        return super(AdminConsoleApp, self).get_application_config(
            'adminconsole.ini')

    def on_start(self, **kwargs):
        popup = LoginViewApp.build(self)
        popup.open()


AdminConsoleApp().run()