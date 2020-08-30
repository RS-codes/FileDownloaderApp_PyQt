#14_QCheckBox.py - under QWidgetDemo
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QApplication, QLabel, QCheckBox
import sys

class QWidgetDemos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgets Demo")

        #ex2-to make handler to check whether checkbox is checked or not
        #1stmake checkbox-into an instance wide variable, by adding self.
        self.checkbox = QCheckBox()
        self.checkbox.setText("Check me..!")

        #ex1-To keep it checked, by default
        #checkbox.setChecked(True)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(close_button)
        self.setLayout(layout)

        self.setFocus()

        #ex3-cont'd
        #3rd connect the Signal and Slot
        self.checkbox.stateChanged.connect(self.selected)
    #ex2-cont'd
    #2ndDefine a method handler- To check the status of Checkbox
    def selected(self):
        if self.checkbox.isChecked():
            print("Yes, it is Checked..!")
        else:
            print("It is UnChecked, now..!")

app = QApplication(sys.argv)
dialog = QWidgetDemos()
dialog.show()
app.exec_()
