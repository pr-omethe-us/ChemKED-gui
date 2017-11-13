import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
        QPushButton, QMessageBox, QAction, QToolTip, QDesktopWidget, QSpinBox,
        QHBoxLayout, QVBoxLayout, QTabWidget, QSplashScreen,
        QLabel, QLineEdit, QFormLayout, QGroupBox, QScrollArea,
        QScrollBar)
from PyQt5.QtGui import *
# from PyQt5.QtCore import *


class Window(QMainWindow):
    """
    Controls main window handling.
    """
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
        self.setWindowIcon(QIcon('pyked-logo.png'))

        self.vbox = QVBoxLayout()

        # The Table Class handles the majority of the work.
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
        Centers the window on the screen.
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


    def closeEvent(self, event):
        """
        Prompts the user before closing window.
        """
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class Table(QWidget):
    """
    This class handles creating tabs, their contents, and exporting to YAML.
    In each tab is file information.
    When the Export button is clicked, the information
    entered is exported to a YAML file.
    """

    def __init__(self, parent):
        """
        Sets up tabs and contents.
        """
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
        file_version = QLineEdit('0')
        chemked_version = QLineEdit('0.0.1')

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
        self.tab2.add_button = QPushButton('Add...')
        self.tab2.add_button.clicked.connect(self.addSpecies)
        self.tab2.remove_button = QPushButton('Remove...')
        self.tab2.remove_button.clicked.connect(self.removeSpecies)

        self.tab2.num_species = 0

        self.tab2.experiment_type = QLineEdit('ignition delay')
        self.tab2.apparatus_kind = QLineEdit()
        self.tab2.apparatus_institution = QLineEdit()
        self.tab2.apparatus_facility = QLineEdit()
        self.tab2.comp_kind = QLineEdit()
        self.tab2.ignition_target = QLineEdit()
        self.tab2.ignition_type = QLineEdit()

        self.tab2.species = []
        self.tab2.species_names = []
        self.tab2.InChIs = []
        self.tab2.amounts = []

        # Seems to either be a bug or tricky code with making scroll bars work
        # self.tab2.scroll_area = QScrollArea()
        # self.tab2.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.tab2.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.tab2.scroll_area.setWidgetResizable(False)

        self.tab2.hbox = QHBoxLayout()
        self.tab2.formGroupBox_1 = QGroupBox()
        self.tab2.formGroupBox_2 = QGroupBox()
        self.tab2.formLayout_1 = QFormLayout()
        self.tab2.formLayout_2 = QFormLayout()

        self.tab2.formLayout_1.addRow(QLabel('Composition Information'))
        self.tab2.formLayout_1.addRow(QLabel('Kind'), self.tab2.comp_kind)
        self.tab2.formLayout_1.addRow(QLabel(''))
        self.tab2.formLayout_1_species_header = QHBoxLayout()
        self.tab2.formLayout_1_species_header.addWidget(QLabel('Species Information'))
        self.tab2.formLayout_1_species_header.addWidget(self.tab2.add_button)
        self.tab2.formLayout_1_species_header.addWidget(self.tab2.remove_button)
        self.tab2.formLayout_1.addRow(self.tab2.formLayout_1_species_header)

        self.tab2.formLayout_2.addRow(QLabel('Experiment Type'), self.tab2.experiment_type)
        self.tab2.formLayout_2.addRow(QLabel(''))
        self.tab2.formLayout_2.addRow(QLabel('Apparatus Information'))
        self.tab2.formLayout_2.addRow(QLabel('Kind'), self.tab2.apparatus_kind)
        self.tab2.formLayout_2.addRow(QLabel('Institution'), self.tab2.apparatus_institution)
        self.tab2.formLayout_2.addRow(QLabel('Facility'), self.tab2.apparatus_facility)
        self.tab2.formLayout_2.addRow(QLabel(''))
        self.tab2.formLayout_2.addRow(QLabel('Ignition Information'))
        self.tab2.formLayout_2.addRow(QLabel('Target'), self.tab2.ignition_target)
        self.tab2.formLayout_2.addRow(QLabel('Type'), self.tab2.ignition_type)

        # self.tab2.scroll_area.setWidget(self.tab2.formLayout_1)
        self.tab2.formGroupBox_1.setLayout(self.tab2.formLayout_1)
        self.tab2.formGroupBox_2.setLayout(self.tab2.formLayout_2)

        self.tab2.hbox.addWidget(self.tab2.formGroupBox_2)
        self.tab2.hbox.addWidget(self.tab2.formGroupBox_1)

        self.tab2.setLayout(self.tab2.hbox)

        # Tab 3 contents
        self.tab3.add_button = QPushButton('Add...')
        self.tab3.add_button.clicked.connect(self.addDatapoint)
        self.tab3.remove_button = QPushButton('Remove...')
        self.tab3.remove_button.clicked.connect(self.removeDatapoint)

        self.tab3.num_datapoints = 0

        self.tab3.datapoints = []
        self.tab3.temperatures = []
        self.tab3.pressures = []
        self.tab3.ignition_delays = []
        self.tab3.equivalence_ratios = []

        self.tab3.vbox = QVBoxLayout()
        self.tab3.formGroupBox = QGroupBox()
        self.tab3.formLayout = QFormLayout()

        self.tab3.tab_header = QHBoxLayout()
        self.tab3.tab_header.addWidget(self.tab3.add_button)
        self.tab3.tab_header.addWidget(self.tab3.remove_button)

        self.tab3.formGroupBox.setLayout(self.tab3.formLayout)
        self.tab3.vbox.addItem(self.tab3.tab_header)
        self.tab3.vbox.addWidget(self.tab3.formGroupBox)
        self.tab3.setLayout(self.tab3.vbox)

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

    def addSpecies(self):
        """
        Adds more fields for species on second tab.
        """
        self.tab2.species_names.append(QLineEdit())
        self.tab2.InChIs.append(QLineEdit())
        self.tab2.amounts.append(QLineEdit())
        self.tab2.formLayout_1.addRow(QLabel('Species ' + str(self.tab2.num_species+1)))
        self.tab2.formLayout_1.addRow(QLabel('Name'), self.tab2.species_names[self.tab2.num_species])
        self.tab2.formLayout_1.addRow(QLabel('InChI'), self.tab2.InChIs[self.tab2.num_species])
        self.tab2.formLayout_1.addRow(QLabel('Amount'), self.tab2.amounts[self.tab2.num_species])
        self.tab2.num_species += 1

    def addDatapoint(self):
        """
        Adds more fields for datapoints on third tab.
        """
        self.tab3.temperatures.append(QLineEdit())
        self.tab3.pressures.append(QLineEdit())
        self.tab3.ignition_delays.append(QLineEdit())
        self.tab3.equivalence_ratios.append(QLineEdit())
        self.tab3.formLayout.addRow(QLabel('Datapoint ' + str(self.tab3.num_datapoints+1)))
        self.tab3.formLayout.addRow(QLabel('Temperature (K)'), self.tab3.temperatures[self.tab3.num_datapoints])
        self.tab3.formLayout.addRow(QLabel('Pressure (atm)'), self.tab3.pressures[self.tab3.num_datapoints])
        self.tab3.formLayout.addRow(QLabel('Ignition Delay (us)'), self.tab3.ignition_delays[self.tab3.num_datapoints])
        self.tab3.formLayout.addRow(QLabel('Equivalence Ratio'), self.tab3.equivalence_ratios[self.tab3.num_datapoints])
        self.tab3.formGroupBox.setLayout(self.tab3.formLayout)
        self.tab3.vbox.addWidget(self.tab3.formGroupBox)
        self.tab3.setLayout(self.tab3.vbox)
        self.tab3.num_datapoints += 1

    def removeSpecies(self):
        """
        Removes fields for species in second tab.
        """
        if len(self.tab2.species_names) > 0:
            del self.tab2.species_names[-1]
            del self.tab2.InChIs[-1]
            del self.tab2.amounts[-1]
            remove_iter = 4
            while remove_iter > 0:
                self.tab2.formLayout_1.removeRow(self.tab2.formLayout_1.rowCount()-1)
                remove_iter -= 1
            self.tab2.num_species -= 1
        else:
            pass

    def removeDatapoint(self):
        """
        Removes fields for datapoints in third tab.
        """
        if len(self.tab3.temperatures) > 0:
            del self.tab3.temperatures[-1]
            del self.tab3.pressures[-1]
            del self.tab3.ignition_delays[-1]
            del self.tab3.equivalence_ratios[-1]
            remove_iter = 5
            while remove_iter > 0:
                self.tab3.formLayout.removeRow(self.tab3.formLayout.rowCount()-1)
                remove_iter -= 1
            self.tab3.num_datapoints -= 1
        else:
            pass

    def export(self):
        """
        Exports to a YAML document.
        This can DEFINITELY be optimized further.
        ...but it works.
        """

        for i in range(len(self.tab2.species_names)):
            self.tab2.species.append([self.tab2.species_names[i].text(),
                                      self.tab2.InChIs[i].text(),
                                      self.tab2.amounts[i].text()])

        for i in range(len(self.tab3.temperatures)):
            self.tab3.datapoints.append([self.tab3.temperatures[i].text(),
                                         self.tab3.ignition_delays[i].text(),
                                         self.tab3.pressures[i].text(),
                                         self.tab3.equivalence_ratios[i].text()])

        metadata_labels = ['    name: ', '    ORCID: ',
                           'file-version: ', 'chemked-version: ']
        reference_labels = ['    doi: ', '    authors: ', '    journal: ', '    year: ',
                            '    volume: ', '    pages: ', '    detail: ']
        datapoint_labels = ['    - temperature:', '      ignition-delay:',
                            '      pressure:', '      composition: *comp',
                            '      ignition-type: *ign', '      equivalence-ratio: ']

        with open(self.tab2.species[0][0]+'.yaml', 'w') as f:
            # Write file metadata
            f.write('---\nfile-author:\n')
            for i in range(len(metadata_labels)):
                f.write(metadata_labels[i] +
                        self.tab1.metadata_values[i].text() +
                        '\n')
            f.write('reference:\n')
            for i in range(len(reference_labels)):
                if i == 1:
                    auths = self.tab1.reference_values[1].text().split(', ')
                    f.write(reference_labels[i] + '\n')
                    for j in range(len(auths)):
                        f.write('        - name: ' +
                                auths[j] + '\n')
                else:
                    f.write(reference_labels[i] +
                            self.tab1.reference_values[i].text() +
                            '\n')
            # Write common properties
            f.write('experiment-type: ' + self.tab2.experiment_type.text() + '\n')
            f.write('apparatus:\n')
            f.write('    kind:  ' + self.tab2.apparatus_kind.text() + '\n')
            f.write('    institution: ' + self.tab2.apparatus_institution.text() + '\n')
            f.write('    facility: ' + self.tab2.apparatus_facility.text() + '\n')
            f.write('common-properties:\n    composition: &comp\n      kind: ')
            f.write(self.tab2.comp_kind.text() + '\n      species:')
            for i in range(len(self.tab2.species)):
                f.write('        - species-name: ' + self.tab2.species[i][0] +
                        '\n          InChI: ' + self.tab2.species[i][1] +
                        '\n          amount:\n            - ' + self.tab2.species[i][2] + '\n')
            f.write('    ignition-type:  &ign\n        target: ' + self.tab2.ignition_target.text() + '\n')
            f.write('        type: ' + self.tab2.ignition_type.text() + '\n')
            # Write datapoints
            # The nested for loop is probably unnecessary here
            f.write('datapoints:\n')
            for j in range(len(self.tab3.datapoints)):
                for i in range(len(datapoint_labels)):
                    if i == 0:
                        f.write(datapoint_labels[i]+'\n        - '+self.tab3.datapoints[j][i]+'\n')
                    elif i == 1:
                        f.write(datapoint_labels[i]+'\n        - '+self.tab3.datapoints[j][i]+'\n')
                    elif i == 2:
                        f.write(datapoint_labels[i]+'\n        - '+self.tab3.datapoints[j][i]+'\n')
                    elif i == 3 or i == 4:
                        f.write(datapoint_labels[i]+'\n')
                    elif i == 5:
                        f.write(datapoint_labels[i]+self.tab3.datapoints[j][3]+'\n')


def main():
    # Define application
    app = QApplication(sys.argv)

    # Define window (class displays window internally)
    gui = Window()

    # Close smoothly
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
