from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, ThreeLineIconListItem
from kivymd.uix.list import IconLeftWidget
from kivy.uix.scrollview import ScrollView


class App(MDApp):

    def build(self):
        screen = Screen()
        list_view = MDList()
        scroll = ScrollView()

        for i in range(20):
            icon = IconLeftWidget(icon='android')
            item = ThreeLineIconListItem(text='Item ' + str(i), secondary_text='Hello', tertiary_text='world')
            item.add_widget(icon)
            list_view.add_widget(item)

        scroll.add_widget(list_view)
        screen.add_widget(scroll)
        return screen


App().run()