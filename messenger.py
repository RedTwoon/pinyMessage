"""
As basic of a CLI messenger as I could create.

Uses select and socket module and allows server and
client to send and receive messages to each other
until one sends 'quit'
"""

import socket
import select
import threading

SERVER = True
PORT = 6666
BUFFER = 1024  # Should be exponent of 2 for some reason ??

class Server:
    """
    Creates a Server which waits for connection from Client

    Server can send and receive messages from Client
    """

    def __init__(self):
        self.thread = None
        self.recipient = None
        self.running = True
        self.socket = self.make_socket()

    def make_socket(self):
        """Returns a bound and listening socket"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('', PORT))
        sock.listen(1)
        return sock

    def check_quit(self, message):
        """Ends program if message == 'quit'"""
        if message == 'quit':
            try:
                self.recipient.send(b'quit')
            except:
                pass
            self.socket.close()
            self.running = False
            print('Disconnected.')
            return True

    def send_message(self):
        """Sends input message to Client"""
        message = str.encode(input(' >> '))
        if self.running:
            self.recipient.send(message)
            self.send_message()

    def main_loop(self):
        """
        Wait for connection and start Thread for pinyMessage
        Read incoming messages until told not to
        """
        readers, writers, error = select.select([self.socket], [], [])
        for sock in readers:
            if sock == self.socket:
                self.recipient, address = self.socket.accept()
                if not self.thread:
                    self.thread = threading.Thread(target=self.send_message)
                    self.thread.start()
            while self.running:
                data = self.recipient.recv(BUFFER)
                if data:
                    if not self.check_quit(data.decode()):
                        print(' << ', data.decode())


class Client:
    """
    Creates a Client which connects to Server

    If connection made, Client and Server can send and receive messages.
    """

    def __init__(self):
        self.thread = None
        self.running = True
        self.host = self.get_host()
        self.socket = self.connect_to_server()

    def get_host(self):
        """User types server IP, or blank for 'localhost'"""
        print("'Type the server's IP / hostname, or press ENTER to use 'localhost'")
        host = input(' -> ')
        if host:
            return host
        else:
            return 'localhost'

    def connect_to_server(self):
        """Forms connection with server"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, PORT))
        print('Connected to server.')
        return sock

    def check_quit(self, message):
        """Ends program if message == 'quit'"""
        if message.lower() == 'quit':
            try:
                self.socket.send(b'quit')
            except:
                pass
            self.socket.close()
            self.running = False
            print('Disconnected.')
            return True

    def send_message(self):
        """Sends input message to server"""
        message = input(' >> ')
        if self.running:
            self.socket.send(str.encode(message))
            self.send_message()

    def main_loop(self):
        """Start a Thread for pinyMessage, read incoming messages"""
        self.socket.send(str.encode('Client has connected'))
        self.thread = threading.Thread(target=self.send_message)
        self.thread.start()
        while self.running:
            try:
                data = self.socket.recv(BUFFER)
                if data:
                    if not self.check_quit(data.decode()):
                        print(' << ', data.decode())
            except:
                pass


if __name__ == '__main__':
    import sys
    x = sys.argv
    if len(x) == 1:  # No extra argument on Terminal creates server
        sock = Server()
    else:  # Any extra argument on Terminal creates client, ex: 'python3 pinyMessage.py client'
        sock = Client()
    sock.main_loop()
    print('Press ENTER to quit')