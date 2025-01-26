import os
import json
import threading
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import time

REQUEST_PIPE = "/tmp/core_request_pipe"
RESPONSE_PIPE = "/tmp/core_response_pipe"

file_locks = defaultdict(threading.Lock)
log_file_lock = threading.Lock

def logfunc(log_entry, log_path):
    print(log_entry)
    log_entry = str(log_entry) + '\n'
    
    try:
        if not os.path.exists(log_path):
            with open(log_path, "w") as log_file:
                log_file.write(log_entry)
        else:
            with open(log_path, "a") as log_file:
                log_file.write(log_entry)
    except Exception as e:
        print(f"An error occurred while writing to the log file: {e}")

    
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
        logfunc(f"account {cardNumber} created w balance {initBalance}",log_path=log_path)
        return f"Account with card number {cardNumber} successfully created with balance {initBalance}."
    except Exception as e:
        print("error")
        return f"Error creating account: {str(e)}"
    

def showBalance(cardNumber):
    file_path = f'core/accounts/{cardNumber}.json'
    lock = file_locks[file_path]
    log_path = f'core/logs/{cardNumber}.txt'

    
    lock.acquire(timeout=2)
    try:
        with open(file_path,"r") as acc:
            content = json.load(acc)
               
            logfunc(f"account {cardNumber} checked balance ",log_path=log_path)
            return 1000
            

    except FileNotFoundError:
        return "Account Not Found !"
    finally:
        lock.release()
    

def transfer(source, destination, value, retries=3, timeout=10):
    source_file_path = f'core/accounts/{source}.json'
    destination_file_path = f'core/accounts/{destination}.json'
    source_lock = file_locks[source_file_path]
    destination_lock = file_locks[destination_file_path]
    log_path = f'core/logs/{source}.txt'

    start_time = time.time()  # Record the start time
    
    for _ in range(retries):
        # Check elapsed time
        elapsed_time = time.time() - start_time
        if elapsed_time >= timeout:
            return f"Transfer aborted due to timeout of {timeout} seconds."

        # Try to acquire both locks
        acquired_source = source_lock.acquire(blocking=False)
        acquired_destination = destination_lock.acquire(blocking=False)

        if acquired_source and acquired_destination:
            try:
                # Perform transfer
                with open(source_file_path, "r+") as src_file, open(destination_file_path, "r+") as dest_file:
                    # Read source and destination accounts
                    src_content = json.load(src_file)
                    dest_content = json.load(dest_file)

                    # Check for sufficient balance
                    if src_content["balance"] >= value:
                        src_content["balance"] -= value
                        dest_content["balance"] += value

                        # Write updated balances
                        src_file.seek(0)
                        json.dump(src_content, src_file, indent=4)
                        src_file.truncate()

                        dest_file.seek(0)
                        json.dump(dest_content, dest_file, indent=4)
                        dest_file.truncate()
                        logfunc(f"account {source} transfered {value} to {destination}",log_path=log_path)
                        log_path = f'core/logs/{destination}.txt'
                        logfunc(f"account {destination} was transfered {value} ",log_path=log_path)
                        return f"Transferred {value} from {source} to {destination}."
                    else:
                        return "Insufficient balance in the source account."
            except FileNotFoundError as e:
                return f"Error: {e}"
            finally:
                # Release both locks
                source_lock.release()
                destination_lock.release()
        else:
            # Release any lock that was acquired if both couldn't be acquired
            if acquired_source:
                source_lock.release()
            if acquired_destination:
                destination_lock.release()

            # Retry after a short delay or on the next iteration
            time.sleep(0.5)  # Optional: adding a delay between retries
    
    return "Could not acquire both locks after multiple attempts, transfer aborted."
    

def withdraw(cardNumber, value):
    file_path = f'core/accounts/{cardNumber}.json'
    lock = file_locks[file_path] 
    log_path = f'core/logs/{cardNumber}.txt'

    lock.acquire(timeout=2)
    try:
        with open(file_path, "r+") as acc:
            content = json.load(acc)
            if content["balance"] >= value:
                content["balance"] -= value
                acc.seek(0)
                json.dump(content, acc, indent=4)
                acc.truncate()
                logfunc(f"Withdrawn {value}, New Balance: {content['balance']}",log_path=log_path)
                return f"Withdrawn {value}, New Balance: {content['balance']}"
            else:
                return "Insufficient balance."
    except FileNotFoundError:
        return "Account not found."
    finally:
        lock.release()

def deposite(cardNumber, value):
    file_path = f'core/accounts/{cardNumber}.json'
    lock = file_locks[file_path]
    log_path = f'core/logs/{cardNumber}.txt'

    lock.acquire(timeout=2)
    print('1')
    try:
        with open(file_path, "r+") as acc:
            print('2')
            
            content = json.load(acc)
            # print('3')
            print(content)
            content["balance"] += value
            
            # print('4')
            acc.seek(0)
            
            # print('5')
            json.dump(content, acc, indent=4)
            # print('6')
            
            acc.truncate()
            
            # print('7')
            logfunc(f"Deposited {value}, New Balance: {content['balance']}",log_path=log_path)
            print("deposited")
            return f"Deposited {value}, New Balance: {content['balance']}"
    except FileNotFoundError:
        print("not found")
        return "Account not found."
    finally:
        lock.release()

def process_request(request):
    try:
        cardNumber, action, value = request
        if action == "deposit":
            print(f'inside loggggg {cardNumber} {action} {value}')
            return deposite(cardNumber, value)
        elif action == "withdraw":
            return withdraw(cardNumber, value)
        elif action == "createAccount":
            return createAccount(cardNumber, value)
        elif action.split('#')[0] == "transfer":
            return transfer(cardNumber,action.split('#')[1], value)
        elif action == "showBalance":
            return showBalance(cardNumber)
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
