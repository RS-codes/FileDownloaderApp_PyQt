#Basic UI Design - FileDownloaderApplication

from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLineEdit, QPushButton, QProgressBar
import sys
#from PyQt5.QtCore import Qt
#from PyQt5.QtCore import *

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self) #UI interface

        layout = QVBoxLayout()

        url = QLineEdit()
        save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")

        url.setPlaceholderText("URL")
        save_location.setPlaceholderText("File save_location")

        progress.setValue(0)
        #progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("MyDownloader")

app = QApplication(sys.argv)
d1 = Downloader()
d1.show()  #shows the UI
app.exec_()

