"""
This program creates a GUI for exporting combustion
experiment data to a YAML file in the ChemKED format.
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QMessageBox, QAction,
                             QToolTip, QDesktopWidget, QSpinBox,
                             QHBoxLayout, QVBoxLayout, QTabWidget,
                             QSplashScreen, QLabel, QLineEdit,
                             QFormLayout, QGroupBox, QScrollArea)
# from PyQt5.QtGui import *


class Window(QMainWindow):
    """
    Controls main window handling.
    """
    def __init__(self):
        super(Window, self).__init__()

        self.title = 'Prototype ChemKED GUI'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setWindowIcon(QIcon('pyked-logo.png'))

        self.tabs_widget = Tabs(self)
        self.setCentralWidget(self.tabs_widget)

        self.center()

        close_gui = QAction("&Close GUI", self)
        close_gui.setShortcut('Ctrl+Q')
        close_gui.setStatusTip('Close without saving.')
        close_gui.triggered.connect(self.closeEvent)

        self.show()


    def center(self):
        """
        Centers the window on the screen.
        """
        fg = self.frameGeometry()
        av = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(av)
        self.move(fg.topLeft())


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


class Tabs(QWidget):
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

        self.tabs = QTabWidget()
        self.tab_meta = self.tab_meta_setup()
        self.tab_comp = self.tab_comp_setup()
        self.tab_data = self.tab_data_setup()
        # self.tabs.resize(300, 200)

        # Add tabs to vbox
        self.tabs.addTab(self.tab_meta, "Metadata")
        self.tabs.addTab(self.tab_comp, "Experiment")
        self.tabs.addTab(self.tab_data, "Datapoints")

        # Add vbox to instantiation
        self.layout.addWidget(self.tabs)
        # self.layout.addWidget(self.export_button)
        self.setLayout(self.layout)

        # self.export_button.clicked.connect(self.export)

    def tab_meta_setup(self):
        tab = QWidget()
        return tab

    def tab_comp_setup(self):
        tab = QWidget()
        return tab

    def tab_data_setup(self):
        tab = QWidget()
        return tab

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
            f.write(self.tab2.comp_kind.text() + '\n      species:\n')
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
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
