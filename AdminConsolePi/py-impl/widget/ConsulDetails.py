from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.properties import ListProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior


Builder.load_file("widget/template/ConsulDetails.kv")

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''
    pass


class ConsulDetails(Popup):
    checks = ListProperty([])

    def __init__(self, details, **kwargs):
        self.details = details
        self.checks = details.checks
        super(ConsulDetails, self).__init__(**kwargs)

    def exit_application(self):
        App.get_running_app().stop()

class ConsulDetailsApp(App):

    def __init__(self, details, **kwargs):
        self.details = details
        super(ConsulDetailsApp, self).__init__(**kwargs)

    def build(self):
        return ConsulDetails(self.details)
