import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QMessageBox, QAction,
                             QToolTip, QDesktopWidget, QSpinBox,
                             QHBoxLayout, QVBoxLayout, QTabWidget,
                             QSplashScreen, QLabel, QLineEdit,
                             QFormLayout, QGroupBox, QScrollArea)


class Window(QMainWindow):
    """
    Controls the window frame, location,
    close actions, and file menu.
    """

    def __init__(self):
        super(Window, self).__init__()

        self.title = "ChemKED GUI"
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QVBoxLayout()
        self.tabs_widget = self.tabs()
        self.layout.addWidget(self.tabs_widget)

        self.center()
        self.show()

    def center(self):
        """
        Centers the window on the screen.
        """
        fg = self.frameGeometry()
        ag = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(ag)
        self.move(fg.topLeft())

    def tabs(self):
        tabs = QTabWidget()

        tab_meta = self.tab_meta_setup()
        tab_comp = self.tab_comp_setup()
        tab_data = self.tab_data_setup()

        tabs.addTab(tab_meta, "Metadata")
        tabs.addTab(tab_comp, "Experiments")
        tabs.addTab(tab_data, "Datapoints")

        return tabs

    def tab_meta_setup(self):
        tab1 = QWidget()
        return tab1

    def tab_comp_setup(self):
        tab2 = QWidget()
        return tab2

    def tab_data_setup(self):
        tab3 = QWidget()
        return tab3


def main():
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
