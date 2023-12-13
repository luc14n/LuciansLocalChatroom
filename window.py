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

    def display_message(self, message):
        self.text_display.append(message)

#Merge Issues