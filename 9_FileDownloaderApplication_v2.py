#Basic Functionality added - FileDownloaderApplication

from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLineEdit, QPushButton, QProgressBar
import sys

import urllib.request

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self) #UI interface

        layout = QVBoxLayout()
    #edit3
    #make 'QLineEdit' into an INSTANCE_WIDE_VARIABLE
    #Inorder to obtain the user input URL and savelocation
    #add self. infront of url and savelocation, variables everywhere
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save_location")

    # edit6 add self.progress everywhere
        self.progress.setValue(0)
        #progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("MyDownloader")
        #self.setFocus()

    #edit2
        download.clicked.connect(self.download)

    #edit1
    #DEFINING A NEW USER-DEFINED METHOD
    def download(self):
    #edit5-define the function
        url = self.url.text()
        save_location = self.save_location.text()
    #text()-is used to Grab the user input and return to it
        #use urlretrieve method from urllibrary
        urllib.request.urlretrieve(url, save_location, self.report)


    #edit4-create function that urlretrieve will report to and tell it
    #about the file size and path
    def report(self, blocknum, blocksize, totalsize):
        sizeread = blocknum * blocksize
        if totalsize > 0:
            percent = (sizeread * 100 / totalsize) + 1
            self.progress.setValue(int(percent))


app = QApplication(sys.argv)
d1 = Downloader()
d1.show()  #shows the UI
#app.exec_()
sys.exit(app.exec_())


#URL: https://blogs.3ds.com/northamerica/wp-content/uploads/sites/4/2019/08/Robots-Square.jpg
#URL2: https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Atlas_from_boston_dynamics.jpg/220px-Atlas_from_boston_dynamics.jpg
#savelocation: /home/rs/Downloads/filename.jpeg  (Remeber to give a filename and its respective extension)