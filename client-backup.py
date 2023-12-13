import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLineEdit, QMessageBox, QLabel
import socket

from app import send_message
from window import ChatWindow  # Import your ChatWindow from the main app


class ChatWindowWithClientSocket(ChatWindow):

    def set_client_socket(self, client_socket):
        self.client_socket = client_socket

    def send_message(self, message):
        try:
            if self.client_socket:
                self.client_socket.send(message.encode())
                print(f"Sent: {message}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to send message: {e}")
            print(f"Error sending message: {e}")


class ChatClient(QMainWindow):
    def __init__(self):
        super().__init__()  # Call the superclass constructor
        self.connect_button = None
        self.port_input = None
        self.ip_input = None
        self.port_label = None
        self.ip_label = None
        self.init_ui()  # Initialize the user interface

    def init_ui(self):
        # Initialize the user interface components here
        self.setWindowTitle("Chat Client")
        self.setGeometry(100, 100, 400, 200)

        self.ip_label = QLabel("Server IP:")
        self.port_label = QLabel("Server Port:")
        self.ip_input = QLineEdit()
        self.port_input = QLineEdit()
        self.connect_button = QPushButton("Connect")

        layout = QVBoxLayout()
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_input)
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_input)
        layout.addWidget(self.connect_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.connect_button.clicked.connect(self.connect_to_server)

    def connect_to_server(self):
        ip = self.ip_input.text()
        port = int(self.port_input.text())

        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((ip, port))
            print("Connection successful")
            # Connection successful, open chat window
            self.open_chat_window_for_client(client_socket)
        except ConnectionRefusedError:
            QMessageBox.critical(self, "Connection Error", "Failed to connect to the server.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def open_chat_window(self, client_socket):
        self.hide()

        chat_window = ChatWindowWithClientSocket(send_message)  # Use your ChatWindow implementation
        chat_window.set_client_socket(client_socket)
        chat_window.show()
        print("Chat window opened")

    def open_chat_window_for_client(self, client_socket):
        # Create a new chat window for the client
        print("1")
        chat_window = ChatWindowWithClientSocket(send_message) # , "Client Chat" # Provide a label for the client chat

        # Set the client socket and display the chat window
        print("2")
        chat_window.set_client_socket(client_socket)
        print("3")
        chat_window.show()
        print("Chat window opened")


if __name__ == '__main__':
    app = QApplication([])

    client = ChatClient()
    client.show()

    app.exec_()
