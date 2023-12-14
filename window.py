import json
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLineEdit, QInputDialog


class ChatWindow(QMainWindow):
    def __init__(self, send_message_callback):
        super().__init__()
        self.init_ui(send_message_callback)

    def init_ui(self, send_message_callback):
        self.setWindowTitle("Chat App")
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
        message = {"username": "Server",
                   "text": self.input_field.text(),
                   "time": str(datetime.now())}
        self.send_message_callback(json.dumps(message))
        self.input_field.clear()

    def display_message(self, message):
        self.text_display.append(message)

    def display_message_json(self, messagein):
        message = json.loads(messagein)
        formatted_message = message["username"] + " (" + message["time"] + ") : " + message["text"]
        self.text_display.append(formatted_message)

#Merge Issues