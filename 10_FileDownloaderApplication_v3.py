#Additional Functionality added - FileDownloaderApplication

from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLineEdit, QPushButton, QProgressBar, QMessageBox
import sys

import urllib.request

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self) #UI interface

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save_location")

        self.progress.setValue(0)
        #progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("MyDownloader")
        #self.setFocus()

        download.clicked.connect(self.download)

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()

    #edit2- add try exception block
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed")
            return
    #edit1
        QMessageBox.information(self, "Information", "The download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")


    def report(self, blocknum, blocksize, totalsize):
        sizeread = blocknum * blocksize
        if totalsize > 0:
            percent = (sizeread * 100 / totalsize) + 1
            self.progress.setValue(int(percent))


app = QApplication(sys.argv)
d1 = Downloader()
d1.show()
sys.exit(app.exec_())


#URL: https://blogs.3ds.com/northamerica/wp-content/uploads/sites/4/2019/08/Robots-Square.jpg
#URL2: https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Atlas_from_boston_dynamics.jpg/220px-Atlas_from_boston_dynamics.jpg
#savelocation: /home/rs/Downloads/filename.jpeg  (Remeber to give a filename and its respective extension)