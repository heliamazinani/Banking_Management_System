import os
import json
from multiprocessing import Process

REQUEST_PIPE = "/tmp/core_request_pipe"
RESPONSE_PIPE = "/tmp/core_response_pipe"

def send_request(cardNumber, action, value=0):
    """Send a request to the core and print the response."""
    request = json.dumps([cardNumber, action, value])
    print(f"Request: {request}")
    with open(REQUEST_PIPE, "w") as req_pipe:
        req_pipe.write(request)
    
    with open(RESPONSE_PIPE, "r") as res_pipe:
        response = res_pipe.read().strip()
        print(f"Response: {response}")

def test_client(requests):
    """Execute a sequence of requests as a single client."""
    for request in requests:
        send_request(*request)

if __name__ == "__main__":
    # Define the requests for each client process
    client_requests = [
        [(1002, "showBalance", 0), (1003, "transfer#1004", 100)],
        [(1004, "transfer#1005", 100), (1007, "transfer#1008", 5)],
        [(1004, "transfer#1002", 100), (1004, "deposit", 110)],
        [(1002, "withdraw", 50), (1001, "withdraw", 10)],
        [(1005, "deposit", 190), (1003, "deposit", 5)],
    ]

    # Create and start a process for each set of client requests
    processes = []
    for requests in client_requests:
        p = Process(target=test_client, args=(requests,))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    # Send an exit command to the core
    with open(REQUEST_PIPE, "w") as req_pipe:
        req_pipe.write("exit")
