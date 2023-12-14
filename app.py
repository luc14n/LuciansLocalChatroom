import json
import sys
import threading
import time
from datetime import datetime

import requests
from PyQt5.QtWidgets import QApplication
from window import ChatWindow
from port_window import PortWindow
import socket
import server

def get_local_ip():
    try:
        # Connect to an external server to determine the local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        print(f"Error getting local IP: {e}")
        return None

def send_message(message):
    chat_window.display_message_json(message)  # Display your messages
    server.sendToConnectedClients(message.encode(), None)

def main(port_number):
    # Get the IP address of the system
    ip_address = get_local_ip()

    # Display the port number and IP address
    chat_window.display_message(f"---------------------------------")
    chat_window.display_message(f"IP Address: {ip_address}")
    chat_window.display_message(f"Port Number: {port_number}")
    chat_window.display_message(f"---------------------------------")

    #sys.exit(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    port_window = PortWindow()
    result = port_window.exec_()

    if result == PortWindow.Accepted:
        port_number = port_window.port_input.text()
    else:
        sys.exit(1)  # Exit if the port window is canceled

    chat_window = ChatWindow(send_message)
    chat_window.show()

    # Start the server in the background
    server_thread = threading.Thread(target=server.server_thread, args=(get_local_ip(), int(port_number), chat_window))
    server_thread.daemon = True
    server_thread.start()

    # Add a delay to allow the server to set up
    time.sleep(1)

    main(port_number)  # Call the main function after creating the chat window

    sys.exit(app.exec_())

#Merge Issues