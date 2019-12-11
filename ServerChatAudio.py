from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import pyaudio

HOST = "127.0.0.1"
PORTCHAT = 4000
PORTAUDIO = 5000
BufferSize = 1024

addresses = {}
clients = {}
addressesAudio = {}
CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 100000
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
It waits for the clinet to connect
When clinet connects to the server it will print the
the client is connected and assignes the address of
the clinet in addresses based on the the socket(client)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def connectionsCheck():
    while True:
        client, addrOfClient = serverChat.accept()
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

def broadcastMsg(msg, name = ""):
    for sockets in clients:
        sockets.send(name.encode("utf-8") + msg)


def Connections():
    while True:
        try:
            clientAudio, addr = serverAudio.accept()
            print("{} is connected!!".format(addr))
            addresses[clientAudio] = addr
            Thread(target=ClientConnectionSound, args=(clientAudio,)).start()
        except:
            continue

def ClientConnectionSound(clientAudio):
    while True:
        try:
            data = clientAudio.recv(BufferSize * 4)
            stream.write(data)
        except:
            continue

serverChat = socket(family=AF_INET, type=SOCK_STREAM)
serverAudio = socket(family=AF_INET, type=SOCK_STREAM)
try:
    serverChat.bind((HOST, PORTCHAT))
except OSError:
    print("Server Busy")
try:
    serverAudio.bind((HOST, PORTAUDIO))
except OSError:
    print("Server Busy")

    
serverAudio.listen(2)
AcceptThreadAudio = Thread(target=Connections)
AcceptThreadAudio.start()

serverChat.listen(2)
print("Waiting for Connections... ")
AcceptThreadChat = Thread(target=connectionsCheck)
AcceptThreadChat.start()
AcceptThreadChat.join()
serverChat.close()


'''
stream.stop_stream()
stream.close()
p.terminate()
'''











