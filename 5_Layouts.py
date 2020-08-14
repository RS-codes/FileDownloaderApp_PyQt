from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        #layout = QVBoxLayout()
        layout = QHBoxLayout()

        self.label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(self.label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()