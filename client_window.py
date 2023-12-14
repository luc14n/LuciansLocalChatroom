from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLineEdit
from threading import Thread
from datetime import datetime
import json

class ClientChatWindow(QMainWindow):

    def __init__(self, send_message_callback, client_socket, username):
        super().__init__()
        self.client_socket = client_socket
        self.init_ui(send_message_callback)
        self.userName = username

    def init_ui(self, send_message_callback):
        self.setWindowTitle("Client Chat App")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        central_widget.setLayout(layout)

        self.input_field.returnPressed.connect(self.send_button_clicked)

        self.send_message_callback = send_message_callback

    def send_button_clicked(self):
        message = {"username": self.userName,
                   "text": self.input_field.text(),
                   "time": str(datetime.now())}
        self.send_message_callback(json.dumps(message))
        self.input_field.clear()

    # Add a new method to send messages through the client socket
    def send_message_to_server(self, message):
        try:
            if self.client_socket:
                self.client_socket.send(message.encode())
        except Exception as e:
            print(f"Failed to send message to server: {e}")

    def client_display_message(self, messagein):
        message = json.loads(messagein)
        formatted_message = message["username"] + " (" + message["time"] + ") : " + message["text"]
        self.text_display.append(formatted_message)

#Merge Issues