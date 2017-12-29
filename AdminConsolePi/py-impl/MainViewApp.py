from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from NavigationPanelApp import NavigationPanel

from widget.ConsulWidget import Consul
from widget.WeatherWidget import Weather
from widget.CameraWidget import Camera

root = Builder.load_string('''
<ContainerBox>:
    canvas:
        Rectangle:
            size: self.size
            source: '../assets/background.png'
                    
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'Consul'
                ConsulWidget:
                    size: self.size
                    pos: self.pos
                    rows: 1
                    row_force_default: True
            Screen:
                name: 'Weather'
                WeatherWidget:
                    size: self.size
                    pos: self.pos
                    rows: 1
                    row_force_default: True
            Screen:
                name: 'Camera'
                CameraWidget:
                    size: self.size
                    pos: self.pos
                    rows: 1
                    row_force_default: True                    
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: .7, .1
            Button:
                text: 'Consul'
                on_press:
                    _screen_manager.transition.direction = 'up'
                    _screen_manager.current = 'Consul'
            Button:
                text: 'Weather'
                on_press:
                    _screen_manager.transition.direction = 'up'
                    _screen_manager.current = 'Weather'        
            Button:
                text: 'Camera'
                on_press: 
                    _screen_manager.transition.direction = 'up'
                    _screen_manager.current = 'Camera'      
            Button:
                text: 'Exit'
                on_press: app.stop()        
''')

class ConsulWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(ConsulWidget.build(self), self).__init__(**kwargs)

class WeatherWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(WeatherWidget.build(self), self).__init__(**kwargs)

class CameraWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraWidget.build(self), self).__init__(**kwargs)

class NavigationPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(NavigationPanel.build(self), self).__init__(**kwargs)

class ContainerBox(FloatLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class MainView(App):

    def build(self):
        return ContainerBox()
