# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
from rserver import RServer
import pyMotion as pm
from pyMotion import logger
from  pathlib import Path
import re
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTimer, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar, QMessageBox, QDialog,
    QWidget, QFileDialog, QTableWidgetItem, QComboBox, QLineEdit, QCompleter)

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

# Global Constant
# ///////////////////////////////////////////////////////////////
joint_name = [
['UT', 'MT', 'LT', 'AD', 'MD', 'PD', 'PM', 'LD', 'BB', 
'TB', 'BRD', 'ECRL', 'ECRB', 'ECU', 'ED', 'EDM', 'EI', 
 'FCR', 'PL', 'FCU', 'FDS', 'FDP', 'FPL', 'SSP', 'ISP', 
'SSC', 'TM', 'RA', 'EO', 'IO', 'TA', 'ES', 'GM', 'Gme', 
'BF', 'ST', 'SM', 'VL', 'VM', 'VI', 'RF', 'TA', 'GM', 'GL', 'SOL'],

['Trapezius (upper)', 'Trapezius (middle)', 'Trapezius (lower)', 'Deltoid (anterior)', 
 'Deltoid (middle)', 'Deltoid (posterior)', 'Pectoralis Major', 'Latissimus Dorsi', 
 'Biceps Brachii', 'Triceps Brachii', 'Brachioradialis', 'Extensor Carpi Radialis Longus', 
 'Extensor Carpi Radialis Brevis', 'Extensor Carpi Ulnaris', 'Extensor Digitorum', 
 'Extensor Digiti Minimi', 'Extensor Indicis', 'Flexor Carpi Radialis', 'Palmaris Longus',
 'Flexor Carpi Ulnaris', 'Flexor Digitorum Superficialis', 'Flexor Digitorum Profundus', 
 'Flexor Pollicis Longus', 'Supraspinatus', 'Infraspinatus', 'Subscapularis', 'Teres Major', 
 'Rectus Abdominis', 'External Oblique', 'Internal Oblique', 'Transversus Abdominis', 'Erector Spinae',
 'Gluteus Maximus', 'Gluteus Medius', 'Biceps Femoris', 'Semitendinosus', 'Semimembranosus', 
 'Vastus Lateralis', 'Vastus Medialis', 'Vastus Intermedius', 'Rectus Femoris', 'Tibialis Anterior',
 'Gastrocnemius (medial head)', 'Gastrocnemius (lateral head)', 'Soleus']]

def checkValidPath(fpath):
    return os.path.exists(fpath)

