import os
import json

REQUEST_PIPE = "/tmp/core_request_pipe"
RESPONSE_PIPE = "/tmp/core_response_pipe"

def send_request(cardNumber, action, value=0):
    request = json.dumps([cardNumber, action, value])

    with open(REQUEST_PIPE, "w") as req_pipe:
        req_pipe.write(request)

    with open(RESPONSE_PIPE, "r") as res_pipe:
        response = res_pipe.read().strip()
        print(f"Response: {response}")

if __name__ == "__main__":
    # send_request(1001, "deposit", 2)
    # send_request(1001, "withdraw", 3)
    # send_request(1001, "withdraw", 10)
    # send_request(1002, "withdraw", 5)
    # send_request(1003, "deposit", 5)
    send_request
    with open(REQUEST_PIPE, "w") as req_pipe:
        req_pipe.write("exit")
