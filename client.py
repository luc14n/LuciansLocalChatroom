import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel
from threading import Thread
import socket
from client_window import ClientChatWindow

class ServerInfoDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Server Information")

        self.ip_label = QLabel("Server IP:")
        self.ip_input = QLineEdit()
        self.port_label = QLabel("Server Port:")
        self.port_input = QLineEdit()
        self.userName_label = QLabel("Username:")
        self.userName = QLineEdit()
        self.connect_button = QPushButton("Connect")

        layout = QVBoxLayout()
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_input)
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_input)
        layout.addWidget(self.userName_label)
        layout.addWidget(self.userName)
        layout.addWidget(self.connect_button)

        self.setLayout(layout)

        self.connect_button.clicked.connect(self.connect_to_server)

    def connect_to_server(self):
        global server_socket, client_chat_window

        server_ip = self.ip_input.text()
        server_port = int(self.port_input.text())

        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((server_ip, server_port))

            # Connection successful, open client chat window
            self.hide()  # Hide the server info dialog
            client_chat_window = open_client_chat_window(server_socket, self.userName.text())
            client_chat_window.show()
        except ConnectionRefusedError:
            print("Failed to connect to the server.")
        except Exception as e:
            print(f"An error occurred: {e}")


def open_client_chat_window(client_socket, username):
    global client_chat_window

    # Ensure thread safety by using a local variable
    new_client_chat_window = ClientChatWindow(client_socket, username)

    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break  # Break the loop if no message is received (connection closed)
                print(f"Received message")
                new_client_chat_window.client_display_message(message)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    # Start a thread for continuous communication
    communication_thread = Thread(target=receive_messages)
    communication_thread.daemon = True
    communication_thread.start()

    return new_client_chat_window


if __name__ == '__main__':
    app = QApplication(sys.argv)

    server_socket = None  # Initialize server_socket
    client_chat_window = None  # Initialize client_chat_window

    server_info_dialog = ServerInfoDialog()
    server_info_dialog.show()  # Use show() instead of exec_()

    sys.exit(app.exec_())

#Merge Issues