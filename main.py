from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
Builder.load_file('ban.kv')

class MainMenu(Screen):
    button_1 = ["",""]
    button_2 = ["   ","transfer"]
    button_3 =["    ","deposit"]
    button_4 = ["no","back"]
    button_5 = ["   ","balance"]
    button_6 = ["   ","list of transactions"]
    button_7 = ["   ","withdraw"]
    button_8 = ["yes","exit"]
    text1 = StringProperty("    ")
    text2 = StringProperty("transfer")
    text3 = StringProperty("deposit")
    text4 = StringProperty("back")
    text5 = StringProperty("balance")
    text6 = StringProperty("list of transactions")
    text7 = StringProperty("withdraw")
    text8 = StringProperty("exit")
    def on_button_1(self,widget):            
        print ("clicked 1")
    def on_button_2(self,widget):
        print ("clicked 2")
    def on_button_3(self,widget):
        print ("clicked 3")
    def on_button_4(self,widget):
        self.manager.current = 'rootpage'
        print ("clicked 4")
    def on_button_5(self,widget):
        print ("clicked 5")
    def on_button_6(self,widget):
        print ("clicked 6")
    def on_button_7(self,widget):
        print ("clicked 7")
    def on_button_8(self,widget):
        print ("clicked 8")

class rootpage(Screen):
    button_1 = ["",""]
    button_2 = ["   ","transfer"]
    button_3 =["    ","deposit"]
    button_4 = ["no","back"]
    button_5 = ["   ","balance"]
    button_6 = ["   ","list of transactions"]
    button_7 = ["   ","withdraw"]
    button_8 = ["yes","exit"]
    text1 = StringProperty("    ")
    text2 = StringProperty("    ")
    text3 = StringProperty("    ")
    text4 = StringProperty("no")
    text5 = StringProperty("    ")
    text6 = StringProperty("    ")
    text7 = StringProperty("    ")
    text8 = StringProperty("yes")
    def on_button_1(self,widget):            
        print ("clicked 1")
    def on_button_2(self,widget):
        print ("clicked 2")
    def on_button_3(self,widget):
        print ("clicked 3")
    def on_button_4(self,widget):
        self.manager.current = 'mainmenu'
        print ("clicked 4")
    def on_button_5(self,widget):
        print ("clicked 5")
    def on_button_6(self,widget):
        print ("clicked 6")
    def on_button_7(self,widget):
        print ("clicked 7")
    def on_button_8(self,widget):
        self.manager.current = 'mw'
        print ("clicked 8")
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
        sm.add_widget(MainMenu(name='mainmenu'))

        return sm

state = "auth"
BankApp().run()