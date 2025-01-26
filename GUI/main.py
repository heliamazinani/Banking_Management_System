from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from controller import *
from kivy.animation import Animation

Builder.load_file('ban.kv')
card_number = "nothing"
Password = "nothing"
second_card_nummber = "nothing"
value = "0"
class CreateAccount(Screen):
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
        if create_account(card_number,Password):
            self.manager.current = 'mainmenu'
        self.play_audio()      
        print ("clicked 8")
    def play_audio(self):
        if self.sound:
            self.sound.play()  
    def on_enter(self):
        global Password
        Password = self.cn.text  
        global card_number
        card_number = self.inp.text


class Deposite(Screen):
    sound = SoundLoader.load('sound/keypress.mp3')
    text1 = StringProperty("    ")
    text2 = StringProperty("    ")
    text3 = StringProperty("    ")
    text4 = StringProperty("<--back")
    text5 = StringProperty("    ")
    text6 = StringProperty("    ")
    text7 = StringProperty("next-->")
    text8 = StringProperty("exit-->")
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
        self.manager.current = 'mainmenu'      

    def on_button_5(self,widget):
        self.play_audio()      
        print ("clicked 5")
    def on_button_6(self,widget):
        self.play_audio()      
        print ("clicked 6")
    def on_button_7(self,widget):
        self.play_audio()      
        print ("clicked 7")
        if deposite(card_number,Password,value):
            print("yippe")
            self.manager.current = 'mainmenu'

    def on_button_8(self,widget):
        self.play_audio()      
        print ("clicked 8")
        App.get_running_app().stop()  
    def play_audio(self):
        if self.sound:
            self.sound.play()  
    def on_enter(self):
        global value
        value = self.v.text
class Withdraw(Screen):
    sound = SoundLoader.load('sound/keypress.mp3')
    text1 = StringProperty("    ")
    text2 = StringProperty("    ")
    text3 = StringProperty("    ")
    text4 = StringProperty("<--back")
    text5 = StringProperty("    ")
    text6 = StringProperty("    ")
    text7 = StringProperty("next-->")
    text8 = StringProperty("exit-->")
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
        self.manager.current = 'mainmenu'      

    def on_button_5(self,widget):
        self.play_audio()      
        print ("clicked 5")
    def on_button_6(self,widget):
        self.play_audio()      
        print ("clicked 6")
    def on_button_7(self,widget):
        self.play_audio()      
        print ("clicked 7")
        if withdraw(card_number,Password,value):
            print("yippe")
            self.manager.current = 'mainmenu'

    def on_button_8(self,widget):
        self.play_audio()      
        print ("clicked 8")
        App.get_running_app().stop()  
    def play_audio(self):
        if self.sound:
            self.sound.play()  
    def on_enter(self):
        global value
        value = self.v.text
class Transfer(Screen):
    sound = SoundLoader.load('sound/keypress.mp3')
    text1 = StringProperty("    ")
    text2 = StringProperty("    ")
    text3 = StringProperty("    ")
    text4 = StringProperty("<--back")
    text5 = StringProperty("    ")
    text6 = StringProperty("    ")
    text7 = StringProperty("next-->")
    text8 = StringProperty("exit-->")
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
        self.manager.current = 'mainmenu'      

    def on_button_5(self,widget):
        self.play_audio()      
        print ("clicked 5")
    def on_button_6(self,widget):
        self.play_audio()      
        print ("clicked 6")
    def on_button_7(self,widget):
        self.play_audio()      
        print ("clicked 7")
        if transfer(card_number,Password,value,second_card_nummber):
            print("yippe")
            self.manager.current = 'mainmenu'

    def on_button_8(self,widget):
        self.play_audio()      
        print ("clicked 8")
        App.get_running_app().stop()  
    def play_audio(self):
        if self.sound:
            self.sound.play()  
    def on_enter(self):
        global second_card_nummber
        second_card_nummber = self.inp.text  
        global value
        value = self.v.text

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
        if check_password(Password):
            self.manager.current = 'mainmenu'
        self.play_audio()      
        print ("clicked 8")
    def play_audio(self):
        if self.sound:
            self.sound.play()  
    def on_enter(self):
        global Password
        Password = self.inp.text  


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
        self.manager.current = 'transfer'
    def on_button_3(self,widget):
        self.play_audio()      
        print ("clicked 3")
        self.manager.current = 'deposite'
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
        self.manager.current = 'wd'
    def on_button_8(self,widget):
        self.play_audio()    
        App.get_running_app().stop()  
        print ("clicked 8")
    def play_audio(self):
        if self.sound:
            self.sound.play() 

class firstpage(Screen):
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
        self.manager.current = 'create'
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
    def animate(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &amp;= is in parallel
        animation = Animation(pos =(100, 100), t ='out_bounce')
        animation += Animation(pos =(200, 100), t ='out_bounce')
        animation += Animation(size =(100, 50))

        # apply the animation on the button, passed in the &quot;instance&quot; argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
        animation.start(instance)   
class Card(Screen):
    flag = False

    def on_enter(self):
        global card_number
        card_number = self.inp.text
        print(card_number)
        if self.flag and len(card_number)> 0 and check_account(card_number):
            self.manager.current = 'login'
            self.flag = False
            return
        if self.flag and not check_account(card_number) and len(card_number)> 0 :
            print("wrong cardnumber")

        self.flag = True



class BankApp(App):
    def build(self):
        print("Building ui")
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(firstpage(name='rootpage'))
        sm.add_widget(LogIn(name='login'))
        sm.add_widget(Card(name='card'))
        sm.add_widget(MainMenu(name='mainmenu'))
        sm.add_widget(Transfer(name='transfer'))
        sm.add_widget(Deposite(name='deposite'))
        sm.add_widget(Withdraw(name='wd'))
        sm.add_widget(CreateAccount(name='create'))
        return sm

state = "auth"
BankApp().run()