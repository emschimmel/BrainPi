from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup

root = Builder.load_string('''
#:import Factory kivy.factory.Factory
<LoginView@Popup>:
    title: 'Login to the admin console'
    auto_dismiss: False
    size_hint: None, None
    size: 500, 250

    BoxLayout
        orientation: 'vertical'
        padding: [10,30,10,30]
        spacing: 20           
                                
        BoxLayout:
            Label:
                width: 20
                text: 'Username'
                font_size: 16
                halign: 'left'
                align: 'left'
            TextInput:
                id: login
                multiline:False
                font_size: 16

        BoxLayout:
            Label:
                text: 'Password'
                halign: 'left'
                font_size: 16
            TextInput:
                id: password
                multiline:False
                password:True
                font_size: 16

        BoxLayout:
            Button:
                text: 'Exit'
                on_press: root.exit_application()
            Button:
                text: 'Test'
                on_press: root.dismiss()
            Button:
                text: 'Login'
                font_size: 16
                on_press: root.do_login(login.text, password.text)
''')

class LoginView(Popup):
    def __init__(self, **kwargs):
        super(LoginView, self).__init__(**kwargs)

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        print(app)

    def exit_application(self):
        App.get_running_app().stop()

class LoginViewApp(App):

    def build(self):
        return LoginView()
