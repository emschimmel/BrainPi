from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty
from kivy.uix.recycleview import RecycleView

from random import sample
from string import ascii_lowercase

root = Builder.load_string('''
<Row@BoxLayout>:
    canvas.before:
        Color:
            rgba: 0.5, 0.5, 0.5, 1
        Rectangle:
            size: self.size
            pos: self.pos
    value: ''
    Label:
        text: root.value
        
<UserListWidget>:    
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
        
    BoxLayout:
        padding: 20, 20, 20, 20
        orientation: 'vertical'
        size_hint: .9, .9      

        rv: rv

        Button:
            text: 'Populate list'
            on_press: root.populate()
        
        RecycleView:
            id: rv
            scroll_type: ['bars', 'content']
            scroll_wheel_distance: dp(114)
            bar_width: dp(10)
            viewclass: 'Row'
            RecycleBoxLayout:
                default_size: dp(56), dp(56)
                default_size_hint: 1, 1
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
                spacing: dp(2)
            
''')

class UserListWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(UserListWidget, self).__init__(**kwargs)

    def populate(self):
        self.rv.data = [{'value': ''.join(sample(ascii_lowercase, 6))}
                        for x in range(50)]

    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['value'])

    def clear(self):
        self.rv.data = []

    def insert(self, value):
        self.rv.data.insert(0, {'value': value or 'default value'})

    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['value'] = value or 'default new value'
            self.rv.refresh_from_data()

    def remove(self):
        if self.rv.data:
            self.rv.data.pop(0)


class UserList(App):

    def build(self):
        return UserListWidget()

