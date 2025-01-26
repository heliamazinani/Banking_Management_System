import json
import os
import time
REQUEST_PIPE = "/tmp/core_request_pipe"
RESPONSE_PIPE = "/tmp/core_response_pipe"
def check_account(cardnumber):
    return True
def check_password(password):
    return True
def balence(cardnumber,password):
    return 0
def deposite(cardnumber,password,value):
    return send_request(cardnumber,"deposit",value)
     
def withdraw(cardnumber,password,value):
    return send_request(cardnumber,"withdraw",value)
    
def transfer(cardnumber,password,value,second_cardnumber):
    return send_request(cardnumber,f"transfer#{second_cardnumber}",value)
def create_account(cardnumber,password):
    return send_request(cardnumber,"createAccount",10)

def get_balance(cardnumber):
    return send_request(cardnumber,"showBalance",0)
def transaction(cardnumber):
    return send_request(cardnumber,"transactions",0)
def send_request(cardNumber, action, value=0):
    """Send a real request to the core and get the response."""
    request = json.dumps([cardNumber, action, value])
    print(f"Request from {cardNumber} is: {request}")
    res = "null"
    flag = True
    
    # Writing the request to the core
    with open(REQUEST_PIPE, "w") as req_pipe:
        req_pipe.write(request)
    # time.sleep(1)
    # Reading the response from the core
    with open(RESPONSE_PIPE, "r") as res_pipe:
        response = res_pipe.read().strip()
        print(f"Response for {cardNumber}: {response}")
        res = response
        if response.startswith("E"):
            flag = False
    if action == "showBalance" or action == "transactions":
        return res
    return flag