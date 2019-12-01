"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name: Zelalem Tenaw Terefe
Professor: Dr.Amos Johnson
Class: Artificial intelligence
Date: Nov 11, 2019
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

HOST = input("Enter Host IP: ")
PORT = eval(input("Enter Port No: "))
BufferSize = 1024

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Recieves a message form the client and prints the
message
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def recieveMessage():
    while True:
        try:
            inputMsg = client.recv(BufferSize).decode("utf-8")
            print(inputMsg)
        except OSError:
            break
            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Takes the client message which is string from StandardInput
If the string is quit it sends the message and closes
the clinet connection
Else it will just send the message
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def sendMessage():
    while True:
        inputMsg = input()
        if inputMsg == "quit":
            client.send(inputMsg.encode("utf-8"))
            client.close()
            break
        else:
            client.send(inputMsg.encode("utf-8"))

client = socket(family = AF_INET, type = SOCK_STREAM)
client.connect((HOST, PORT))

RecieveThread = Thread(target = recieveMessage).start()
SendThread = Thread(target = sendMessage).start()
