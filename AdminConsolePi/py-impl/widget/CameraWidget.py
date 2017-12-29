from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from kivy.network.urlrequest import UrlRequest

root = Builder.load_string('''
<CameraWidget>:    
    canvas.before:    
        Color:
            rgba: 1, 1, 1, 0.8    
        Line:
            rectangle: self.x+0.015*self.width, self.y+0.02*self.height, 0.97*self.width, 0.96*self.height
        Color:
            rgba: 1, 1, 1, 0.3
        Rectangle:
            size: 0.976*self.width, 0.96*self.height
            pos: self.x+0.012*self.width, self.y+0.022*self.height 
            
    Camera:
        id: camera
        resolution: 399, 299        
''')

class CameraWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraWidget, self).__init__(**kwargs)


class Camera(App):

    def build(self):
        return CameraWidget()

