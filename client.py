#
#   CS361 Microservice: Client
#   Connects REQ socket to tcp://localhost:5555
#
# if zeromq not install, run command: pip install pyzmq
import zmq
import base64

context = zmq.Context()

#  Socket to talk to server
print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
number_of_messages = 0

#  Do 10 requests, waiting each time for a response
while number_of_messages < 1:
    print(f"Sending request …")
    socket.send(b'Requesting image')

    #  Get the reply.
    message = socket.recv()
    # message = base64.b64decode(message)
    fh = open('meme.png', 'wb')
    fh.write(base64.b64decode(message))
    fh.close()
    print(f"Received reply, meme saved to file")
    number_of_messages += 1