from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
Builder.load_file('ban.kv')
card_number = "nothing"

class LogIn(Screen):
    sound = SoundLoader.load('sound/keypress.mp3')
    text1 = StringProperty("    ")
    text2 = StringProperty("    ")
    text3 = StringProperty("    ")
    text4 = StringProperty("<--exit")
    text5 = StringProperty("    ")
    text6 = StringProperty("    ")
    text7 = StringProperty("    ")
    text8 = StringProperty("next-->")
    def on_button_1(self,widget):      
        self.play_audio()      
        print ("clicked 1")
    def on_button_2(self,widget):
        self.play_audio()      
        print ("clicked 2")
    def on_button_3(self,widget):
        self.play_audio()      
        print ("clicked 3")
    def on_button_4(self,widget):
        self.play_audio()      
        print ("clicked 4")
        App.get_running_app().stop()  
    def on_button_5(self,widget):
        self.play_audio()      
        print ("clicked 5")
    def on_button_6(self,widget):
        self.play_audio()      
        print ("clicked 6")
    def on_button_7(self,widget):
        self.play_audio()      
        print ("clicked 7")
    def on_button_8(self,widget):
        self.manager.current = 'mainmenu'
        self.play_audio()      
        print ("clicked 8")
    def play_audio(self):
        if self.sound:
            self.sound.play()    
class MainMenu(Screen):
    global card_number
    card_number 
    sound = SoundLoader.load('sound/keypress.mp3')
    text1 = StringProperty("    ")
    text2 = StringProperty("<--transfer")
    text3 = StringProperty("<--deposit")
    text4 = StringProperty("<--back")
    text5 = StringProperty("balance-->")
    text6 = StringProperty("transactions-->")
    text7 = StringProperty("withdraw-->")
    text8 = StringProperty("exit-->")
    def on_button_1(self,widget):      
        self.play_audio()      
        global card_number
         
        print ("clicked 1")
        print(card_number)
    def on_button_2(self,widget):
        self.play_audio()      
        print ("clicked 2")
    def on_button_3(self,widget):
        self.play_audio()      
        print ("clicked 3")
    def on_button_4(self,widget):
        self.manager.current = 'rootpage'
        self.play_audio()      
        print ("clicked 4")
    def on_button_5(self,widget):
        self.play_audio()      
        print ("clicked 5")
    def on_button_6(self,widget):
        self.play_audio()      
        print ("clicked 6")
    def on_button_7(self,widget):
        self.play_audio()      
        print ("clicked 7")
    def on_button_8(self,widget):
        self.play_audio()    
        App.get_running_app().stop()  
        print ("clicked 8")
    def play_audio(self):
        if self.sound:
            self.sound.play() 

class rootpage(Screen):
    sound = SoundLoader.load('sound/keypress.mp3')
    text1 = StringProperty("    ")
    text2 = StringProperty("    ")
    text3 = StringProperty("    ")
    text4 = StringProperty("<--no")
    text5 = StringProperty("    ")
    text6 = StringProperty("    ")
    text7 = StringProperty("    ")
    text8 = StringProperty("yes-->")
    def on_button_1(self,widget):      
        self.play_audio()      
        print ("clicked 1")
    def on_button_2(self,widget):
        self.play_audio()      
        print ("clicked 2")
    def on_button_3(self,widget):
        self.play_audio()      
        print ("clicked 3")
    def on_button_4(self,widget):
        self.play_audio()      
        self.manager.current = 'mainmenu'
        print ("clicked 4")
    def on_button_5(self,widget):
        self.play_audio()      
        print ("clicked 5")
    def on_button_6(self,widget):
        self.play_audio()      
        print ("clicked 6")
    def on_button_7(self,widget):
        self.play_audio()      
        print ("clicked 7")
    def on_button_8(self,widget):
        self.manager.current = 'card'
        self.play_audio()      
        print ("clicked 8")
    def play_audio(self):
        if self.sound:
            self.sound.play()     
class MainWidget(Screen):
    my_text = StringProperty("1")
    flag = False
    def on_enter(self):
        global card_number
        card_number = self.inp.text
        print(card_number)
        if self.flag and len(card_number)> 0:
            self.manager.current = 'login'
            self.flag = False
            return
        self.flag = True



class BankApp(App):
    def build(self):
        print("Building ui")
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(rootpage(name='rootpage'))
        sm.add_widget(LogIn(name='login'))
        sm.add_widget(MainWidget(name='card'))
        sm.add_widget(MainMenu(name='mainmenu'))

        return sm

state = "auth"
BankApp().run()