import concurrent
import socket
from threading import Thread

# List to keep track of connected clients
clients = []
clientAddress = []

def broadcast(message, sender_socket):
    print(f"Broadcasting: {message}")  # Debugging statement
    try:
        print(f"Trying to send to: {sender_socket}")  # Debugging statement
        sender_socket.send(message.encode())
        print("Success")
    except Exception as e:
        print(f"Failed to send message to client: {e}")

def sendToConnectedClients(message, user):
    for userID in clients:
        if userID != user:
            broadcast(message, userID)

class ChatServer:
    global global_socket

    def __init__(self, host, port, chat_window):
        self.host = host
        self.port = port
        self.chat_window = chat_window
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

    def start(self):
        self.chat_window.display_message("Server is now listening for connections.")

        connection_thread = Thread(target=self.seeNewConnections)
        read_connection_thread = Thread(target=self.readConnections)

        connection_thread.daemon = True
        read_connection_thread.daemon = True

        connection_thread.start()
        read_connection_thread.start()

            # Inside the server's main loop

    def seeNewConnections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.chat_window.display_message(f"Connected to {client_address}")
            clients.append(client_socket)  # Add the new client to the list
            clientAddress.append(client_address)


    def readConnections(self):
        print(2)
        while True:
            for userID in clients:
                try:
                    print(1)
                    message = userID.recv(1024).decode()
                    if not message:
                        break  # Break the loop if no message is received (connection closed)
                    print(f"Received message: {message}")  # Debugging statement
                    self.chat_window.display_message(f"Client {userID}: {message}")
                    sendToConnectedClients(message, userID)
                except Exception as e:
                    print(f"Error receiving message: {e}")
                    break

def server_thread(host, port, chat_window):
    server = ChatServer(host, port, chat_window)
    server.start()

#Merge Issues