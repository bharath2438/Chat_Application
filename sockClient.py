import socket
import threading

socketClient = socket.socket()

host = socket.gethostname()
port = 5000

socketClient.connect((host, port))

def send():
    while(True):
        data = input()
        socketClient.send(data.encode())

def receive():
    while(True):
        data = socketClient.recv(512).decode()
        print("=> ", data)

t1 = threading.Thread(target = send)
t2 = threading.Thread(target = receive)

t1.start()
t2.start()

t1.join()
t2.join()

    
