import socket
from threading import Thread
import time 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip = '0.0.0.0'
port = 4441
s.bind((ip, port))
s.listen(5)

connected_clients=[]


def handle_client(c, addr):

    while True:
        try:
            if c:
                c.send('test'.encode())

        except:
            print('closing')
            if c:
                c.close()



while True:

    c, addr = s.accept()
    print('Connected:', addr)

    t = Thread(target=handle_client, args=(lambda:c, addr))
    t.setDaemon(True)
    t.start()

    
