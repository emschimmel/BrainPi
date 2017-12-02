from kivy.app import App

from MainViewApp import MainView

class AdminConsoleApp(App):
    def build(self):
        return MainView.build(self)

AdminConsoleApp().run()