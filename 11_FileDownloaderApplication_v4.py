#Extended Functionality added - FileDownloaderApplication
#Browse computer and give save location-functionality added
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLineEdit, QPushButton, QProgressBar, QMessageBox, \
    QFileDialog
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
    #edit1-add Browse button
        browse = QPushButton("Browse")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save_location")

        self.progress.setValue(0)
        #progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
    #edit2 - add Browse button widgetbelow save-location
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("MyDownloader")
        #self.setFocus()

        download.clicked.connect(self.download)
    #edit3 - connect the browse Signal to Slot (we need to define the method also)
        browse.clicked.connect(self.browse_file) #browse-file method has to be defined

    #edit4 - define method- browsefile
    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As", directory=".",
                                                    filter="All Files(*.*)")
        self.save_location.setText(QDir.toNativeSeparators(str(save_file[0])))

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed")
            return

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