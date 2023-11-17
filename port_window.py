from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class PortWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Enter Port Number")
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()

        label = QLabel("Please enter a 5-digit port number:")
        self.port_input = QLineEdit()
        submit_button = QPushButton("Submit")

        layout.addWidget(label)
        layout.addWidget(self.port_input)
        layout.addWidget(submit_button)

        submit_button.clicked.connect(self.submit_button_clicked)

        self.setLayout(layout)

    def submit_button_clicked(self):
        port_number = self.port_input.text()
        if port_number.isdigit() and len(port_number) == 5:
            self.accept()
        else:
            # Display an error message or handle invalid input as needed
            pass
