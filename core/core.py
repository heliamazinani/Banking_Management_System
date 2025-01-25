import os
import json
import threading
from collections import defaultdict
import time

REQUEST_PIPE = "/tmp/core_request_pipe"
RESPONSE_PIPE = "/tmp/core_response_pipe"

file_locks = defaultdict(threading.Lock)

def createAccount(cardNumber, initBalance):
    with open(f'core/accounts/{cardNumber}.json', "w") as acc:
        content = {"balance": initBalance}
        json.dump(content, acc, indent=4)


def showBalance(cardNumber):
    file_path = f'core/accounts/{cardNumber}.json'
    lock = file_locks[file_path]
    
    lock.acquire(timeout=2)
    try:
        with open(file_path,"r") as acc:
            content = json.load(acc)
            return f"Balance is : {content['balance']}"
    except FileNotFoundError:
        return "Account Not Found !"
    finally:
        lock.release()
    

def transfer(source, destination, value, retries=3, timeout=10):
    source_file_path = f'core/accounts/{source}.json'
    destination_file_path = f'core/accounts/{destination}.json'
    source_lock = file_locks[source_file_path]
    destination_lock = file_locks[destination_file_path]

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

    lock.acquire(timeout=2)
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
    finally:
        lock.release()

def deposite(cardNumber, value):
    file_path = f'core/accounts/{cardNumber}.json'
    lock = file_locks[file_path]

    lock.acquire(timeout=2)

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
    finally:
        lock.release()

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
    if not os.path.exists(REQUEST_PIPE):
        os.mkfifo(REQUEST_PIPE)
    if not os.path.exists(RESPONSE_PIPE):
        os.mkfifo(RESPONSE_PIPE)

    print("Core process is running...")

    while True:
        with open(REQUEST_PIPE, "r") as req_pipe:
            request_data = req_pipe.read().strip()
            if request_data == "exit":
                print("Shutting down core process.")
                break

        thread = threading.Thread(target=handle_client, args=(request_data,))
        thread.start()
