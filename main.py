#from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
#from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
#from kivymd.uix.textfield import MDTextField
#from kivymd.uix.label import MDLabel
#from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu
#from kivymd.uix.label import MDLabel

#for ads
from kivmob import KivMob, TestIds

#size screen
from kivy.core.window import Window
#Window.size = (320,620)

#from kivy.uix.image import Image
#from kivy.uix.screenmanager import Screen
#from kivymd.uix.button import MDRectangleFlatButton
#from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp

from kivy.clock import Clock
from kivy.uix.label import Label

#from sysinfo import show_info_system
#App.get_running_app().root.ids['nav_drawer']]
with open('main.kv','r') as app_file:
    app_file_str = str(app_file.read())

#from toddy.tools import date
import collections,os

#creating a list of options for the menu
list_options = ['about','exit']
from sysinfo import show_info_system as sis
#import psutil
import os,sys

sys.stderr = open(os.devnull, "w")
try:
  import psutil
finally:
  sys.stderr = sys.__stderr__

class SysInfo(MDApp):
   # def __init__(self):
    #    self.time = time.time
    def update_content(self,*args):
        self.root.ids.content.text = f"{os.popen('cat /proc/version').read()}"
        self.root.ids.bar.title = f"Sysinfo"
        #print(self.time())
        
    def build(self):
        self.time = ''
        Clock.schedule_interval(self.update_content, 1)
        self.ads = KivMob(TestIds.APP)
        self.ads.new_banner(TestIds.BANNER, top_pos=True)
        self.ads.request_banner()
        self.ads.show_banner()
        
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{i}",
                "height": dp(56),
                "on_release": lambda x=i: self.menu_callback(x),
             } for i in list_options
        ]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
        )
        content_back = 'memame'
        ## the new app_str
        
        return Builder.load_string(app_file_str)
   
   
    def test(self,button):
        self.menu.caller = button
        self.menu.open()
        print('testado')
        #Snackbar(text="Hello World").open()
        
        
    def menu_callback(self, text_item):
        self.menu.dismiss()
        if text_item=='about':
            Snackbar(text='Creator: ReynanBr\n@reysoft').open()
        
        

SysInfo().run()

