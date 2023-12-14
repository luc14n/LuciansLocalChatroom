from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLineEdit
from datetime import datetime
import json
from cryptography.fernet import Fernet


# User key
key = Fernet.generate_key()
fernet = Fernet(key)

class ClientChatWindow(QMainWindow):

    def __init__(self, client_socket, username):
        super().__init__()
        self.input_field = None
        self.text_display = None
        self.client_socket = client_socket
        self.userName = username

        self.init_ui()

    def init_ui(self):
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

    def send_button_clicked(self):
        message = {"username": self.userName,
                   "text": self.input_field.text(),
                   "time": str(datetime.now())}
        dump = json.dumps(message)

        sendMessage(dump, self.client_socket)

        self.client_display_message(dump)
        self.input_field.clear()

    def client_display_message(self, messagein):
        message = json.loads(messagein)
        formatted_message = message["username"] + " (" + message["time"] + ") : " + message["text"]
        self.text_display.append(formatted_message)

def sendMessage(message, socket):
    encyptedDump = fernet.encrypt(message.encode())
    socket.send(encyptedDump)