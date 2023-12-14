import socket
from threading import Thread
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# List to keep track of connected clients
clients = []
clientAddress = []

# Keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

with open('private_key.pem', 'wb') as f:
    f.write(pem)

pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('public_key.pem', 'wb') as f:
    f.write(pem)


# User keys
userKeys = {}

def broadcast(message, socket):
    print(f"Broadcasting")  # Debugging statement
    try:
        print(f"Trying to send to: {socket}")  # Debugging statement
        fernet = Fernet(userKeys[socket])
        encryptedmessage = fernet.encrypt(message)
        socket.send(encryptedmessage)
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
        self.server_socket.listen(5)

    def start(self):
        self.chat_window.display_message("Server is now listening for connections.")

        connection_thread = Thread(target=self.seeNewConnections)
        connection_thread.daemon = True
        connection_thread.start()

            # Inside the server's main loop

    def seeNewConnections(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            self.chat_window.display_message(f"Connected to {client_address}")
            print(f"Connected to {client_address}")
            print(public_key)

            public_key_bytes = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

            client_socket.send(public_key_bytes)
            print(public_key_bytes.decode())

            encryptedClientKey = client_socket.recv(1024)
            print(encryptedClientKey)

            clientKey = private_key.decrypt(
                encryptedClientKey,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            print(clientKey)

            userKeys[client_socket] = clientKey
            clients.append(client_socket)  # Add the new client to the list
            clientAddress.append(client_address)

            read_connection_thread = Thread(target=lambda: self.readConnections(client_socket, clientKey))

            read_connection_thread.daemon = True
            read_connection_thread.start()

    def readConnections(self, userID, key):

        print(2)
        fernet = Fernet(key)
        while True:
            try:
                print(1)
                
                encrypedmessage = userID.recv(1024)
                message = fernet.decrypt(encrypedmessage)

                if not message:
                    break  # Break the loop if no message is received (connection closed)
                print(f"Received message")  # Debugging statement
                sendToConnectedClients(message, userID)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

def server_thread(host, port, chat_window):
    server = ChatServer(host, port, chat_window)
    server.start()