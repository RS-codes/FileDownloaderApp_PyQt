from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys

class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self) #override constructor

        layout = QVBoxLayout()

        #edit1
        self.label = QLabel("Hello World!")

        line_edit = QLineEdit()
        button = QPushButton("Close")

        #edit2
        layout.addWidget(self.label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        self.setLayout(layout) #Constructor built

        #Handler
        button.clicked.connect(self.close)
        #Note: Dont add paranthesis after handler, like close()-this is wrong
        # no need to pass argument also in close()

        line_edit.textChanged.connect(self.changeTextLabel)
        #here, 'textChanged' is our Event
        # 'changeTextLabel' is our Handler

    #Our Own user-defined Handler
    def changeTextLabel(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()