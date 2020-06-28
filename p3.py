from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = 'A700'  # to make it very dark or light
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hi Kaustubh!', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_flat)
        return screen


App().run()
