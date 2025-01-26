from core.simpleClient import *
def check_account(cardnumber):
    return True
def check_password(password):
    return True
def balence(cardnumber,password):
    return 0
def deposite(cardnumber,password,value):
    send_request(cardnumber,"deposit",value)
    return "success"
def withdraw(cardnumber,password,value):
    send_request(cardnumber,"withdraw",value)
    return "success"
def transfer(cardnumber,password,value,second_cardnumber):
    return True
def create_account(cardnumber,password):
    return True