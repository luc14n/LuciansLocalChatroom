from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLineEdit
from datetime import datetime
import json

class ClientChatWindow(QMainWindow):

    def __init__(self, client_socket, username):
        super().__init__()
        self.client_socket = client_socket
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
        dump = json.dumps(message)
        self.client_socket.send(dump.encode())
        self.client_display_message(dump)
        self.input_field.clear()

    def client_display_message(self, messagein):
        message = json.loads(messagein)
        formatted_message = message["username"] + " (" + message["time"] + ") : " + message["text"]
        self.text_display.append(formatted_message)

#Merge Issues