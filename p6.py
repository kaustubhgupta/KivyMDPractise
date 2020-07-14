from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from helpers import username_helper


class App(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = 'Green'
        btn = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                    on_release=self.showData)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(btn)
        return screen

    def showData(self, obj):
        if self.username.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + ' does not exist'

        close = MDFlatButton(text='Close', on_release=self.close_dia)
        more_button = MDFlatButton(text='More')
        self.dia = MDDialog(text=check_string,
                            title='Username check',
                            size_hint=(0.7, 1),
                            buttons=[close, more_button])
        self.dia.open()

    def close_dia(self, obj):
        self.dia.dismiss()


App().run()
