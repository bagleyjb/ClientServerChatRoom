"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
/*-----------------------------------------------------/
Name: Zelalem Tenaw Terefe
Professor: Dr.Amos Johnson
Class: Artificial intelligence
Date: Nov 11, 2019
/-----------------------------------------------------*/
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 4000

addresses = {}
clients = {}

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
It waits for the clinet to connect
When clinet connects to the server it will print the
the client is connected and assignes the address of
the clinet in addresses based on the the socket(client)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def connectionsCheck():
    while True:
        client, addrOfClient = server.accept()
        print("{} is connected!!".format(addrOfClient))
        client.send(("Welcome to Chat Room. Type {quit} to exit. Enter your name: ").encode("utf-8"))
        addresses[client] = addrOfClient
        Thread(target = clientConnection, args=(client, )).start()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Accepts soicket(client) as an argument

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def clientConnection(client):
    name = client.recv(BufferSize).decode("utf-8")
    client.send(("Hello {}".format(name)).encode("utf-8"))
    message = ("{} has joined the chat..").format(name)
    broadcastMsg(message.encode("utf-8"))
    clients[client] = name
    while True:
        msg = client.recv(BufferSize).decode("utf-8")
        if msg != "quit":
            broadcastMsg(msg.encode("utf-8"), name + ": ")
        else:
            message = ("{} has left the chat.").format(clients[client])
            broadcastMsg(message.encode("utf-8"))
            client.send(("Will see you soon..").encode("utf-8"))
            del clients[client]
            break
            
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def broadcastMsg(msg, name = ""):
    for sockets in clients:
        sockets.send(name.encode("utf-8") + msg)

server = socket(family=AF_INET, type=SOCK_STREAM)
try:
    server.bind((HOST, PORT))
except OSError:
    print("Server Busy")
BufferSize = 1024

server.listen(5)
print("Waiting for Connections... ")
AcceptThread = Thread(target=connectionsCheck)
AcceptThread.start()
AcceptThread.join()
server.close()
