from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class App(MDApp):
    def build(self):
        # label = MDLabel(text='Hi Kaustubh!', halign='center', theme_text_color='Error')
        label = MDLabel(text='Hi Kaustubh!', halign='center', theme_text_color='Custom',
                        text_color=(0.7, 0.3, 0.4, 1), font_style='H1')

        icon_label = MDIcon(icon='language-python', halign='center')
        return icon_label


App().run()
