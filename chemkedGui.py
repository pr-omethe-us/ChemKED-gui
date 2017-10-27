import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCalendarWidget, QFontDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory
from PyQt5.QtWidgets import QColorDialog, QTextEdit


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

        extractAction = QAction(QIcon('pic.png'), 'Leave', self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        fontChoice = QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)
        self.toolBar = self.addToolBar('Font')
        self.toolBar.addAction(fontChoice)

        self.home()

    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget{background-color: %s}' % color.name())

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)


    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0, 100)

        checkBox = QCheckBox('Enlarge Window', self)
        # uncomment for default to be checked (broken, though)
        # checkBox.toggle()
        checkBox.move(0, 50)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QPushButton('Download', self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        self.styleChoice = QLabel('Windows', self)
        comboBox = QComboBox(self)
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('Cleanlooks')
        comboBox.addItem('windowsvista')

        comboBox.move(25, 250)
        self.styleChoice.move(25, 150)
        comboBox.activated[str].connect(self.style_choice)

        self.show()

    def style_choice(self):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def download(self):
        self.completed = 0

        # The conditions under which the progress
        # bar fills can be modified
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

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
