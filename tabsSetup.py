import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QMessageBox, QAction,
                             QToolTip, QDesktopWidget, QSpinBox,
                             QHBoxLayout, QVBoxLayout, QTabWidget,
                             QSplashScreen, QLabel, QLineEdit,
                             QFormLayout, QGroupBox, QScrollArea)

class Tabs(QVBoxLayout):
    """
    Instantiates a QVBoxLayout object with
    tabs as the only widget contents.
    """

    def __init__(self):
        super(Tabs, self).__init__()

        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tab_meta = self.tab_meta_setup()
        self.tab_comp = self.tab_comp_setup()
        self.tab_data = self.tab_data_setup()

        self.tabs.addTab(self.tab_meta, "Metadata")
        self.tabs.addTab(self.tab_comp, "Experiment")
        self.tabs.addTab(self.tab_data, "Datapoints")

        self.layout.addWidget(self.tabs)

    def tab_meta_setup(self):
        pass

    def tab_comp_setup(self):
        pass

    def tab_data_setup(self):
        pass