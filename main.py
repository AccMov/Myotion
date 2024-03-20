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
    QWidget, QFileDialog, QTableWidgetItem, QComboBox, QLineEdit, QCompleter,
    QCheckBox)

from rserver import RServer
import pyMotion as pm
from pyMotion import logger
from miscWidgets import *
from path import *

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
["UT-L", "UT-R", "MT-L", "MT-R", "LT-L", "LT-R", "AD-L", "AD-R", "MD-L", 
"MD-R", "PD-L", "PD-R", "PM-L", "PM-R", "LD-L", "LD-R", "BB-L", "BB-R", 
"TB-L", "TB-R", "BRD-L", "BRD-R", "ECRL-L", "ECRL-R", "ECRB-L", "ECRB-R", 
"ECU-L", "ECU-R", "ED-L", "ED-R", "EDM-L", "EDM-R", "EI-L", "EI-R", "FCR-L", 
"FCR-R", "PL-L", "PL-R", "FCU-L", "FCU-R", "FDS-L", "FDS-R", "FDP-L", "FDP-R", 
"FPL-L", "FPL-R", "SSP-L", "SSP-R", "ISP-L", "ISP-R", "SSC-L", "SSC-R", "TM-L",
"TM-R", "RA-L", "RA-R", "EO-L", "EO-R", "IO-L", "IO-R", "TA-L", "TA-R", "ES-L", 
"ES-R", "GM-L", "GM-R", "Gme-L", "Gme-R", "BF-L", "BF-R", "ST-L", "ST-R", 
"SM-L", "SM-R", "VL-L", "VL-R", "VM-L", "VM-R", "VI-L", "VI-R", "RF-L", 
"RF-R", "TA-L", "TA-R", "GM-L", "GM-R", "GL-L", "GL-R", "SOL-L", "SOL-R"],

