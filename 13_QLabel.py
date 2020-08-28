#13_QLabel.py - under QWidgetDemo
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QApplication, QLabel
import sys

class QWidgetDemos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgetsDemo")

        #label = QLabel("Hello RS..") #can also be done

        label = QLabel()
        #label.setText("Hello RS..") #Or we can set like this also

        #supports HTML CSS
        label.setText("<b>Hello RS..</b>") #to make bold text,HTML

        
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(close_button)
        self.setLayout(layout)

        self.setFocus()

app = QApplication(sys.argv)
dialog = QWidgetDemos()
dialog.show()
app.exec_()


