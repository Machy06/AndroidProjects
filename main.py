import kivy
import kivymd
# try:
#     import androidhelper as android
# except:
#     import android
# import pywhatkit
import qpython
from permissions import request_permissions, Permission
import androidhelper_r6 as android
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
from kivymd.uix.dialog import MDDialog
from kivy.utils import platform
import time

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
                        on_press: app.send_message()
                        pos_hint: {'center_x': 0.99, 'center_y': 0.1}
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


# droid = android.Android()


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
        self.screen = Builder.load_string(screen_helper)
        self.theme_cls.primary_palette = "Blue"
        request_permissions([Permission.SEND_SMS, Permission.INTERNET])
        return self.screen

    def send_message(self):
        droid = android.Android()
        droid.smsSend("420xxxxxxxxx", "Message")

    def navigation_draw(self):
        print("Hello World")

    def settings(self):
        print("Settings")

    def PlusScreen(self):
        print("Hello")


DemoApplicationApp().run()
