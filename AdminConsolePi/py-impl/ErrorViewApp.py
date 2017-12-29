from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup

root = Builder.load_string('''
#:import Factory kivy.factory.Factory
<ErrorView@Popup>:
    title: 'Unable to locate available service connection'
    auto_dismiss: False
    size_hint: None, None
    size: 400, 150

    BoxLayout
        orientation: 'vertical'
        padding: [10,30,10,30]
        spacing: 20           
                                
        BoxLayout:
            Button:
                text: 'Exit application'
                on_press: root.exit_application()
''')

class ErrorView(Popup):
    def __init__(self, **kwargs):
        super(ErrorView, self).__init__(**kwargs)

    def exit_application(self):
        App.get_running_app().stop()

class ErrorViewApp(App):

    def build(self):
        return ErrorView()
