import os
import json
import time
from multiprocessing import Process

REQUEST_PIPE = "/tmp/core_request_pipe"
RESPONSE_PIPE = "/tmp/core_response_pipe"

def send_request(cardNumber, action, value=0):
    """Send a real request to the core and get the response."""
    request = json.dumps([cardNumber, action, value])
    print(f"Request from {cardNumber} is: {request}")
    
    # Writing the request to the core
    with open(REQUEST_PIPE, "w") as req_pipe:
        req_pipe.write(request)
    
    # Reading the response from the core
    with open(RESPONSE_PIPE, "r") as res_pipe:
        response = res_pipe.read().strip()
        print(f"Response for {cardNumber}: {response}")

def client_process(client_id, num_requests):
    """Each client process will send `num_requests` to the core with real actions."""
    for i in range(num_requests):
        action = ""
        value = 0
        
        # Simulate different actions for each client
        if i % 3 == 0:
            action = f"transfer#{client_id+1}"  # Simulating a transfer action
            value = 100 + (i * 10)
        elif i % 3 == 1:
            action = "deposit"
            value = 50 + (i * 5)
        else:
            action = "withdraw"
            value = 30 + (i * 5)
        
        send_request(client_id, action, value)
        time.sleep(0.1)  # Simulate some delay between requests

def create_multiple_clients(num_clients, num_requests_per_client):
    """Create multiple client processes to simulate heavy load."""
    processes = []
    
    # Create `num_clients` processes, each sending `num_requests_per_client` requests
    for i in range(num_clients):
        p = Process(target=client_process, args=(i+1, num_requests_per_client))
        processes.append(p)
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()

if __name__ == "__main__":
    # Set the number of client processes and number of requests per client
    num_clients = 5  # Number of client processes
    num_requests_per_client = 10  # Number of requests each client sends

    # Start the heavy-light test with multiple clients sending real requests
    create_multiple_clients(num_clients, num_requests_per_client)
    
    # After all requests are sent, close the request pipe with "exit"
    with open(REQUEST_PIPE, "w") as req_pipe:
        req_pipe.write("exit")
