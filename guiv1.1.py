import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QMessageBox, QAction,
                             QToolTip, QDesktopWidget, QHBoxLayout,
                             QVBoxLayout, QTabWidget, QLabel,
                             QLineEdit, QFormLayout, QGroupBox,
                             QScrollArea, QSplashScreen)
from pyked import chemked


# These are the variables that will be exported to a ChemKED file


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

        meta = QVBoxLayout()  # All meta section content added to this box

        self.tab1.authors_box = QVBoxLayout()  # Additional authors added to this box
        self.tab1.btnsRemoveMetaAuthors = []  # List of buttons to remove individual meta authors
        self.tab1.metaAuthors = []  # Contains lists of author name/orcid pairs

        # This is the hard-coded required author (first row, no remove button)
        required_author = QHBoxLayout()
        required_author_name = QLineEdit()
        required_author_orcid = QLineEdit()
        required_author_name_form = QFormLayout()
        required_author_orcid_form = QFormLayout()
        required_author_name_form.addRow(QLabel('Author'), required_author_name)
        required_author_orcid_form.addRow(QLabel('ORCID'), required_author_orcid)
        required_author.addLayout(required_author_name_form)
        required_author.addLayout(required_author_orcid_form)
        add_author_button = QPushButton('Add...')
        add_author_button.clicked.connect(self.add_meta_author)
        required_author.addWidget(add_author_button)

        self.tab1.authors_box.addLayout(required_author)
        meta.addLayout(self.tab1.authors_box)

        self.tab1.setLayout(meta)

        return self.tab1

    def add_meta_author(self):
        new_author = QLineEdit()
        new_orcid = QLineEdit()
        self.tab1.metaAuthors.append([new_author, new_orcid])

        new_author_row = QHBoxLayout()

        new_author_form = QFormLayout()
        new_orcid_form = QFormLayout()
        new_author_form.addRow(QLabel('Author'), new_author)
        new_orcid_form.addRow(QLabel('ORCID'), new_orcid)

        new_author_row.addLayout(new_author_form)
        new_author_row.addLayout(new_orcid_form)

        self.tab1.authors_box.addLayout(new_author_row)

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
