from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

from widget.WeatherWidget import Weather

Builder.load_file("mainnavigation/template/WeatherScreen.kv")

class WeatherScreen(Screen):
    pass

class WeatherWidget(BoxLayout):
    pass

class Weather(App):
    def build(self):
        return WeatherScreen()


