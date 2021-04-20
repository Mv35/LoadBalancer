import os


class Server():

    def __init__(self, port):

        self.number_of_connections = 0
        self.port = port

    def update_number_of_connections(self):
        connections = os.popen("netstat -an | grep -c {}".format(self.port)).read()
        self.number_of_connections = int(connections)//2