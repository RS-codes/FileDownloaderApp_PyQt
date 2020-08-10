#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
import sys

from PyQt5.QtWidgets import QApplication, QDialog

app = QApplication(sys.argv)
dialog = QDialog()
dialog.show()
sys.exit(app.exec_())
#app.exec_()
