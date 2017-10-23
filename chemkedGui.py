import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Still Testing")
        self.setWindowIcon(QIcon('pic.png'))
        self.show()


# app = QApplication(sys.argv)
# window = QWidget()
# window.setGeometry(50, 50, 500, 300)
# window.setWindowTitle("It\'s Just A Test")


def main():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
