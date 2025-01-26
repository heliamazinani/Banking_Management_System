import os
import json

REQUEST_PIPE = "/tmp/core_request_pipe"
RESPONSE_PIPE = "/tmp/core_response_pipe"

def send_request(cardNumber, action, value=0):
    request = json.dumps([cardNumber, action, value])
    print("request is : ",request)
    with open(REQUEST_PIPE, "w") as req_pipe:
        req_pipe.write(request)

    with open(RESPONSE_PIPE, "r") as res_pipe:
        response = res_pipe.read().strip()
        print(f"Response: {response}")

if __name__ == "__main__":
    client_requests = [
        (1002, "showBalance", 0), (1003, "transfer#1004", 100),
        (1004, "transfer#1005", 100), (1007, "transfer#1008", 5),
        (1004, "transfer#1002", 100), (1004, "deposit", 110),
        (1002, "withdraw", 50), (1001, "withdraw", 10),
        (1005, "deposit", 190), (1003, "deposit", 5),
    ]
    # for req in client_requests:
    #     # print(req)
    #     send_request(req[0],req[1],req[2])
    send_request(1002,'showBalance',0)
    send_request(1003,'transfer#1004',100)
    send_request(1004,'transfer#1005',100)
    send_request(1007,'transfer#1008',5)
    send_request(1004,'transfer#1002',100)
    send_request(1004,'transfer#1002',100)
    
    
    
    # send_request(1005,'createAccount',190)
    # send_request(1004,'transfer#1002',100)
    # send_request(1004, "deposit", 110)
    # send_request(1002, "withdraw", 50)
    # send_request(1001, "withdraw", 10)
    # send_request(1002, "withdraw", 5)
    # send_request(1004, "withdraw", 500)
    # send_request(1003, "deposit", 5)
    # send_request(1004,'transfer#1002',100)
    # send_request(1004, "deposit", 110)
    # send_request(1002, "withdraw", 50)
    # send_request(1005, "withdraw", 10)
    # send_request(1002, "withdraw", 5)
    # send_request(1004, "withdraw", 500)
    # send_request(1005, "deposit", 5)
    # send_request(1005,'transfer#1002',100)
    # send_request(1004, "deposit", 110)
    # send_request(1002, "withdraw", 50)
    # send_request(1001, "withdraw", 10)
    # send_request(1002, "withdraw", 5)
    # send_request(1005, "withdraw", 500)
    # send_request(1003, "deposit", 5)
    with open(REQUEST_PIPE, "w") as req_pipe:
        req_pipe.write("exit")
