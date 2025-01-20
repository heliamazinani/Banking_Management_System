from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
Builder.load_file('ban.kv')

class PageLayoutex(PageLayout):
    pass

class rootpage(Screen):
    def on_button(self):
        print ("clicked")



class MainWidget(Screen):
    my_text = StringProperty("1")
    text_input = StringProperty("enter")
    def on_toggle(self,tg):
        print(tg.state)
        if  tg.state == "normal" :
            tg.text = "on"
        else:
            tg.text = "off"

    def on_button(self):
        print ("clicked")
        self.count +=1
        self.my_text = str(self.count)
    def on_text(self,widget):
        self.text_input = widget.text

    

class BankApp(App):
    def build(self):
        print("Building ui")
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(rootpage(name='rootpage'))
        sm.add_widget(MainWidget(name='mw'))

        return sm


BankApp().run()