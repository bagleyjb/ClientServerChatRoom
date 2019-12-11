from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import pyaudio
from array import array


HOST = input("Enter Host IP: ")
PORT = 4000
PORTAUDIO = 5000
BufferSize = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 100000
CHUNK = 1024

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
            
            
def SendAudio():
    while True:
        data = stream.read(CHUNK, exception_on_overflow = False)
        dataChunk = array('h', data)
        vol = max(dataChunk)
        '''
        if(vol > 500):
            print("Recording Sound...")
        else:
            print("Silence..")
        '''
        clientAudio.sendall(data)


def RecieveAudio():
    while True:
        data = recvall(BufferSize * 4)
        stream.write(data)


def recvall(size):
    databytes = b''
    while len(databytes) != size:
        to_read = size - len(databytes)
        if to_read > (4 * CHUNK):
            databytes += clientAudio.recv(4 * CHUNK)
        else:
            databytes += clientAudio.recv(to_read)
    return databytes

client = socket(family = AF_INET, type = SOCK_STREAM)
client.connect((HOST, PORT))

clientAudio = socket(family = AF_INET, type = SOCK_STREAM)
clientAudio.connect((HOST, PORTAUDIO))

audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,channels=CHANNELS, rate=RATE,
                    input=True,frames_per_buffer=CHUNK)

RecieveThread = Thread(target = recieveMessage).start();
SendThread = Thread(target = sendMessage).start();

RecieveAudioThread = Thread(target=RecieveAudio).start();
SendAudioThread = Thread(target=SendAudio).start();
#Audio






