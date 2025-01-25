import os
import json
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

REQUEST_PIPE = "/tmp/core_request_pipe"
RESPONSE_PIPE = "/tmp/core_response_pipe"

file_locks = defaultdict(threading.Lock)

def logfunc(log_entry,log_path):
    if not os.path.exists(log_path): 
        with open(log_path, "w") as log_file:
            log_file.write(log_entry)
            log_file.close()
    else:  
        with open(log_path, "a") as log_file:
            log_file.write(log_entry)
            log_file.close()
    
def createAccount(cardNumber, initBalance):
    print("dhgkhrkd")
    file_path = f'core/accounts/{cardNumber}.json'
    log_path = f'core/logs/{cardNumber}.txt'

    if os.path.exists(file_path):
        return f"Account with card number {cardNumber} already exists."

    try:
        with open(file_path, "w") as acc:
            content = {"balance": initBalance}
            json.dump(content, acc, indent=4)
        logfunc(f"account {cardNumber} created w balance{initBalance}",log_path=log_path)
        return f"Account with card number {cardNumber} successfully created with balance {initBalance}."
    except Exception as e:
        return f"Error creating account: {str(e)}"
    
def withdraw(cardNumber, value):
    file_path = f'core/accounts/{cardNumber}.json'
    lock = file_locks[file_path] 

    with lock:
        try:
            with open(file_path, "r+") as acc:
                content = json.load(acc)
                if content["balance"] >= value:
                    content["balance"] -= value
                    acc.seek(0)
                    json.dump(content, acc, indent=4)
                    acc.truncate()
                    return f"Withdrawn {value}, New Balance: {content['balance']}"
                else:
                    return "Insufficient balance."
        except FileNotFoundError:
            return "Account not found."

def deposite(cardNumber, value):
    file_path = f'core/accounts/{cardNumber}.json'
    lock = file_locks[file_path]

    with lock:
        try:
            with open(file_path, "r+") as acc:
                content = json.load(acc)
                content["balance"] += value
                acc.seek(0)
                json.dump(content, acc, indent=4)
                acc.truncate()
                return f"Deposited {value}, New Balance: {content['balance']}"
        except FileNotFoundError:
            return "Account not found."

def process_request(request):
    try:
        cardNumber, action, value = request
        if action == "deposit":
            return deposite(cardNumber, value)
        elif action == "withdraw":
            return withdraw(cardNumber, value)
        else:
            return "Invalid action"
    except ValueError:
        return "Invalid request format"

def handle_client(request_data):
    try:
        request = json.loads(request_data)
        response = process_request(request)
    except json.JSONDecodeError:
        response = "Invalid JSON request"

    with open(RESPONSE_PIPE, "w") as res_pipe:
        res_pipe.write(response)

if __name__ == "__main__":
    if os.path.exists(REQUEST_PIPE):
        os.remove(REQUEST_PIPE)
    if os.path.exists(RESPONSE_PIPE):
        os.remove(RESPONSE_PIPE)

    os.mkfifo(REQUEST_PIPE)
    os.mkfifo(RESPONSE_PIPE)

    print("Core process is running...")

    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            with open(REQUEST_PIPE, "r") as req_pipe:
                request_data = req_pipe.read().strip()
                if request_data == "exit":
                    print("Shutting down core process.")
                    break

            executor.submit(handle_client, request_data)
