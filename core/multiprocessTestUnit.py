import os
import json
from multiprocessing import Process, Queue

REQUEST_PIPE = "/tmp/core_request_pipe"
RESPONSE_PIPE = "/tmp/core_response_pipe"

def send_request(request_queue, response_queue, cardNumber, action, value=0):
    """Send a request to the core and print the response."""
    request = json.dumps([cardNumber, action, value])
    print(f"Request: {request}")
    
    request_queue.put(request)
    
    response = response_queue.get()
    print(f"Response: {response}")

def test_client(requests, request_queue, response_queue):
    """Execute a sequence of requests as a single client."""
    for request in requests:
        send_request(request_queue, response_queue, *request)

def core_process(request_queue, response_queue):
    """Simulate the core process that handles requests from clients."""
    while True:
        request_data = request_queue.get()
        if request_data == "exit":
            print("Shutting down core process.")
            break
        
        print(f"Core received request: {request_data}")

        response = f"Processed: {request_data}"
        response_queue.put(response)

if __name__ == "__main__":

    request_queue = Queue()
    response_queue = Queue()

    core_p = Process(target=core_process, args=(request_queue, response_queue))
    core_p.start()

    client_requests = [
        [(1002, "showBalance", 0), (1003, "transfer#1004", 100)],
        [(1004, "transfer#1005", 100), (1007, "transfer#1008", 5)],
        [(1004, "transfer#1002", 100), (1004, "deposit", 110)],
        [(1002, "withdraw", 50), (1001, "withdraw", 10)],
        [(1005, "deposit", 190), (1003, "deposit", 5)],
    ]

    processes = []
    for requests in client_requests:
        p = Process(target=test_client, args=(requests, request_queue, response_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    request_queue.put("exit")

    core_p.join()
