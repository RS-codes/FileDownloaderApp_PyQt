from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self) #override constructor

        layout = QVBoxLayout()

        label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout) #Constructor built

        #Handler
        button.clicked.connect(self.close)
        #Note: Dont add paranthesis after handler, like close()-this is wrong

        line_edit.textChanged.connect(label.setText)
        #here, 'textChanged' is our Event

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()