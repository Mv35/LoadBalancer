import webbrowser
import socket
import random
import requests 
import sys
from server import Server
import os
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 4440    # Port to listen on (non-privileged ports are > 1023)
SERVERS_PORTS = [4441,4442,4443,4444,4445,4446,4447]
SERVERS = []


# class loadBalancer():

#     def __init__(self):
#         pass
def run():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(10)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #for this simulation I'll assume that the hostname will be localhost for all server
    #different configurations can be easly implemented if needed that can allow different hostnames
    #per server

    #for robin round algo
    #SERVERS = [8867,8868, 8869]

    #for least_number_of_connections we need a server class with .number_of_connection attribute
    #then:
    
    for port in SERVERS_PORTS:
        SERVERS.append(Server(port))


    #n = -1 
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        
        print(request)
        #for lnc algo we need to have in the reques an identifier of the
        #robin round algo
        #n += 1
        #server = SERVERS[n % len(SERVERS_PORTS)]
        #least number of connection algorithm:

        for server in SERVERS:

            print('server port', server.port)
            server.update_number_of_connections()

            print('number of connections', server.number_of_connections)


        server = min(SERVERS, key=(lambda x: x.number_of_connections))

        # once we have the server:
        print("Sending connection to: " + str(server.port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_address = ('0.0.0.0', server.port)

        print(server.port, server.number_of_connections)
        sock.connect(server_address)
        #tm = sock.recv(1024)
        # print(tm)

        sock.sendall("request from balancer".encode())

        sock.close()

        client_connection.sendall('response from balancer'.encode())
        client_connection.close()

run()
# if __name__ == "__main__":
#     loadBalancer = loadBalancer()
#     loadBalancer.run()