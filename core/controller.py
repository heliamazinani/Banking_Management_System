import json

def createAccount(cardNumber, initBalance):
    with open(f'core/accounts/{cardNumber}.json', "w") as acc:
        content = {"balance": initBalance} 
        json.dump(content, acc, indent=2)

def withdraw(cardNumber, value):
    with open(f'core/accounts/{cardNumber}.json', "r+") as acc:
        content = json.load(acc)
        if content["balance"] >= value:
            content["balance"] -= value
        else:
            print("Insufficient balance.")
        
        acc.seek(0)
        json.dump(content, acc, indent=2)
        acc.truncate() 
        
    return "1"

def deposite(cardNumber, value):
    with open(f'core/accounts/{cardNumber}.json', "r+") as acc:
        content = json.load(acc)
        content["balance"] += value
        
        acc.seek(0)
        json.dump(content, acc, indent=2)
        acc.truncate()  
        
    return "2"

def transfer(source, destination, value):
    withdraw(source, value)
    deposite(destination, value)

if __name__ == "__main__":
    # createAccount(1, 5)
    deposite(1, 2)
