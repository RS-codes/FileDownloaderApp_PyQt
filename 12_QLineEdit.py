#12_QLineEdit.py - under QWidgetDemo
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QApplication
import sys

class QWidgetDemos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWigetsDemo")

        line_edit = QLineEdit()

        #ex5- to view like password
        line_edit.setEchoMode(QLineEdit.Password)

        #line_edit.setText("Hello RS") #ex1-to set Text
        #line_edit.setPlaceholderText("Enter username")  #ex2-to set placeholder


        #line_edit.setText("Hello RS..")
        #line_edit.selectAll() #ex3-to select all texts from QlineEdit
        #line_edit.setReadOnly(True) #ex4-to set the text Readonly


        #text = line_edit.text()
        #print("You typed: ", text)


        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(close_button)
        self.setLayout(layout)

        #self.setFocus()

app = QApplication(sys.argv)
dialog = QWidgetDemos()
dialog.show()
app.exec_()