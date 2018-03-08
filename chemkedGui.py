import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QMessageBox, QAction,
                             QHBoxLayout, QVBoxLayout, QTabWidget,
                             QLabel, QLineEdit, QFormLayout,
                             QComboBox, QDesktopWidget, QGroupBox,
                             QFileDialog, QScrollArea)
from PyQt5.QtGui import QIcon
from pyked import __version__, chemked

# Start using PyQt
app = QApplication(sys.argv)

file = {
    'file-authors': [
        {'name': QLineEdit(),
         'ORCID': QLineEdit()}
    ],
    'file-version': QLineEdit(),
    'chemked-version': QLineEdit(__version__),
    'reference': {
        'doi': QLineEdit(),
        'authors': [
            {'name': QLineEdit(),
             'ORCID': QLineEdit()}
        ],
        'journal': QLineEdit(),
        'year': QLineEdit(),
        'volume': QLineEdit(),
        'pages': QLineEdit(),
        'detail': QLineEdit()
    },
    'experiment-type': QComboBox(),
    'apparatus': {
        'kind': QComboBox(),
        'institution': QLineEdit(),
        'facility': QLineEdit()
    },
    'datapoints': [
        {
            'temperature': QLineEdit(),
            'pressure': QLineEdit(),
            'ignition-delay': QLineEdit(),
            'equivalence-ratio': QLineEdit()
        }
    ],
    'common-properties': {
        'species': [
            {'species-name': QLineEdit(),
             'InChI': QLineEdit(),
             'amount': QLineEdit()}
        ],
        'kind': QComboBox(),
        'ignition-target': QLineEdit(),
        'ignition-type': QLineEdit()
    }
}

experiment_types = ['ignition delay']
for i in experiment_types:
    file['experiment-type'].addItem(i)

apparatus_kinds = ['rapid compression machine', 'shock tube']
for i in apparatus_kinds:
    file['apparatus']['kind'].addItem(i)

composition_kinds = ['mass fraction', 'mole fraction', 'mole percent']
for i in composition_kinds:
    file['common-properties']['kind'].addItem(i)


