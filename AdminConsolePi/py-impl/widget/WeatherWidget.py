from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file("widget/template/WeatherWidget.kv")

class WeatherWidget(BoxLayout):
    def __init__(self, **kwargs):
        self.random_number = 'Before';
        super(WeatherWidget, self).__init__(**kwargs)

    def change_text(self):
        self.random_number = 'After'
        print('After')

class Weather(App):

    def build(self):
        return WeatherWidget()