class EMGAddWindow(QDialog):
    def __init__(self, root, width, height, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.resize(width, height)
        self.setWindowTitle('Add EMG File')

        self.widgets = self.ui
        self.root = root
        self.emg = None
        self.person = None
        self.channels = []
        self.mvcfiles = {}
        self.formalizedName = {}

        self.widgets.import_btn.clicked.connect(self.importEMGBtnClicked)
        self.widgets.lineEdit.textChanged.connect(self.updateFilterText)
        self.widgets.import_btn_2.clicked.connect(self.confirmBtnClicked)
        self.widgets.import_btn_3.clicked.connect(self.cancelBtnClicked)

    def run(self):
        self.exec()
        return self.person, self.emg
    
    # update emg and mvc qtablewidget
    def updateChannelBox(self):
        self.widgets.tableWidget.clearContents()
        # column width
        w = self.frameGeometry().width()
        # fixed ratio
        self.widgets.tableWidget.setColumnWidth(1, w * 0.1)
        self.widgets.tableWidget.setColumnWidth(2, w * 0.4)
        self.widgets.tableWidget.setColumnWidth(3, w * 0.1)

        n = len(self.channels)
        self.widgets.tableWidget.setRowCount(n)
        for i in range(0, n):
            chan = self.channels[i]
            q = QTableWidgetItem(chan)
            q.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
            q.setFlags(q.flags() ^ Qt.ItemIsEditable)
            self.widgets.tableWidget.setItem(i, 0, q)
            # drop down selection
            self.widgets.tableWidget.setCellWidget(i, 1, self.jointComboBox(chan))
            # mvc file path
            p = ""
            if chan in self.mvcfiles:
                p = self.mvcfiles[chan]
            self.widgets.tableWidget.setCellWidget(i, 2, self.mvcFileDisplay(p))
            # buttons for mvc file
            self.widgets.tableWidget.setCellWidget(i, 3, self.mvcFileButton(chan))

        self.widgets.tableWidget.resizeColumnToContents(0)
    
    def jointComboBox(self, chan):
        comboBox = QComboBox()
        comboBox.setObjectName(chan)
        comboBox.addItems(joint_name[0])
        comboBox.currentIndexChanged.connect(self.jointBoxChanged)
        return comboBox
    
    def mvcFileButton(self, chan):
        btn = QPushButton()
        btn.setText('select file')
        btn.setObjectName(chan)
        btn.setStyleSheet(u"color:#f4f4f4;\n"
        "background-color: #333b46;\n"
        "padding:8px 8px;\n"
        "border-radius:8px;")
        btn.clicked.connect(self.importMVCBtnClicked)
        return btn

    def mvcFileDisplay(self, str):
        line = QLineEdit()
        line.setReadOnly(True)
        line.setText(str)
        return line

    # SIGNALS AND SLOT
    ################################################
    def jointBoxChanged(self, index):
        jointbox = self.sender()
        chan = jointbox.objectName()
        self.formalizedName[chan] = joint_name[0][index]

    def updateFilterText(self):
        filter_str = self.widgets.lineEdit.text()
        if filter_str == "":
            filter_str = '.*'
        
        # check valid regex string
        try:
            re.compile(filter_str)
        except re.error:
            print('regex not valid')
            return
            
        self.channels = self.emg.searchChannels(filter_str)
        self.updateChannelBox()

    def importEMGBtnClicked(self):
        # load EMG file
        file, extension = QFileDialog.getOpenFileName(None, caption = 'open EMG file', dir = self.root, filter = "EMG Files (*.c3d *.mat)")

        if not checkValidPath(file):
            return
        
        # open up emg file
        try:
            self.emg = pm.emg(file)
        except Exception:
            QMessageBox.critical(None, 'error', 'Selected emg file is invalid!', QMessageBox.Ok)
            return
        
        # get channels and update list
        self.channels = self.emg.getChannels()

        self.widgets.label_3.setText(file)
        self.updateChannelBox()

    def importMVCBtnClicked(self):
        btn = self.sender()
        chan = btn.objectName()
        file, extension = QFileDialog.getOpenFileName(None, caption = 'open MVC file', dir = self.root, filter = "EMG Files (*.c3d *.mat)")

        if not checkValidPath(file):
            return
        try:
            self.emg.setMVCFile(chan, file) 
        except Exception:
            QMessageBox.critical(None, 'error', 'Selected mvc file is invalid!', QMessageBox.Ok)
            return
        self.mvcfiles[chan] = file
        self.updateChannelBox()

    def sanity(self):
        if self.emg is None:
            QMessageBox.critical(None, 'error', 'No EMG file selected!', QMessageBox.Ok)
            return False
        if not self.emg.isMVCComplete():
            QMessageBox.critical(None, 'error', 'MVC file not complete!', QMessageBox.Ok)
            return False
        names = set()
        for old, new in self.formalizedName:
            if new in names:
                QMessageBox.critical(None, 'error', 'Duplicated joint name found, please assign each channel to joints properly!', QMessageBox.Ok)
                return False
            names.add(new)
        return True
        
    def confirmBtnClicked(self):
        #if not self.sanity():
        #    return
        
        # creat person
        name = self.widgets.lineEdit_3.text()
        self.person = pm.person(name, 'N/A', 'N/A')
        # filter and rename channels
        old = self.emg.getChannels()
        for c in old:
            if c not in self.channels:
                self.emg.removeChannel(c)
        for old, new in self.formalizedName:
            self.emg.renameChannel(old, new)
        self.close()
    
    def cancelBtnClicked(self):
        self.person = None
        self.emg = None
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Launch R server
        self.rserver = RServer()
        self.rserver.start()

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = False

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "MYOTION"
        description = "MYOTION"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_start.clicked.connect(self.buttonClick)
        widgets.btn_emg.clicked.connect(self.buttonClick)
        widgets.btn_kinematic.clicked.connect(self.buttonClick)
        widgets.btn_frequency.clicked.connect(self.buttonClick)
        widgets.btn_advanced.clicked.connect(self.buttonClick)
        widgets.btn_stats.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # Project
        widgets.btn_new.clicked.connect(self.newProjectButtonClick)

        # EMG Page
        widgets.pushButton_10.clicked.connect(self.addEMGButtonClick)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.showMaximized()
        #self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "D:/Myotion/themes/py_dracula_test.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.start_page)
        widgets.btn_start.setStyleSheet(UIFunctions.selectMenu(widgets.btn_start.styleSheet()))

        # APPLICATION LOGICS
        self.workspace = None                # workspace (participant list, emg list, reports, configure file list and etc.)
        self.home = None                     # current project path
        self.participants = {}               # particpate list, person:emg
        self.singleEMG = (None, None)        # Participant, Steps
        self.batchEMG = (None, None)         # Participant list, configure file

        #self.test()

    def test(self):
        self.newWorkSpace('D:/Myotion/test', 'testProject')

        # add people
        p1 = pm.person("Guo Chen", "1995/08/05", 'male')
        self.participants.append(p1)

        f = os.getcwd() + '/ERRPT.c3d'
        # add data
        self.workspace.addparticipant(p1, f)

        self.updateparticipantBox()

        #////// test
        a = pm.c3dFile(f)
        b = a.analog.convertToTST()
        channel = 'Fx1'

        widgets.plot_input.line(b, channel)
        widgets.plot_input.show()

        b[channel] = b.rectification(channel)

        widgets.plot_output.line(b, channel)
        widgets.plot_output.show()

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW START PAGE
        if btnName == "btn_start":
            widgets.stackedWidget.setCurrentWidget(widgets.start_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW EMG PAGE
        if btnName == "btn_emg":
            widgets.stackedWidget.setCurrentWidget(widgets.emg_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW STATS PAGE
        if btnName == "btn_stats":
            widgets.stackedWidget.setCurrentWidget(widgets.stats_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # //////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def addEMGButtonClick(self):
        # create person
        p, emgdata = EMGAddWindow(self.home, 1200, 800).run()
        logger.info('added participate {}'.format(p.name))
        # add to list
        self.participants[p] = emgdata

        # update UI
        self.updateparticipantBox()

    def newProjectButtonClick(self):
        dir = QFileDialog.getExistingDirectory(None, 'New Project', self.home, 
                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        
        if not checkValidPath(dir):
            QMessageBox.critical(None, 'error', 'Selected path does not exist!', QMessageBox.Ok)

        p = Path(dir)
        if self.newWorkSpace(p, p.name):
            QMessageBox.critical(None, 'error', 'Failed to create new Workspace!', QMessageBox.Ok)
        
        logger.info('workspace path: {}'.format(self.home))
        logger.info('workspace name: {}'.format(self.workspace.name))

    # UPDATE UI EVENTS
    # //////////////////////////////////////////////////////////////
    def updateparticipantBox(self):
        # emg panel
        n = len(self.participants)
        print(n)
        widgets.tableWidget_2.setRowCount(n)
        i = 0
        for p, emg in self.participants.items():
            q = QTableWidgetItem(p.name)
            q.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
            widgets.tableWidget_2.setItem(i, 1, q)
            i = i + 1

    # Application Logic
    # ///////////////////////////////////////////////////////////////
    def newWorkSpace(self, fpath, name=''):
        if self.workspace is not None:
            self.saveWorkSpace()
            self.workspace.clear()
            self.updateparticipantTable()
        
        # create new project
        self.workspace = pm.workspace(name)
        
        self.home = str(fpath)
        return 0
    
    def saveWorkSpace(self):
        return
    
    
    def addSingleEMGFile(self, fpath):
        if checkValidPath(fpath):
            #error
            return -1
        
        # add sub window, blocking

        self.updateparticipantTable()
        return 0
    
    def startSingleEMGProcess(self, nameofperson):
        if not self.workspace.hasPerson(nameofperson):
            return -1
        
    def startBatchEMGProcess(self, listofpeople, nameofconfig):
        for p in listofpeople:
            if not self.workspace.hasPerson(p):
                return -1
        
        if not self.workspace.hasConfigFile(nameofconfig):
            return -1
    
    # update widget of participant table
    def updateparticipantTable(self):
        
        return
    
    # update waveform regarding to config step and user input metrics
    def updateWaveFormTable(self, configName):
        return
    
if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    qApp.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    qApp.exec_()
    window.rserver.join()
    sys.exit(0)