# noinspection PyArgumentList, PyUnresolvedReferences, PyCallByClass
class Window(QMainWindow):
    """Controls main window size, location, and menu bar.
    """

    def __init__(self):
        super(Window, self).__init__()
        title = 'ChemKED'
        self.left = 0
        self.top = 0
        self.width = 800
        self.height = 600
        self.setWindowTitle(title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('pyked-logo.png'))

        contents = Contents(self)
        self.setCentralWidget(contents)

        self.center()

        close_gui = QAction('&Close GUI', self)
        close_gui.setShortcut('Ctrl+Q')
        close_gui.triggered.connect(self.closeEvent)

    def center(self):
        """Centers the window on the screen.
        """
        fg = self.frameGeometry()
        av = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(av)
        self.move(fg.topLeft())

    def closeEvent(self, event):
        """Prompts the user before closing window.
        """
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# noinspection PyArgumentList, PyUnresolvedReferences
class Contents(QWidget):
    """Provides a widget which is the contents of
    the Window class. Widget contains 3 tabs, and
    an export button below them.

    Todo:
    - Move each tab's setup to it's own function
    """

    global file

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        btn_export = QPushButton('Export')
        btn_export.clicked.connect(self.export)

        # Tabs
        self.tabs = QTabWidget()

        # Tab Setup - File Metadata & References
        """
        This tab's layout is a QHBoxLayout.
        The layout contains 2 items:
            - Left: Metadata
            - Right: References
        """
        self.tab_meta = QWidget()
        hbox_tab_meta = QHBoxLayout()  # Tab layout

        """
        These buttons allow the user to add and remove
        file and reference authors.
        """
        btn_addFileAuthor = QPushButton('Add...')
        btn_remFileAuthor = QPushButton('Remove...')
        btn_addFileAuthor.clicked.connect(self.addFileAuthor)
        btn_remFileAuthor.clicked.connect(self.removeFileAuthor)
        hbox_metaBtns = QHBoxLayout()
        hbox_metaBtns.addWidget(QLabel('Author(s)'))
        hbox_metaBtns.addWidget(btn_addFileAuthor)
        hbox_metaBtns.addWidget(btn_remFileAuthor)

        btn_addRefAuthor = QPushButton('Add...')
        btn_remRefAuthor = QPushButton('Remove...')
        btn_addRefAuthor.clicked.connect(self.addRefAuthor)
        btn_remRefAuthor.clicked.connect(self.removeRefAuthor)
        hbox_refBtns = QHBoxLayout()
        hbox_refBtns.addWidget(QLabel('Author(s)'))
        hbox_refBtns.addWidget(btn_addRefAuthor)
        hbox_refBtns.addWidget(btn_remRefAuthor)

        """
        The QScrollArea is necessary because the user is
        not limited in the number of authors they add.
        Using a QScrollArea prevents the window from extending
        beyond the user's screen.
        """
        scrollAreaMeta = QScrollArea()
        scrollAreaMeta.setWidgetResizable(True)

        """
        Unfortunately, it seems like QScrollAreas don't
        play nice with QFormLayouts. QFormLayouts that
        require scrolling are first added to QGroupBoxes,
        which are then added to QScrollAreas. This works,
        but if the QGroupBoxes can be removed, it would
        reduce line count.
        
        This QFormLayout has rows pertaining to the 'Meta'
        section of the PyKED schema.
        """
        groupbox_meta = QGroupBox()
        self.form_meta = QFormLayout()

        self.form_meta.addRow(QLabel('File Metadata'))
        self.form_meta.addRow(QLabel('File Version'), file['file-version'])
        self.form_meta.addRow(QLabel('ChemKED Version'), file['chemked-version'])
        self.form_meta.addRow(QLabel(''))
        self.form_meta.addRow(hbox_metaBtns)
        self.form_meta.addRow(QLabel('Name'), file['file-authors'][0]['name'])
        self.form_meta.addRow(QLabel('ORCID'), file['file-authors'][0]['ORCID'])

        groupbox_meta.setLayout(self.form_meta)
        scrollAreaMeta.setWidget(groupbox_meta)

        """
        This QFormLayout has rows pertaining to the 'Reference'
        section of the PyKED schema.
        """
        scrollAreaRef = QScrollArea()
        scrollAreaRef.setWidgetResizable(True)
        groupbox_ref = QGroupBox()
        self.form_ref = QFormLayout()

        self.form_ref.addRow(QLabel('Reference Information'))
        self.form_ref.addRow(QLabel('DOI'), file['reference']['doi'])
        self.form_ref.addRow(QLabel('Journal'), file['reference']['journal'])
        self.form_ref.addRow(QLabel('Year'), file['reference']['year'])
        self.form_ref.addRow(QLabel('Volume'), file['reference']['volume'])
        self.form_ref.addRow(QLabel('Pages'), file['reference']['pages'])
        self.form_ref.addRow(QLabel('Detail'), file['reference']['detail'])
        self.form_ref.addRow(QLabel(''))
        self.form_ref.addRow(hbox_refBtns)
        self.form_ref.addRow(QLabel('Name'), file['reference']['authors'][0]['name'])
        self.form_ref.addRow(QLabel('ORCID'), file['reference']['authors'][0]['ORCID'])

        groupbox_ref.setLayout(self.form_ref)
        scrollAreaRef.setWidget(groupbox_ref)

        hbox_tab_meta.addWidget(scrollAreaMeta)
        hbox_tab_meta.addWidget(scrollAreaRef)
        self.tab_meta.setLayout(hbox_tab_meta)

        # Tab Setup - Experiment Info. & Common Properties
        """
        This tab's layout is a QHBoxLayout. The
        layout contains 2 items:
            - Left: Experiment/Apparatus/Ignition Info.
            - Right: Composition/Species/Common Properties
        """
        self.tab_comp = QWidget()
        hbox_tab_comp = QHBoxLayout()

        """
        These buttons allow the user to add and remove
        species fields to the common properties section
        of the tab (on the right).
        """

        btn_addSpecies = QPushButton('Add...')
        btn_remSpecies = QPushButton('Remove...')
        btn_addSpecies.clicked.connect(self.addSpecies)
        btn_remSpecies.clicked.connect(self.removeSpecies)
        hbox_speciesBtns = QHBoxLayout()
        hbox_speciesBtns.addWidget(QLabel('Species'))
        hbox_speciesBtns.addWidget(btn_addSpecies)
        hbox_speciesBtns.addWidget(btn_remSpecies)

        """
        The form_exp QFormLayout (left) contains data fields
        corresponding to the common properties.
        """
        form_exp = QFormLayout()
        form_exp.addRow(QLabel('Experiment Type'), file['experiment-type'])
        form_exp.addRow(QLabel(''))
        form_exp.addRow(QLabel('Apparatus Information'))
        form_exp.addRow(QLabel('Kind'), file['apparatus']['kind'])
        form_exp.addRow(QLabel('Institution'), file['apparatus']['institution'])
        form_exp.addRow(QLabel('Facility'), file['apparatus']['facility'])
        form_exp.addRow(QLabel(''))
        form_exp.addRow(QLabel('Ignition Information'))
        form_exp.addRow(QLabel('Target'), file['common-properties']['ignition-target'])
        form_exp.addRow(QLabel('Type'), file['common-properties']['ignition-type'])

        """
        The form_species QFormLayout contains fields for
        the common species. The user is able to add and
        remove as many species as they would like.
        """

        scrollAreaComp = QScrollArea()
        scrollAreaComp.setWidgetResizable(True)

        groupbox_comp = QGroupBox()
        self.form_species = QFormLayout()
        self.form_species.addRow(QLabel('Composition'), file['common-properties']['kind'])
        self.form_species.addRow(QLabel(''))
        self.form_species.addRow(hbox_speciesBtns)
        self.form_species.addRow(QLabel('Species 1'))
        self.form_species.addRow(QLabel('Name'), file['common-properties']['species'][0]['species-name'])
        self.form_species.addRow(QLabel('InChI'), file['common-properties']['species'][0]['InChI'])
        self.form_species.addRow(QLabel('Amount'), file['common-properties']['species'][0]['amount'])

        groupbox_comp.setLayout(self.form_species)
        scrollAreaComp.setWidget(groupbox_comp)

        hbox_tab_comp.addLayout(form_exp)
        hbox_tab_comp.addWidget(scrollAreaComp)
        self.tab_comp.setLayout(hbox_tab_comp)

        # Tab Setup - Datapoint-Specific Info.
        self.tab_data = QWidget()

        """
        The datapoints tab uses a QVBoxLayout, which contains 2 items:
            - Top: A QHBoxLayout containing:
                - The Add Datapoint Button
                - The Remove Datapoint Button
            - Bottom: A QFormLayout for datapoints
        """
        vbox_tab_data = QVBoxLayout()

        """
        These buttons allow the user to add/remove datapoint fields.
        """
        btn_addDataPoint = QPushButton('Add...')
        btn_addDataPoint.clicked.connect(self.addDatapoint)
        btn_remDataPoint = QPushButton('Remove...')
        btn_remDataPoint.clicked.connect(self.removeDatapoint)
        hbox_tab_data = QHBoxLayout()
        hbox_tab_data.addWidget(btn_addDataPoint)
        hbox_tab_data.addWidget(btn_remDataPoint)

        scrollAreaData = QScrollArea()
        scrollAreaData.setWidgetResizable(True)

        groupbox_data = QGroupBox()
        self.form_data = QFormLayout()
        self.form_data.addRow(QLabel('Datapoint 1'))
        self.form_data.addRow(QLabel('Temperature (K)'), file['datapoints'][0]['temperature'])
        self.form_data.addRow(QLabel('Pressure (atm)'), file['datapoints'][0]['pressure'])
        self.form_data.addRow(QLabel('Ignition Delay (us)'), file['datapoints'][0]['ignition-delay'])
        self.form_data.addRow(QLabel('Equivalence Ratio'), file['datapoints'][0]['equivalence-ratio'])

        groupbox_data.setLayout(self.form_data)
        scrollAreaData.setWidget(groupbox_data)
        vbox_tab_data.addLayout(hbox_tab_data)
        vbox_tab_data.addWidget(scrollAreaData)

        self.tab_data.setLayout(vbox_tab_data)

        # Export Button

        # Class Layout Composition
        self.tabs.addTab(self.tab_meta, 'File Metadata')
        self.tabs.addTab(self.tab_comp, 'Apparatus & Common Properties')
        self.tabs.addTab(self.tab_data, 'Datapoints')
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        layout.addWidget(btn_export)
        self.setLayout(layout)

    def addFileAuthor(self):
        file['file-authors'].append(
            {'name': QLineEdit(),
             'ORCID': QLineEdit()}
        )
        self.form_meta.addRow(QLabel('Name'), file['file-authors'][-1]['name'])
        self.form_meta.addRow(QLabel('ORCID'), file['file-authors'][-1]['ORCID'])

    def addRefAuthor(self):
        file['reference']['authors'].append(
            {'name': QLineEdit(),
             'ORCID': QLineEdit()}
        )
        self.form_ref.addRow(QLabel('Name'), file['reference']['authors'][-1]['name'])
        self.form_ref.addRow(QLabel('ORCID'), file['reference']['authors'][-1]['ORCID'])

    def addSpecies(self):
        new_species = {
            'species-name': QLineEdit(),
            'InChI': QLineEdit(),
            'amount': QLineEdit()
        }
        file['common-properties']['species'].append(new_species)
        j = len(file['common-properties']['species'])
        self.form_species.addRow(QLabel('Species ' + str(j)))
        self.form_species.addRow(QLabel('Name'), file['common-properties']['species'][-1]['species-name'])
        self.form_species.addRow(QLabel('InChI'), file['common-properties']['species'][-1]['InChI'])
        self.form_species.addRow(QLabel('Amount'), file['common-properties']['species'][-1]['amount'])

    def addDatapoint(self):
        new_datapoint = {
            'temperature': QLineEdit(),
            'pressure': QLineEdit(),
            'ignition-delay': QLineEdit(),
            'equivalence-ratio': QLineEdit()
        }
        file['datapoints'].append(new_datapoint)
        j = len(file['datapoints'])
        self.form_data.addRow(QLabel('Datapoint ' + str(j)))
        self.form_data.addRow(QLabel('Temperature (K)'), file['datapoints'][-1]['temperature'])
        self.form_data.addRow(QLabel('Pressure (atm)'), file['datapoints'][-1]['pressure'])
        self.form_data.addRow(QLabel('Ignition Delay (us)'), file['datapoints'][-1]['ignition-delay'])
        self.form_data.addRow(QLabel('Equivalence Ratio'), file['datapoints'][-1]['equivalence-ratio'])

    def removeFileAuthor(self):
        j = self.form_meta.rowCount() - 1
        if len(file['file-authors']) > 1:
            self.form_meta.removeRow(j)
            self.form_meta.removeRow(j-1)
            del file['file-authors'][-1]
        else:
            pass

    def removeRefAuthor(self):
        j = self.form_ref.rowCount() - 1
        if len(file['reference']['authors']) > 1:
            self.form_ref.removeRow(j)
            self.form_ref.removeRow(j-1)
            del file['reference']['authors'][-1]
        else:
            pass

    def removeSpecies(self):
        j = self.form_species.rowCount() - 1
        if len(file['common-properties']['species']) > 1:
            # Todo: make this a for loop
            self.form_species.removeRow(j)
            self.form_species.removeRow(j-1)
            self.form_species.removeRow(j-2)
            self.form_species.removeRow(j-3)
            del file['common-properties']['species'][-1]
        else:
            pass

    def removeDatapoint(self):
        j = self.form_data.rowCount() - 1
        if len(file['datapoints']) > 1:
            # Todo: make this a for loop
            self.form_data.removeRow(j)
            self.form_data.removeRow(j-1)
            self.form_data.removeRow(j-2)
            self.form_data.removeRow(j-3)
            self.form_data.removeRow(j-4)
            del file['datapoints'][-1]
        else:
            pass

    @staticmethod
    def export():
        """Takes the data stored in the forms within the
        GUI's tabs and stores the data in a dictionary.
        ChemKED takes the dictionary as an input and outputs
        a YAML file in the ChemKED format.
        """

        datapoints = []
        atts = ['temperature', 'pressure', 'ignition-delay', 'equivalence-ratio']
        for i in range(len(file['datapoints'])):
            datapoints.append({})
            for att in atts:
                datapoints[i][att] = [file['datapoints'][i][att].text()]
            datapoints[i]['composition'] = {}
            datapoints[i]['composition']['species'] = []
            for j in range(len(file['common-properties']['species'])):
                datapoints[i]['composition']['species'].append({})
                datapoints[i]['composition']['species'][j]['species-name'] = file['common-properties']['species'][j]['species-name'].text()
                datapoints[i]['composition']['species'][j]['InChI'] = file['common-properties']['species'][j]['InChI'].text()
                datapoints[i]['composition']['species'][j]['amount'] = [file['common-properties']['species'][j]['amount'].text()]
            datapoints[i]['composition']['kind'] = file['common-properties']['kind'].currentText()
            datapoints[i]['composition']['ignition-type'] = {'target': file['common-properties']['ignition-target'].text(),
                                                             'type': file['common-properties']['ignition-type'].text()}
        file_authors = [{'name': author['name'].text(), 'ORCID': author['ORCID'].text()} for author in file['file-authors']]
        for author in file_authors:
            if author['ORCID'] == '':
                del author['ORCID']
        ref_authors = [{'name': author['name'].text(), 'ORCID': author['ORCID'].text()} for author in file['reference']['authors']]
        for author in ref_authors:
            if author['ORCID'] == '':
                del author['ORCID']

        exported_file = {
            'file-version': file['file-version'].text(),
            'chemked-version': file['chemked-version'].text(),
            'file-authors': file_authors,
            'experiment-type': file['experiment-type'].currentText(),
            'reference': {
                'doi': file['reference']['doi'].text(),
                'authors': ref_authors,
                'journal': file['reference']['journal'].text(),
                'year': file['reference']['year'].text(),
                'volume': file['reference']['volume'].text(),
                'pages': file['reference']['pages'].text(),
                'detail': file['reference']['detail'].text()
            },
            'apparatus': {
                'kind': file['apparatus']['kind'].currentText(),
                'institution': file['apparatus']['institution'].text(),
                'facility': file['apparatus']['facility'].text(),
            },
            'datapoints': datapoints
        }

        exported = chemked.ChemKED(dict_input=exported_file, skip_validation=True)
        exported.write_file('testing.yaml', overwrite=True)


def main():
    gui = Window()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
