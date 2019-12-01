from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import pyaudio


HOST = input("Enter Host IP\n")
PORT = 4000
BufferSize = 4096
addresses = {}

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

def Connections():
    while True:
        try:
            client, addr = server.accept()
            print("{} is connected!!".format(addr))
            addresses[client] = addr
            Thread(target=ClientConnectionSound, args=(client,)).start()
        except:
            continue

def ClientConnectionSound(client):
    while True:
        try:
            data = client.recv(BufferSize)
            stream.write(data)
        except:
            continue

server = socket(family=AF_INET, type=SOCK_STREAM)
try:
    server.bind((HOST, PORT))
except OSError:
    print("Server Busy")

server.listen(2)
print("Waiting for connection..")
AcceptThread = Thread(target=Connections)
AcceptThread.start()
AcceptThread.join()
stream.stop_stream()
stream.close()
p.terminate()
