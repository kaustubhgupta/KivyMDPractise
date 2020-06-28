from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

# two modes of helper text: focus and persistent. Persistent always show on screen but in focus it shows only when textfield is selected
username_helper = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""


class App(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = 'Green'
        # this is for coded text field
        # username = MDTextField(text='Enter username', pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                      size_hint=(0.5, 1))
        # if you want constant size then give size_hint_x=None, width=value you want

        # now below will be using builder method to form text field

        username = Builder.load_string(username_helper)
        screen.add_widget(username)
        return screen


App().run()
