#15_QComboBox.py - under QWidgetDemo
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QApplication, QLabel, QCheckBox, QComboBox
import sys

class QWidgetDemos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgets Demo")

        self.combobox = QComboBox()

        #ex1 - To add items in Dropdown Menu
        # self.combobox.addItem("Apple")
        # self.combobox.addItem("Orange")
        # self.combobox.addItem("Banana")


        #ex2 - To add n- No. of items in a single Line
        #takes list of strings as argument
        self.combobox.addItems(["-Select-", "Apple", "Orange", "Banana", "Grapes", "Strawberry", "Raspberry", "Blueberry"])

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.combobox)
        layout.addWidget(close_button)
        self.setLayout(layout)

        self.setFocus()

        #ex3 1st-connect Signal and Slot to view what is selected
        self.combobox.currentIndexChanged.connect(self.selected)

    #ex3-cont'd 2nd define the method
    #Define a method-EventHandler
    def selected(self):
        current_text = self.combobox.currentText()
        current_index = str(self.combobox.currentIndex())

        if current_index == "0":
            print("Nothing selected")
        else:
            print(current_text + " at the index " + current_index + " has been selected")


app = QApplication(sys.argv)
dialog = QWidgetDemos()
dialog.show()
app.exec_()