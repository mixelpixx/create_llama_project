import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMenuBar,
    QMenu,
    QAction,
)


class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat App")

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Chat history display
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        layout.addWidget(self.chat_history)

        # Message input area
        input_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        input_layout.addWidget(self.message_input)
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)
        layout.addLayout(input_layout)

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        load_action = QAction("Load Document", self)
        load_action.triggered.connect(self.load_document)
        file_menu.addAction(load_action)

    def send_message(self):
        message = self.message_input.text()
        self.chat_history.append(f"You: {message}")
        self.message_input.clear()

        # TODO: Send message to backend and display response

    def load_document(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            # TODO: Load and process the selected document
            self.chat_history.append(f"Loaded document: {file_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())
