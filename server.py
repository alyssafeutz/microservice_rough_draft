
#
#   CS361 server in Python
#   Binds REP socket to tcp://*:5555
#

import time
import zmq
import base64
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
number_of_messages = 0
num = random.randint(1, 9)
with open(f"{num}.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    print("copied")
# f = open("pic.bin", "wb")
# f.write(my_string)
# f.close


while number_of_messages < 1:
    #  Wait for next request from client
    message = socket.recv()
    message = message.decode('utf8')
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(my_string)
    number_of_messages += 1