["Trapezius (upper)-L", "Trapezius (upper)-R", "Trapezius (middle)-L", 
    "Trapezius (middle)-R", "Trapezius (lower)-L", "Trapezius (lower)-R",
    "Deltoid (anterior)-L", "Deltoid (anterior)-R", "Deltoid (middle)-L",
    "Deltoid (middle)-R", "Deltoid (posterior)-L", "Deltoid (posterior)-R", 
    "Pectoralis Major-L", "Pectoralis Major-R", "Latissimus Dorsi-L",
    "Latissimus Dorsi-R", "Biceps Brachii-L", "Biceps Brachii-R", "Triceps Brachii-L",
    "Triceps Brachii-R", "Brachioradialis-L", "Brachioradialis-R", 
    "Extensor Carpi Radialis Longus-L", "Extensor Carpi Radialis Longus-R",
    "Extensor Carpi Radialis Brevis-L", "Extensor Carpi Radialis Brevis-R", 
    "Extensor Carpi Ulnaris-L", "Extensor Carpi Ulnaris-R", "Extensor Digitorum-L",
    "Extensor Digitorum-R", "Extensor Digiti Minimi-L", "Extensor Digiti Minimi-R",
    "Extensor Indicis-L", "Extensor Indicis-R", "Flexor Carpi Radialis-L",
    "Flexor Carpi Radialis-R", "Palmaris Longus-L", "Palmaris Longus-R",
    "Flexor Carpi Ulnaris-L", "Flexor Carpi Ulnaris-R", "Flexor Digitorum Superficialis-L",
    "Flexor Digitorum Superficialis-R", "Flexor Digitorum Profundus-L",
    "Flexor Digitorum Profundus-R", "Flexor Pollicis Longus-L", "Flexor Pollicis Longus-R",
    "Supraspinatus-L", "Supraspinatus-R", "Infraspinatus-L", "Infraspinatus-R", 
    "Subscapularis-L", "Subscapularis-R", "Teres Major-L", "Teres Major-R",
    "Rectus Abdominis-L", "Rectus Abdominis-R", "External Oblique-L", "External Oblique-R",
    "Internal Oblique-L", "Internal Oblique-R", "Transversus Abdominis-L", 
    "Transversus Abdominis-R", "Erector Spinae-L", "Erector Spinae-R", "Gluteus Maximus-L",
    "Gluteus Maximus-R", "Gluteus Medius-L", "Gluteus Medius-R", "Biceps Femoris-L", 
    "Biceps Femoris-R", "Semitendinosus-L", "Semitendinosus-R", "Semimembranosus-L", 
    "Semimembranosus-R", "Vastus Lateralis-L", "Vastus Lateralis-R", "Vastus Medialis-L",
    "Vastus Medialis-R", "Vastus Intermedius-L", "Vastus Intermedius-R", "Rectus Femoris-L",
    "Rectus Femoris-R", "Tibialis Anterior-L", "Tibialis Anterior-R", "Gastrocnemius (medial head)-L",
    "Gastrocnemius (medial head)-R", "Gastrocnemius (lateral head)-L", "Gastrocnemius (lateral head)-R", "Soleus-L", "Soleus-R"]]


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
        self.widgets.tableWidget.setColumnWidth(1, w * 0.3)
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
        comboBox.addItems(joint_name[1])
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
        for old, new in self.formalizedName.items():
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
        widgets.pushButton_11.clicked.connect(self.singleEMGButtonClick)
        widgets.listWidget.itemDoubleClicked.connect(self.EMGConfigurationListDoubleClicked)
        widgets.checkBox_4.stateChanged.connect(self.EMGConfigureToggleDCOffset)
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.showMaximized()

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
        self.selectedParticipants = []       # selected participants
        self.singleEMG = (None, None, None)  # Participant, Steps, channel
        self.inputBuffer = None
        self.outputBuffer = None
        self.batchEMG = (None, None)         # Participant list, configure file

        self.test()

    def test(self):
        self.newWorkSpace(MyotionPath, 'test')
        f = os.getcwd() + '/ERRPT.c3d'
        emg = pm.emg(f)

        # add people
        p1 = pm.person("Guo Chen", "1995/08/05", 'male')

        # add data
        self.workspace.addParticipant(p1, emg)

        self.updateEMGParticipantBox()
        self.updateWorkSpaceParticipantBox()

        #////// test
        '''
        a = pm.c3dFile(f)
        b = a.analog.convertToTST()
        channel = 'Fx1'

        widgets.plot_input.line(b, channel)
        widgets.plot_input.show()

        b[channel] = b.rectification(channel)

        widgets.plot_output.line(b, channel)
        widgets.plot_output.show()
        '''

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

        # add to workspace
        self.workspace.addParticipant(p, emgdata)

        # update UI
        self.updateEMGParticipantBox()
        self.updateWorkSpaceParticipantBox()

    def newProjectButtonClick(self):
        dir = QFileDialog.getExistingDirectory(None, 'New Project', self.home, 
                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        if dir == '':
            return
        
        if not checkValidPath(dir):
            QMessageBox.critical(None, 'error', 'Selected path does not exist!', QMessageBox.Ok)

        p = Path(dir)
        if self.newWorkSpace(p, p.name):
            QMessageBox.critical(None, 'error', 'Failed to create new Workspace!', QMessageBox.Ok)
        
        logger.info('workspace path: {}'.format(self.home))
        logger.info('workspace name: {}'.format(self.workspace.name))

    def singleEMGButtonClick(self):

        if len(self.selectedParticipants) == 0:
            QMessageBox.critical(None, 'error', 'No participant selected!', QMessageBox.Ok)
            return
        
        if len(self.selectedParticipants) > 1:
            QMessageBox.critical(None, 'error', 'Only one participant can be selected!', QMessageBox.Ok)
            return
        
        if self.singleEMG[0] is not None:
            QMessageBox.critical(None, 'error', 'Current EMG process is not finished!', QMessageBox.Ok)
            return

        p_key = self.selectedParticipants[0]

        #deselect checkbox
        chbox = widgets.tableWidget_2.findChild(QCheckBox, p_key)
        chbox.stateChanged.emit(False)

        p = self.workspace.findParticipant(int(p_key))
        self.startSingleEMGProcess(p)

    def participantCheckBoxChanged(self, state):
        sender = self.sender()
        p = sender.objectName()

        if state:
            self.selectedParticipants.append(p)
        else:
            self.selectedParticipants.remove(p)

    def EMGConfigurationListDoubleClicked(self, item):
        curr = widgets.listWidget.currentRow()
        if curr == self.singleEMG[1]:
            return
        p, step, chan = self.singleEMG
        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        
        idx = widgets.listWidget.currentRow()
        type, str = cfg.getTypeInfo(idx)
        self.updateEMGToolBox(type)
        self.selectSingleEMGStep(widgets.listWidget.currentRow())

    def EMGConfigureToggleDCOffset(self, state):
        p, step, chan = self.singleEMG
        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        if cfg[step].enable == state:
            return
        
        cfg[step].enable = state
        self.outputBuffer = self.workspace[p].emg.tryConfigStepTo(chan, step)
        self.updateSignalProcessPanel(up=False)

    # WIDGET
    # //////////////////////////////////////////////////////////////
    def createParticipantCheckBox(self, name):
        checkbox = QCheckBox(widgets.tableWidget_2)
        checkbox.setObjectName(name)
        checkbox.stateChanged.connect(self.participantCheckBoxChanged)
        return checkbox

    def createHBox(self, w, parent=None):
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.addWidget(w, alignment=Qt.AlignHCenter)
        w.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        return container

    # UPDATE UI EVENTS
    # //////////////////////////////////////////////////////////////
    def updateEMGParticipantBox(self):
        participants = self.workspace.getParticipants()
        n = len(participants)
        widgets.tableWidget_2.clearContents()
        widgets.tableWidget_2.setRowCount(n)
        for i in range(0, n):
            p = participants[i]
            name = p.name
            # checkbox
            chb = self.createParticipantCheckBox(str(p.key()))
            widgets.tableWidget_2.setCellWidget(i, 0, chb)
            # name
            q = QTableWidgetItem(name)
            q.setTextAlignment(Qt.AlignCenter)
            widgets.tableWidget_2.setItem(i, 1, q)
            # status
            h = widgets.tableWidget_2.rowHeight(i)
            col2w = widgets.tableWidget_2.columnWidth(2)
            col3w = widgets.tableWidget_2.columnWidth(3)
            ready = statusLED(col2w, h, self.workspace[p].isEMGReady())
            report = statusLED(col3w, h, self.workspace[p].isReportReady())
            widgets.tableWidget_2.setCellWidget(i, 2, ready)
            widgets.tableWidget_2.setCellWidget(i, 3, report)

    def updateWorkSpaceParticipantBox(self):
        #listwidget_3
        participants = self.workspace.getParticipants()
        n = len(participants)
        widgets.listWidget_3.clear()
        for i in range(0, n):
            p = participants[i]
            name = p.name
            # name
            widgets.listWidget_3.addItem(name)
            widgets.listWidget_3.item(i).setForeground(Qt.black)

    # update waveform regarding to config step and user input metrics
    def updateSignalProcessPanel(self, up = True, down = True):       
        p, step, chan = self.singleEMG

        if p is None:
            widgets.plot_input.hide()
            widgets.plot_output.hide()
            return

        x = self.workspace[p].emg.getLinspace()
        # push data to plot
        if up:
            widgets.plot_input.line(x, self.inputBuffer, chan)
            widgets.plot_input.show()
        if down:
            widgets.plot_output.line(x, self.outputBuffer, chan)
            widgets.plot_output.show()
    
    def updateEMGConfigureList(self):
        widgets.listWidget.clear()

        if self.workspace is None:
            return
        p = self.singleEMG[0]
        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        cfgstrings = cfg.getStepStringList()
        # update configuration list
        n = len(cfgstrings)
        widgets.listWidget.clear()
        widgets.listWidget.setSortingEnabled(False)
        for i in range(0, n):
            widgets.listWidget.addItem(cfgstrings[i])
            widgets.listWidget.item(i).setForeground(Qt.black)

    def updateEMGToolBox(self, type):
        type2toolbox = {
            pm.emgConfigureEnum.DC_OFFSET : 0,
            pm.emgConfigureEnum.FULL_W_RECT : 1,
            pm.emgConfigureEnum.FILTER : 2,
            pm.emgConfigureEnum.NORMALIZATION : 3,
            pm.emgConfigureEnum.ACTIVATION : 4,
            pm.emgConfigureEnum.SUMMARY : 5,
        }
        print(type2toolbox[type])
        widgets.toolBox.setCurrentIndex(type2toolbox[type])

    # Application Logic/Slots
    # ///////////////////////////////////////////////////////////////
    def newWorkSpace(self, fpath, name=''):
        if self.workspace is not None:
            self.saveWorkSpace()
            self.workspace.clear()

        # create new project
        self.workspace = pm.workspace(name)
        
        self.home = str(fpath)

        # clear GUI
        self.updateSignalProcessPanel()
        self.updateEMGConfigureList()
        self.updateEMGParticipantBox()
        self.updateWorkSpaceParticipantBox()
        return 0
    
    def saveWorkSpace(self):
        return
    
    def startSingleEMGProcess(self, p):
        logger.info("started single EMG process for {}".format(p.name))
        if not self.workspace.hasParticipant(p):
            return -1
        
        # set fsm
        self.singleEMG = (p, 0, self.workspace[p].emg.getChannels()[0])
        self.workspace[p].emg.startProcess()
        self.updateEMGConfigureList()
        self.selectSingleEMGStep(0)
        
    def selectSingleEMGStep(self, idx):
        p, step, chan = self.singleEMG

        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        cfgstrings = cfg.getStepStringList()
        
        if idx > len(cfgstrings):
            logger.info("single EMG process idx {} out of range".format(idx))

        logger.info("selecting EMG process step {}, {}".format(idx, cfgstrings[idx]))
        self.singleEMG = (p, idx, chan)
        if idx == 0:
            self.inputBuffer = self.workspace[p].emg[chan]
        else:
            self.inputBuffer  = self.workspace[p].emg.tryConfigStepTo(chan, idx - 1)
        self.outputBuffer = self.workspace[p].emg.tryConfigStepTo(chan, idx)

        # select index for EMG config widget
        widgets.listWidget.setCurrentRow(idx)
        # update UI
        self.updateSignalProcessPanel()
        type, str = cfg.getTypeInfo(idx)
        self.updateEMGToolBox(type)
        
    def startBatchEMGProcess(self, listofpeople, nameofconfig):
        for p in listofpeople:
            if not self.workspace.hasPerson(p):
                return -1
        
        if not self.workspace.hasConfigFile(nameofconfig):
            return -1
    
if __name__ == "__main__":
    qApp = QApplication(sys.argv)
    qApp.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    qApp.exec_()
    window.rserver.join()
    sys.exit(0)
