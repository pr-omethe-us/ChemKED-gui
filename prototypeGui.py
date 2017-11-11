import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QPushButton, QMessageBox, QAction
from PyQt5.QtWidgets import QToolTip, QDesktopWidget, qApp
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QTabWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QFormLayout, QGroupBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import pyqtSlot

class Window(QMainWindow):
    def __init__(self):
        # Inherits class methods from QMainWindow
        super(Window, self).__init__()
        self.title = 'Prototype ChemKED GUI'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.vbox = QVBoxLayout()
        self.table_widget = Table(self)
        self.vbox.addWidget(self.table_widget)
        self.setCentralWidget(self.table_widget)

        self.center()

        # Easily close the GUI (without saving)
        close_gui = QAction("&Close GUI", self)
        close_gui.setShortcut('Ctrl+Q')
        close_gui.setStatusTip('Close without saving.')
        close_gui.triggered.connect(self.closeEvent)

        self.show()


    def center(self):
        """
        Centers the window
        on the screen.
        """

        # Get window geometry.
        qr = self.frameGeometry()
        # Get screen resolution.
        cp = QDesktopWidget().availableGeometry().center()
        # Move center of rectangle of equal size to geometry
        #  to the center of the screen.
        qr.moveCenter(cp)
        # Move the top left corner of the geometry to the
        #  top left corner of the rectangle.
        self.move(qr.topLeft())

    # def close_application(self):
    #
    #     choice = QMessageBox.question(self, 'Message',
    #                                    "Are you sure to quit?",
    #                                    QMessageBox.Yes |
    #                                    QMessageBox.No,
    #                                    QMessageBox.No)
    #
    #     if choice == QMessageBox.Yes:
    #         print("Closing GUI")
    #         sys.exit()
    #     else:
    #         pass


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class Table(QWidget):
    """
    This class creates a tab widget, which contains tabs.
    The tab widget is placed onto the object called by the
    Window class.

    Bugs:
    1. QLayout: Attempting to add QLayout "" to Table "", which already has a layout
        Not sure what's causing this, doesn't seem to affect functionality.
    """


    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300, 200)

        # Tab 1 contents
        author_name = QLineEdit()
        author_orcid = QLineEdit()
        file_version = QLineEdit()
        chemked_version = QLineEdit()
        doi = QLineEdit()
        ref_authors = QLineEdit()
        journal = QLineEdit()
        year = QLineEdit()
        volume = QLineEdit()
        pages = QLineEdit()
        detail = QLineEdit()

        self.tab1.metadata_values = [author_name, author_orcid, file_version,
                            chemked_version]
        self.tab1.reference_values = [doi, ref_authors, journal,
                            year, volume, pages, detail]
        self.tab1.metadata_labels = ['Author Name', 'Author ORCID', 'File Version', 'ChemKED Version']
        self.tab1.reference_labels = ['DOI', 'Author(s)', 'Journal',
                            'Year', 'Volume', 'Pages', 'Detail']

        self.tab1.vbox = QVBoxLayout()
        self.tab1.formGroupBox = QGroupBox()
        self.tab1.formLayout = QFormLayout()
        for i in range(len(self.tab1.metadata_labels)):
            self.tab1.formLayout.addRow(QLabel(self.tab1.metadata_labels[i]),
                                        self.tab1.metadata_values[i])
        self.tab1.formLayout.addRow(QLabel(''))
        self.tab1.formLayout.addRow(QLabel('Reference Information'))
        for i in range(len(self.tab1.reference_labels)):
            self.tab1.formLayout.addRow(QLabel(self.tab1.reference_labels[i]),
                                        self.tab1.reference_values[i])
        self.tab1.formGroupBox.setLayout(self.tab1.formLayout)
        self.tab1.vbox.addWidget(self.tab1.formGroupBox)
        self.tab1.setLayout(self.tab1.vbox)

        # Tab 2 contents
        self.tab2.vbox = QVBoxLayout()
        self.tab2.formGroupBox = QGroupBox()
        self.tab2.formLayout = QFormLayout()
        self.tab2.formLayout.addRow(QLabel('Experiment Type'), QLineEdit('Ignition Delay'))
        self.tab2.formLayout.addRow(QLabel(''))
        self.tab2.formLayout.addRow(QLabel('Apparatus Information'))
        self.tab2.formLayout.addRow(QLabel('Kind'), QLineEdit())
        self.tab2.formLayout.addRow(QLabel('Institution'), QLineEdit())
        self.tab2.formLayout.addRow(QLabel('Facility'), QLineEdit())
        self.tab2.formLayout.addRow(QLabel(''))
        self.tab2.formLayout.addRow(QLabel('Common Properties'))
        self.tab2.formGroupBox.setLayout(self.tab2.formLayout)
        self.tab2.vbox.addWidget(self.tab2.formGroupBox)
        self.tab2.setLayout(self.tab2.vbox)

        # Tab 3 contents

        # Add tabs to vbox
        self.tabs.addTab(self.tab1, "File Information")
        self.tabs.addTab(self.tab2, "Experiment Information")
        self.tabs.addTab(self.tab3, "Datapoints")

        # Export to YAML button
        self.export_button = QPushButton('Export')
        self.export_button.resize(self.export_button.sizeHint())

        # Add tabs to Window
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.export_button)
        self.setLayout(self.layout)

        self.export_button.clicked.connect(self.export)


    def export(self):
        values = []
        for item in self.tab1.metadata_values:
            item = item.text()
            values.append(item)
        with open('testing.txt', 'w') as f:
            for item in values:
                f.write(item + '\n')


    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


def main():
    # Define application
    app = QApplication(sys.argv)

    # Define window
    gui = Window()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
