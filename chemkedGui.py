import sys
from PyQt5.QtCore import QCoreApplication, Qt
# from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.uic.properties import QtGui
from PyQt5.QtWidgets import QCheckBox

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("It\'s Just a Test")
        # setWindowIcon does nothing on OSX. Works for Windows.
        # self.setWindowIcon(QIcon('pic.png'))

        extractAction = QAction('&Close GUI', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Close the window')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        self.home()

    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0, 100)

        checkBox = QCheckBox('Enlarge Window', self)
        # checkBox.toggle() # uncomment for default to be checked
        checkBox.move(0, 50)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.show()

    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)


    def close_application(self):

        choice  = QMessageBox.question(self, 'Message',
                                       "Close without saving?",
                                       QMessageBox.Yes |
                                       QMessageBox.No,
                                       QMessageBox.No)

        if choice == QMessageBox.Yes:
            print("Closing GUI")
            sys.exit()
        else:
            pass


def main():
    app = QApplication(sys.argv)
    gui = window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
