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
    QMetaObject, QObject, QPoint, QRect, QDir,
    QSize, QTimer, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar, QMessageBox, QDialog,
    QWidget, QFileDialog, QTableWidgetItem, QComboBox, QLineEdit, QCompleter,
    QCheckBox, QFileSystemModel )

from rserver import RServer
from miscWidgets import *
from path import *

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
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
        self.mvcfiles = []
        self.mvcfilesMap = {}
        self.formalizedName = {}

        self.widgets.import_btn.clicked.connect(self.importEMGBtnClicked)
        self.widgets.lineEdit.textChanged.connect(self.updateFilterText)
        self.widgets.import_btn_2.clicked.connect(self.confirmBtnClicked)
        self.widgets.import_btn_3.clicked.connect(self.cancelBtnClicked)
        self.widgets.importMVC_btn.clicked.connect(self.importMVCBtnClicked)

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
            self.widgets.tableWidget.setCellWidget(i, 2, self.mvcFileDisplay(chan))

        self.widgets.tableWidget.resizeColumnToContents(0)
    
    def jointComboBox(self, chan):
        comboBox = QComboBox()
        comboBox.setObjectName(chan)
        comboBox.addItems(joint_name[1])
        if chan in self.formalizedName:
            comboBox.setCurrentText(self.formalizedName[chan])
        else:
            comboBox.setCurrentIndex(0)
        comboBox.currentIndexChanged.connect(self.jointBoxChanged)
        return comboBox
    
    '''
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
    '''

    def mvcFileDisplay(self, chan):
        comboBox = QComboBox()
        comboBox.setObjectName(chan)

        # only display  file name instead of full path
        for f in self.mvcfiles:
            comboBox.addItem(os.path.basename(f))
        if chan in self.mvcfilesMap:
            comboBox.setCurrentIndex(self.mvcfilesMap[chan])
        else:
            comboBox.setCurrentIndex(-1)
        comboBox.currentIndexChanged.connect(self.MVCFilesChanged)
        return comboBox

    # SIGNALS AND SLOT
    ################################################
    def jointBoxChanged(self, index):
        jointbox = self.sender()
        chan = jointbox.objectName()
        self.formalizedName[chan] = joint_name[0][index]

    def MVCFilesChanged(self, index):
        mvcBox = self.sender()
        chan = mvcBox.objectName()
        self.mvcfilesMap[chan] = index
        # apply MVC
        try:
            self.emg.setMVCFile(chan, self.mvcfiles[index]) 
        except Exception:
            QMessageBox.critical(None, 'error', 'Selected mvc file is invalid!', QMessageBox.Ok)
            return

    def updateFilterText(self):
        filter_str = self.widgets.lineEdit.text()
        if filter_str == "":
            filter_str = '.*'
        
        # check valid regex string
        try:
            re.compile(filter_str)
        except re.error:
            logger.error('regex not valid')
            return
            
        self.channels = self.emg.searchChannels(filter_str)
        self.updateChannelBox()

    def importEMGBtnClicked(self):
        # load EMG file
        file, extension = QFileDialog.getOpenFileName(None, caption = 'open EMG file', dir = self.root, filter = "EMG Files (*.c3d *.mat)")
        
        # open up emg MVC file
        try:
            self.emg = emg(file)
        except Exception:
            QMessageBox.critical(None, 'error', 'Selected emg file is invalid!', QMessageBox.Ok)
            return
        
        # get channels and update list
        self.channels = self.emg.getChannels()

        self.widgets.label_3.setText(file)
        self.updateChannelBox()

    def importMVCBtnClicked(self):
        if len(self.channels) == 0:
            QMessageBox.critical(None, 'error', 'Please select emg file before MVC file!', QMessageBox.Ok)
            return

        btn = self.sender()
        chan = btn.objectName()

        files, extension = QFileDialog.getOpenFileNames(None, caption = 'open MVC file', dir = self.root, filter = "EMG Files (*.c3d *.mat)")

        # clear old, set new val
        self.mvcfilesMap.clear()
        self.mvcfiles = files
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
        self.person = person(name, 'N/A', 'N/A')

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
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

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
        widgets.checkBox_4.stateChanged.connect(self.EMGConfigureToggleConfiguration)
        widgets.checkBox_11.stateChanged.connect(self.EMGConfigureToggleConfiguration)
        widgets.checkBox_12.stateChanged.connect(self.EMGConfigureToggleConfiguration)
        widgets.checkBox_13.stateChanged.connect(self.EMGConfigureToggleConfiguration)
        widgets.comboBox_2.currentIndexChanged.connect(self.EMGChannelSelectorIndexChanged)
        widgets.toolBox.currentChanged.connect(self.EMGChannelToolBoxIndexChanged)
        widgets.pushButton_19.clicked.connect(self.EMGStepNextButtonClicked)
        widgets.pushButton_20.clicked.connect(self.EMGStepNextButtonClicked)
        widgets.pushButton_21.clicked.connect(self.EMGConfigureFilterConfiguration)
        widgets.pushButton_22.clicked.connect(self.EMGStepNextButtonClicked)
        widgets.pushButton_23.clicked.connect(self.EMGStepNextButtonClicked)
        widgets.pushButton_25.clicked.connect(self.EMGStepNextButtonClicked)
        widgets.pushButton_26.clicked.connect(self.EMGGenerateReportButtonClicked)
        widgets.pushButton_27.clicked.connect(self.EMGSaveConfigurationButtonClicked)
        widgets.pushButton_12.clicked.connect(self.EMGBatchProcessButtonClicked)
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
        widgets.btn_start.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_start.styleSheet())
        )

        # APPLICATION LOGICS
        self.workspace = None                # workspace (participant list, emg list, reports, configure file list and etc.)
        self.home = None                     # current project path
        self.filesystemTree = QFileSystemModel()
        self.selectedParticipants = []       # key of selected participants
        self.singleEMG = (None, None, None)  # Participant, Steps, channel
        self.inputBuffer = None
        self.outputBuffer = None
        #self.test()

    def test(self):
        self.newWorkSpace("D:\\test\\myotion", 'test')
        f = "D:\\test\\myotion\\lifting+bending\\Normal\\caoshaoying\\2021-11-04-19-11_lift.mat"
        memg = emg(f)

        # add people
        p1 = person("Guo Chen", "1995/08/05", 'male')

        # add data
        self.workspace.addParticipant(p1, memg)

        self.updateEMGParticipantBox()
        self.updateWorkSpaceParticipantBox()

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
            widgets.stackedWidget.setCurrentWidget(widgets.stats_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        if btnName == "btn_kinematic":
            widgets.stackedWidget.setCurrentWidget(widgets.kinematics_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            return

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
            print("Mouse click: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            print("Mouse click: RIGHT CLICK")

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

        # Jump to EMG page
        widgets.stackedWidget.setCurrentWidget(widgets.emg_page)

    def singleEMGButtonClick(self):
        p, step, chan = self.singleEMG
        
        if len(self.selectedParticipants) == 0:
            QMessageBox.critical(None, 'error', 'No participant selected!', QMessageBox.Ok)
            return
        
        if len(self.selectedParticipants) > 1:
            QMessageBox.critical(None, 'error', 'Only one participant can be selected!', QMessageBox.Ok)
            return
        
        if p is not None:
            QMessageBox.critical(None, 'error', 'Current EMG process is not finished!', QMessageBox.Ok)
            return

        p_key = self.selectedParticipants[0]

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
        self.selectSingleEMGStep(widgets.listWidget.currentRow())
        self.updateEMGToolBox(type)

    def EMGConfigureToggleConfiguration(self, state):
        p, step, chan = self.singleEMG
        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        
        state = not not state
        if cfg[step].enable == state:
            return
        
        cfg[step].enable = state
        logger.info('EMG process step {}, configuration {} set to {}'.format(step, cfg.getStepStringList()[step], state))
        self.__updateEMGRenderBuffer(prev=False)
        self.updateEMGSignalProcessPanel(prev=False)

    def EMGConfigureFilterConfiguration(self):
        p, step, chan = self.singleEMG
        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        # according to UI layout
        filtertypename = {
            0 : emgFilterEnum.BAND_PASS,
            1 : emgFilterEnum.LOW_PASS,
        }
        filter_type = filtertypename[widgets.comboBox_7.currentIndex()]
        cutoff_b_h_text = widgets.lineEdit_10.text()
        cutoff_b_l_text = widgets.lineEdit_11.text()
        cutoff_l_l_text = widgets.lineEdit_12.text()
        print(cutoff_b_h_text)
        print(cutoff_b_l_text)
        cutoff_b_l = None
        cutoff_b_h = None
        cutoff_l_l = None
        if cutoff_b_l_text != '':
            cutoff_b_l = int(cutoff_b_l_text)
        if cutoff_b_h_text != '':
            cutoff_b_h = int(cutoff_b_h_text)
        if cutoff_l_l_text != '':
            cutoff_l_l = int(cutoff_l_l_text)

        fs = self.workspace[p].emg.getfs()
        #sanity
        if filter_type == emgFilterEnum.BAND_PASS:
            if cutoff_b_h is None or cutoff_b_l is None:
                QMessageBox.critical(None, 'error', 'cut off frequency is not complete!', QMessageBox.Ok)
                return
            if cutoff_b_h >= fs/2 or cutoff_b_h < 0 or cutoff_b_l >= fs/2 or cutoff_b_l < 0:
                QMessageBox.critical(None, 'error', 'cut off frequency has to be between 0 and {}!'.format(fs/2), QMessageBox.Ok)
                return
            if cutoff_b_l >= cutoff_b_h:
                QMessageBox.critical(None, 'error', 'cut off low has to be smaller than cut off high!', QMessageBox.Ok)
                return
        elif filter_type == emgFilterEnum.LOW_PASS:
            if cutoff_l_l is None:
                QMessageBox.critical(None, 'error', 'cut off frequency is not complete!', QMessageBox.Ok)
                return
            if cutoff_l_l >= fs/2 or cutoff_l_l < 0:
                QMessageBox.critical(None, 'error', 'cut off frequency has to be between 0 and {}!'.format(fs/2), QMessageBox.Ok)
                return

        cfg[step].type = filter_type
        if filter_type == emgFilterEnum.BAND_PASS:
            cfg[step].cutoff_l = cutoff_b_l
            cfg[step].cutoff_h = cutoff_b_h
        elif filter_type == emgFilterEnum.LOW_PASS:
            cfg[step].cutoff_l = cutoff_l_l
 
        self.__updateEMGRenderBuffer(prev=False)
        self.updateEMGSignalProcessPanel(prev=False)

    def EMGChannelSelectorIndexChanged(self, idx):
        p, step, chan = self.singleEMG
        if p is None:
            return
        newchan = widgets.comboBox_2.currentText()
        if chan == newchan:
            return
        logger.info('EMG channel selector index changed to {}'.format(newchan))
        self.selectSingleEMGChannel(newchan)

    def EMGChannelToolBoxIndexChanged(self, idx):
        # do not allow user change
        p, step, chan = self.singleEMG
        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        type, str = cfg.getTypeInfo(step)
        self.updateEMGToolBox(type)

    def EMGStepNextButtonClicked(self):
        p, step, chan = self.singleEMG
        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        
        if step + 1 >= cfg.size():
            QMessageBox.critical(None, 'error', 'end of emg process!', QMessageBox.Ok)
            return
        
        widgets.listWidget.setCurrentRow(step + 1)
        # equivent to double click on EMG configuration list
        self.EMGConfigurationListDoubleClicked(None)
    
    def EMGGenerateReportButtonClicked(self):
        # sanity
        p, step, chan = self.singleEMG
        if p is None:
            return
        
        # apply configuration on all chans in EMG and MVC
        # this might takes a while
        self.workspace[p].emg.processWithConfigure()

        # save report
        self.workspace.genReport(p)
        self.workspace.saveReport(p, self.home)

        # exit single process stage
        self.singleEMG = (None, None, None)
        self.updateEMGSignalProcessPanel()
        self.updateEMGConfigureList()

        self.selectedParticipants.clear()
        self.updateEMGParticipantBox()
    
    def EMGSaveConfigurationButtonClicked(self):
        p, step, chan = self.singleEMG
        if p is None:
            QMessageBox.critical(None, 'error', 'Single EMG not started!', QMessageBox.Ok)
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            QMessageBox.critical(None, 'error', 'EMG process file not available!', QMessageBox.Ok)
            return
        
        cfgname = p.name + "'s EMGConfig"
        self.workspace.saveConfigure(p, cfgname)
        self.updateEMGSavedConfigureList()

    def EMGBatchProcessButtonClicked(self):
        # sanity for pariticpants
        if len(self.selectedParticipants) == 0:
            QMessageBox.critical(None, 'error', 'Please select participants first!', QMessageBox.Ok)
            return
        
        listofpeople = []
        for p_key in self.selectedParticipants:
            p = self.workspace.findParticipant(int(p_key))
            if p is not None:
                listofpeople.append(p)

        logger.info("batch process: selected participants {}".format([','.join(p.name) for p in listofpeople]))
        
        # if report has been generated, generate warning

        # check configure file
        configureList = self.workspace.getConfigures()
        if len(configureList) == 0:
            QMessageBox.critical(None, 'error', 'No saved configuration file found, please use single EMG to generate configure file!', QMessageBox.Ok)
            return
        
        # get current selected one
        selectedConfigs = widgets.listWidget_2.selectedItems()
        if len(selectedConfigs) >= 1:
            config_name = selectedConfigs[0].text()
            config = configureList[config_name]
        else:
            # pick any one
            config_name = configureList.keys()[0]
            config = configureList[config_name]
            
        logger.info("batch process: select configure {}".format(config_name))
        self.startBatchEMGProcess(listofpeople, config)

    # WIDGET
    # //////////////////////////////////////////////////////////////
    def createParticipantCheckBox(self, name):
        checkbox = QCheckBox(widgets.tableWidget_2)
        checkbox.setObjectName(name)

        # select state according to selectedpartipant
        if name in self.selectedParticipants:
            checkbox.setChecked(True)
        else:
            checkbox.setChecked(False)
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
    def updateEMGSignalProcessPanel(self, prev = True, post = True):       
        p, step, chan = self.singleEMG

        if p is None:
            widgets.plot_input.hide()
            widgets.plot_output.hide()
            return

        x = self.workspace[p].emg.getLinspace()
        # push data to plot
             
        if prev:
            widgets.plot_input.line(x, self.inputBuffer, chan)
            widgets.plot_input.show()
        if post:
            widgets.plot_output.line(x, self.outputBuffer, chan)
            widgets.plot_output.show()
    
    def updateEMGConfigureList(self):
        widgets.listWidget.clear()

        if self.workspace is None:
            return
        p, step, chan = self.singleEMG
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
            emgConfigureEnum.DC_OFFSET : 0,
            emgConfigureEnum.FULL_W_RECT : 1,
            emgConfigureEnum.FILTER : 2,
            emgConfigureEnum.NORMALIZATION : 3,
            emgConfigureEnum.ACTIVATION : 4,
            emgConfigureEnum.SUMMARY : 5,
        }
        idx = type2toolbox[type] 
        widgets.toolBox.setCurrentIndex(idx)
        # update toolbox with current config
        p, step, chan = self.singleEMG
        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        if type == emgConfigureEnum.DC_OFFSET:
            widgets.checkBox_4.setCheckState(Qt.Checked if cfg[step].enable else Qt.Unchecked)
        elif type == emgConfigureEnum.FULL_W_RECT:
            widgets.checkBox_11.setCheckState(Qt.Checked if cfg[step].enable else Qt.Unchecked)
        elif type == emgConfigureEnum.FILTER:
            widgets.checkBox_13.setCheckState(Qt.Checked if cfg[step].enable else Qt.Unchecked)
            if cfg[step].type ==  emgFilterEnum.BAND_PASS:
                widgets.comboBox_7.setCurrentIndex(0)
                widgets.lineEdit_10.setText(str(cfg[step].cutoff_h))
                widgets.lineEdit_11.setText(str(cfg[step].cutoff_l))
                widgets.lineEdit_12.setText("")
            else:
                widgets.comboBox_7.setCurrentIndex(1)
                widgets.lineEdit_12.setText(str(cfg[step].cutoff_l))
                widgets.lineEdit_10.setText('')
                widgets.lineEdit_11.setText('')
        elif type == emgConfigureEnum.NORMALIZATION:
            widgets.checkBox_12.setCheckState(Qt.Checked if cfg[step].enable else Qt.Unchecked)
        elif type == emgConfigureEnum.SUMMARY:
            widgets.label_23.setText("{:.4f}".format(cfg[step].max))
            widgets.label_25.setText("{:.4f}".format(cfg[step].min))
            widgets.label_27.setText("{:.4f}".format(cfg[step].med))
            widgets.label_29.setText("{:.4f}".format(cfg[step].rms))
            widgets.label_31.setText("{:.4f}".format(cfg[step].ptp))
            widgets.label_33.setText("{:.4f}".format(cfg[step].zeros))

    def updateEMGChannelSelectorContent(self):
        p, step, chan = self.singleEMG
        widgets.comboBox_2.clear()
        if p is None:
            return
        chan = self.workspace[p].emg.getChannels()
        widgets.comboBox_2.addItems(chan)
    
    def updateEMGChannelSelectorText(self, chan):
        widgets.comboBox_2.setCurrentText(chan)

    def updateWorkProjectTreeWidget(self):
        widgets.treeView.setForegroundRole(QPalette.Base)
        if self.home is not None:
            widgets.treeView.setModel(self.filesystemTree)
            widgets.treeView.setRootIndex(self.filesystemTree.index(self.home))
        else:
            widgets.treeView.setModel(None)

    def updateEMGSavedConfigureList(self):
        if self.workspace is None:
            return
        p, step, chan = self.singleEMG
        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        # update configuration list
        n = len(self.workspace.getConfigures())
        widgets.listWidget_2.clear()
        widgets.listWidget_2.setSortingEnabled(False)
        i = 0
        for key, item in self.workspace.getConfigures().items():
            widgets.listWidget_2.addItem(key)
            widgets.listWidget_2.item(i).setForeground(Qt.black)
            i += 1

    # Application Logic/Slots
    # ///////////////////////////////////////////////////////////////
    def reset(self):
        self.singleEMG = (None, None, None)
        self.inputBuffer = None
        self.outputBuffer = None
        self.workspace = None
        self.home = None
        self.filesystemTree = QFileSystemModel()
        self.selectedParticipants = []

    def newWorkSpace(self, fpath, name=''):
        if self.workspace is not None:
            self.saveWorkSpace()
            self.reset()

        # create new project
        self.workspace = workspace(name)
        self.home = str(fpath)

        # load workspace file exploer
        self.filesystemTree.setRootPath(self.home)

        # clear GUI
        self.updateEMGSignalProcessPanel()
        self.updateEMGConfigureList()
        self.updateEMGParticipantBox()
        self.updateWorkSpaceParticipantBox()
        self.updateWorkProjectTreeWidget()
        self.updateEMGChannelSelectorContent()
        return 0
    
    def saveWorkSpace(self):
        return
    
    def startSingleEMGProcess(self, p):
        logger.info("started single EMG process for {}".format(p.name))
        if not self.workspace.hasParticipant(p):
            return -1
        
        # set fsm
        chan = self.workspace[p].emg.getChannels()[0]
        self.singleEMG = (p, 0, chan)
        self.workspace[p].emg.startProcess()
        self.updateEMGConfigureList()
        self.updateEMGChannelSelectorContent()
        self.updateEMGChannelSelectorText(chan)
        self.selectSingleEMGStep(0)

    def __updateEMGRenderBuffer(self, prev=True, post=True):
        p, step, chan = self.singleEMG
        if prev:
            if step == 0:
                self.inputBuffer = self.workspace[p].emg[chan]
            else:
                self.inputBuffer = self.workspace[p].emg.tryConfigStepTo(chan, step - 1)
        if post:
            self.outputBuffer = self.workspace[p].emg.tryConfigStepTo(chan, step)

    def selectSingleEMGChannel(self, chan):
        p, step, oldchan = self.singleEMG
        self.singleEMG = (p, step, chan)
        self.__updateEMGRenderBuffer()
        self.updateEMGSignalProcessPanel()

    def selectSingleEMGStep(self, idx):
        p, step, chan = self.singleEMG

        if p is None:
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        cfgstrings = cfg.getStepStringList()
        
        if idx > len(cfgstrings) or idx < 0:
            logger.info("single EMG process idx {} out of range".format(idx))

        logger.info("selecting EMG process step {}, {}".format(idx, cfgstrings[idx]))
        self.singleEMG = (p, idx, chan)
        logger.info("Current channel {}".format(chan))

        self.__updateEMGRenderBuffer()
        # select index for EMG config widget
        widgets.listWidget.setCurrentRow(idx)
        # update UI
        self.updateEMGSignalProcessPanel()
        type, str = cfg.getTypeInfo(idx)
        self.updateEMGToolBox(type)
        
    def startBatchEMGProcess(self, people, configure):
        for p in people:
            # process data
            self.workspace[p].emg.setProcessConfig(configure)
            self.workspace[p].emg.processWithConfigure()
            # save report
            self.workspace.genReport(p)
            self.workspace.saveReport(p, self.home)

        # clear selectedparitipant
        self.selectedParticipants.clear()
        self.updateEMGParticipantBox()
    
if __name__ == "__main__":
    from PySide6.QtQuick import QQuickWindow, QSGRendererInterface
    #DO NOT REMOVE enorce pyside to use opengl for underlying graphics render.
    QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGL)
    qApp = QApplication(sys.argv)
    qApp.setWindowIcon(QIcon("Myotion_logo.png"))
    window = MainWindow()
    qApp.exec()
    window.rserver.join()
    sys.exit(0)
