from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

root = Builder.load_string('''
<WeatherWidget>:
    canvas.before:    
        Color:
            rgba: 1, 1, 1, 0.8    
        Line:
            rectangle: self.x, self.y, self.width, self.height
            
        Color:
            rgba: 1, 1, 1, 0.3
        Rectangle:
            size: 0.995*self.width, 0.995*self.height
            pos: self.x+0.0025*self.width, self.y+0.0025*self.height
            
	padding: 5, 5, 5, 5
        
    StackLayout:
        orientation: 'lr-tb'
        search: id_search
        Label:
            size_hint: None, 0.05
            text: "Search"
        TextInput:
            size_hint: None, 0.05
            width: 150
            id: id_search
            text: root.random_number
        Button:
            size_hint: None, 0.05
            text: "click"
            on_release: root.change_text
''')

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
