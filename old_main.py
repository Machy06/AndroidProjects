import kivy
import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDFillRoundFlatButton, MDRectangleFlatButton
from kivymd.uix.list import OneLineListItem, IconLeftWidget, ThreeLineListItem, MDList
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

screen_helper = """
ScreenManager:
    id: 'screen_manager'
    MainScreen:
    PlusScreen:

<MainScreen>:
    name: 'main'
    Screen:
        NavigationLayout:
            ScreenManager:
                Screen:
                    
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: 0.9
                        ScrollView:
                            MDList:
                                id: list_one
                                    
                    MDFillRoundFlatIconButton:
                        icon: 'plus'
                        on_press: root.manager.current = 'plus'
                        pos_hint: {'center_x': 0.95, 'center_y': 0.1}
                    BoxLayout:
                        orientation: 'vertical'
                        MDToolbar:
                            title: 'Demo App'
                            left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                            elevation:10
                        Widget
            MDNavigationDrawer:
                id: nav_drawer
                
                
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo'
                        icon: 'git'
                    ScrollView:
                        MDList:
                            OneLineIconListItem:
                                text: 'Settings'
                                IconLeftWidget:
                                    icon: 'settings'
                            OneLineIconListItem:
                                text: 'Quit'
                                IconLeftWidget:
                                    icon: 'logout'
<PlusScreen>:
    name: 'plus'
    MDLabel:
        text: 'Demo'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'main'

"""


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create_list)

    def create_list(self, *args):
        for i in range(20):
            self.ids.list_one.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )

class PlusScreen(Screen):
    pass


class DemoApplicationApp(MDApp):
    def build(self):
        self.title = "DemoApp"
        self.screen = Builder.load_string(screen_helper)
        self.theme_cls.primary_palette = "Blue"
        # table = MDDataTable(pos_hint={"center_x": 0.5, "center_y": 0.5},
        #                     size_hint=(0.9, 0.6),
        #                     column_data=[("Food", dp(30)),
        #                                  ("Calories", dp(30)),
        #                                  ("Number", dp(20))],
        #                     row_data=[
        #                         ("Burger", "300", "1"),
        #                         ("Oats", "150", "2"),
        #                     ])
        # screen.add_widget(table)
        return self.screen

    def navigation_draw(self):
        print("Hello World")

    def settings(self):
        print("Settings")

    def PlusScreen(self):
        print("Hello")


DemoApplicationApp().run()
