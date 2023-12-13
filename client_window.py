from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QLineEdit
from threading import Thread

class ClientChatWindow(QMainWindow):
    message_received = pyqtSignal(str, str)  # signal for the message and sender

    def __init__(self, send_message_callback, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.init_ui(send_message_callback)

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

        send_button = QPushButton("Send")

        # Adds the send button to the widget
        #layout.addWidget(send_button)

        central_widget.setLayout(layout)

        send_button.clicked.connect(self.send_button_clicked)
        self.input_field.returnPressed.connect(self.send_button_clicked)

        self.send_message_callback = send_message_callback

    def send_button_clicked(self):
        message = self.input_field.text()
        self.send_message_callback(message)
        self.input_field.clear()

    def send_message(self, client_chat_window, message):
        if message:
            self.message_received.emit(message)
            self.input_field.clear()

    # Add a new method to send messages through the client socket
    def send_message_to_server(self, message):
        try:
            if self.client_socket:
                self.client_socket.send(message.encode())
        except Exception as e:
            print(f"Failed to send message to server: {e}")

    def display_message(self, message, sender=None):
        if sender :
            formatted_message = f"{sender}: {message}"
        else:
            formatted_message = message
        self.text_display.append(formatted_message)

    def start_receive_thread(self):
        # Start a thread for continuous communication
        communication_thread = Thread(target=self.receive_messages)
        communication_thread.daemon = True
        communication_thread.start()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break  # Break the loop if no message is received (connection closed)
                # Emit the signal with the received message and sender
                self.message_received.emit(message, "Server")
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

#Merge Issues