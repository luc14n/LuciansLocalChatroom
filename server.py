import socket
import threading

# List to keep track of connected clients
clients = []

def broadcast(message, sender_socket):
    print(f"Broadcasting: {message}")  # Debugging statement
    try:
        print("Trying to send")  # Debugging statement
        sender_socket.send(message.encode())
    except Exception as e:
        print(f"Failed to send message to client: {e}")

    #for client_socket in clients:
    #    if client_socket != sender_socket:


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
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.chat_window.display_message(f"Connected to {client_address}")
            clients.append(client_socket)  # Add the new client to the list

            # Inside the server's main loop
            while True:
                try:
                    message = client_socket.recv(1024).decode()
                    if not message:
                        break  # Break the loop if no message is received (connection closed)
                    print(f"Received message: {message}")  # Debugging statement
                    self.chat_window.display_message(f"Client {client_address}: {message}")
                    #broadcast(message, client_socket)  # Broadcast the message to all connected clients
                except Exception as e:
                    print(f"Error receiving message: {e}")
                    break

def send_message_to_client(message, client_socket):
    try:
        client_socket.send(message.encode())
    except Exception as e:
        print(f"Failed to send message to client: {e}")

def server_thread(host, port, chat_window):
    server = ChatServer(host, port, chat_window)
    server.start()
