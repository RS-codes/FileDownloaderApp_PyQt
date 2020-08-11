#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5 import Qt
#from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout)

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()