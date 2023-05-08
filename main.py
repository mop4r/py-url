import sys
import pyshorteners
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("URL Shortener")
        self.setGeometry(200, 200, 500, 200)

        self.create_widgets()
        self.show()

    def create_widgets(self):
        # create label and entry for long URL
        self.long_url_label = QLabel("Enter the URL to shorten:")
        self.long_url_entry = QLineEdit()
        long_url_layout = QHBoxLayout()
        long_url_layout.addWidget(self.long_url_label)
        long_url_layout.addWidget(self.long_url_entry)

        # create button to shorten URL
        self.shorten_button = QPushButton("Shorten URL")
        self.shorten_button.clicked.connect(self.shorten_url)

        # create label for shortened URL
        self.short_url_label = QLabel("The shortened URL is:")
        self.short_url_entry = QLineEdit()
        self.short_url_entry.setReadOnly(True)
        short_url_layout = QHBoxLayout()
        short_url_layout.addWidget(self.short_url_label)
        short_url_layout.addWidget(self.short_url_entry)

        # create button to copy the shortened URL
        self.copy_button = QPushButton("Copy URL")
        self.copy_button.clicked.connect(self.copy_url)

        # add widgets to layout
        layout = QVBoxLayout()
        layout.addLayout(long_url_layout)
        layout.addWidget(self.shorten_button)
        layout.addLayout(short_url_layout)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

    def shorten_url(self):
        # get the long URL from the entry widget
        long_url = self.long_url_entry.text()

        # shorten the URL using pyshorteners library
        s = pyshorteners.Shortener(api_key=" SUA API KEY AQUI ")
        short_url = s.bitly.short(long_url)

        # display the shortened URL in the label widget
        self.short_url_entry.setText(short_url)

    def copy_url(self):
        # get the shortened URL from the label widget
        short_url = self.short_url_entry.text()

        # copy the shortened URL to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(short_url)

        # show a message box to confirm the copy operation
        QMessageBox.information(self, "URL Copied", "The shortened URL has been copied to the clipboard.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
