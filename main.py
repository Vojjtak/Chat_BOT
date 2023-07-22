import sys
from backend import Chatbot
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, \
    QApplication
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)
        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 400, 30)
        self.input_field.returnPressed.connect(self.send_message)
        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(420, 340, 80, 30)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"Me: {user_input}")
        self.input_field.clear()
        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"Bot: {response}")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
