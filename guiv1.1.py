import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QMessageBox, QAction,
                             QToolTip, QDesktopWidget, QHBoxLayout,
                             QVBoxLayout, QTabWidget, QLabel,
                             QLineEdit, QFormLayout, QGroupBox,
                             QScrollArea, QSplashScreen)
from pyked import chemked


class WindowFrame(QMainWindow):
    """
    Controls main window handling.
    """

    def __init__(self):
        super(WindowFrame, self).__init__()

        # Set up window size and location
        self.setWindowTitle('ChemKED GUI')
        self.setGeometry(0, 0, 800, 600)
        self.center()

        # Set up the main widget, the tabs
        self.layout = QVBoxLayout()
        self.tabs_widget = Tabs(self)
        self.setCentralWidget(self.tabs_widget)


        # Display the window
        self.show()

    def center(self):
        """
        Centers the window on the screen.
        """
        # Get window geometry, make frame
        frame = self.frameGeometry()
        # Get screen resolution
        screen_resolution = QDesktopWidget().availableGeometry().center()
        # Move frame to center of screen
        frame.moveCenter(screen_resolution)
        # Move window to frame
        self.move(frame.topLeft())

    # def closeEvent(self, event):
    #     """
    #     Prompts the user before closing the window.
    #     """
    #     reply = QMessageBox.Question(self, 'Message', 'Are you sure you want to quit?',
    #                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    #
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


class Tabs(QWidget):
    """
    Creates tabs and returns them in a
    QWidget containing a QVBoxLayout.
    """

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        self.tab1 = self.tab_1_setup()  # File metadata/reference 'Meta'
        self.tab2 = self.tab_2_setup()  # Experiment data 'Experiment'
        self.tab3 = self.tab_3_setup()  # Datapoints 'Data'

        self.tabs.addTab(self.tab1, 'Meta')
        self.tabs.addTab(self.tab2, 'Experiment')
        self.tabs.addTab(self.tab3, 'Data')

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def tab_1_setup(self):
        self.tab1 = QWidget()  # This is the returned QWidget

        meta_authors = []
        meta_orcids = []
        meta_values = [file_version, chemked_version] = \
                      [QLineEdit('0'), QLineEdit('0.0.1')]
        meta_labels = ['File Version', 'ChemKED Version']

        ref_authors = []
        ref_orcids = []
        ref_values = [doi, ref_authors, journal, year, volume, pages, detail] = \
                     [QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit(), QLineEdit()]
        ref_labels = ['DOI', 'Author(s)', 'Journal', 'Year', 'Volume', 'Pages', 'Detail']

        tab_1_vbox = QVBoxLayout()
        tab_1_hbox = QHBoxLayout()

        meta_auths_box = QVBoxLayout()
        meta_form = QFormLayout()
        ref_form_header = QFormLayout()
        ref_form_auth_box = QVBoxLayout()
        ref_form_footer = QFormLayout()

        meta_auth_1_hbox = QHBoxLayout()
        meta_auth_1_auth = QLineEdit()
        meta_auth_1_orcid = QLineEdit()
        meta_auth_1_auth_form = QFormLayout()
        meta_auth_1_auth_form.addRow(QLabel('Author'), meta_auth_1_auth)
        meta_auth_1_orcid_form = QFormLayout()
        meta_auth_1_orcid_form.addRow(QLabel('ORCID'), meta_auth_1_orcid)
        meta_auth_1_hbox.addLayout(meta_auth_1_auth_form)
        meta_auth_1_hbox.addLayout(meta_auth_1_orcid_form)

        meta_auths_box.addLayout(meta_auth_1_hbox)
        tab_1_vbox.addLayout(meta_auths_box)

        for label, value in zip(meta_labels, meta_values):
            meta_form.addRow(QLabel(label), value)

        # for label, value in zip(ref_labels, ref_values):
        #     ref_form.addRow(QLabel(label), value)

        tab_1_hbox.addLayout(meta_form)
        # tab_1_hbox.addLayout(ref_form)

        tab_1_vbox.addLayout(tab_1_hbox)
        self.tab1.setLayout(tab_1_vbox)

        return self.tab1

    def tab_2_setup(self):
        self.tab2 = QWidget()
        return self.tab2

    def tab_3_setup(self):
        self.tab3 = QWidget()
        return self.tab3


def main():
    app = QApplication(sys.argv)
    gui = WindowFrame()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
