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
import re
import math
from pathlib import Path

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QIcon, QPalette
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QSizePolicy,
    QMessageBox,
    QDialog,
    QWidget,
    QFileDialog,
    QTableWidgetItem,
    QComboBox,
    QCheckBox,
    QFileSystemModel,
    QTreeWidget,
    QTreeWidgetItem,
    QFrame,
    QSpacerItem,
    QHBoxLayout,
)
from PySide6.QtWebEngineCore import QWebEngineUrlScheme

from modules.kinematics.controller import Controller
from modules.kinematics.model import Model
from rserver import RServer
from miscWidgets import *
from path import *
from qplotview import QPlotView

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
class EMGAddWindow(QDialog):
    def __init__(self, workspace, home, width, height, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_EMGImport()
        self.ui.setupUi(self)

        self.resize(width, height)
        self.setWindowTitle("Add EMG File")

        self.widgets = self.ui
        self.workspace = workspace
        self.root = home
        self.emg = None
        self.person = None
        self.channels = []
        self.mvcfiles = []
        self.mvcfilesMap = {}  # mapping mvc_file -> chan
        self.jointMap = {}  # mapping chan -> joints (short name)
        self.isControlSignal = {}  # isControlSignal[chan] = T/F

        self.widgets.import_btn.clicked.connect(self.importEMGBtnClicked)
        self.widgets.lineEdit.textChanged.connect(self.updateFilterText)
        self.widgets.import_btn_2.clicked.connect(self.confirmBtnClicked)
        self.widgets.import_btn_3.clicked.connect(self.cancelBtnClicked)
        self.widgets.importMVC_btn.clicked.connect(self.importMVCBtnClicked)

    def run(self):
        self.exec()
        return self.person, self.emg, self.kinematic

    # update emg and mvc qtablewidget
    def updateChannelBox(self):
        self.widgets.tableWidget.clearContents()
        # column width
        w = self.frameGeometry().width()
        # fixed ratio
        self.widgets.tableWidget.setColumnWidth(0, w * 0.3)
        self.widgets.tableWidget.setColumnWidth(1, w * 0.1)
        self.widgets.tableWidget.setColumnWidth(2, w * 0.2)
        self.widgets.tableWidget.setColumnWidth(3, w * 0.4)

        n = len(self.channels)
        self.widgets.tableWidget.setRowCount(n)
        for i in range(0, n):
            chan = self.channels[i]
            q = QTableWidgetItem(chan)
            q.setTextAlignment(Qt.AlignLeading | Qt.AlignVCenter)
            q.setFlags(q.flags() ^ Qt.ItemIsEditable)
            self.widgets.tableWidget.setItem(i, 0, q)
            # control signal checkbox
            self.widgets.tableWidget.setCellWidget(
                i, 1, self.controlSignalCheckbox(chan)
            )
            # drop down selection
            self.widgets.tableWidget.setCellWidget(i, 2, self.jointComboBox(chan))
            # mvc file path
            self.widgets.tableWidget.setCellWidget(i, 3, self.mvcFileDisplay(chan))

        self.widgets.tableWidget.resizeColumnToContents(0)

    def jointComboBox(self, chan):
        comboBox = QComboBox()
        comboBox.setObjectName(chan)
        comboBox.setEditable(True)
        for j in jointName.short:
            comboBox.addItem(jointName.getConcatName(j))

        if chan in self.jointMap:
            comboBox.setCurrentText(jointName.getConcatName(self.jointMap[chan]))
        else:
            comboBox.setCurrentIndex(-1)
        comboBox.currentIndexChanged.connect(self.jointBoxChanged)
        return comboBox

    def mvcFileDisplay(self, chan):
        comboBox = QComboBox()
        comboBox.setObjectName(chan)

        # only display file name instead of full path
        for f in self.mvcfiles:
            comboBox.addItem(os.path.basename(f))
        if chan in self.mvcfilesMap:
            comboBox.setCurrentIndex(self.mvcfilesMap[chan])
        else:
            comboBox.setCurrentIndex(-1)
        comboBox.currentIndexChanged.connect(self.MVCFilesChanged)
        return comboBox

    def controlSignalCheckbox(self, chan):
        checkbox = QCheckBox()
        checkbox.setObjectName(chan)
        checkbox.stateChanged.connect(self.controlSignalChanged)
        if chan in self.isControlSignal:
            checkbox.setChecked(self.isControlSignal[chan])
        else:
            self.isControlSignal[chan] = False
            checkbox.setChecked(False)

        QWid = QWidget()
        QHBox = QHBoxLayout(QWid)
        QHBox.addWidget(checkbox)
        QHBox.setAlignment(Qt.AlignCenter)
        QHBox.setContentsMargins(0, 0, 0, 0)
        return QWid

    # SIGNALS AND SLOT
    ################################################
    def jointBoxChanged(self, index):
        jointbox = self.sender()
        chan = jointbox.objectName()
        self.jointMap[chan] = jointName.short[index]

    def MVCFilesChanged(self, index):
        mvcBox = self.sender()
        chan = mvcBox.objectName()
        self.mvcfilesMap[chan] = index
        # apply MVC
        try:
            self.emg.setMVCFile(chan, self.mvcfiles[index])
        except Exception:
            QMessageBox.critical(
                None, "error", "Selected mvc file is invalid!", QMessageBox.Ok
            )
            return

    def controlSignalChanged(self, state):
        checkbox = self.sender()
        chan = checkbox.objectName()
        self.isControlSignal[chan] = not self.isControlSignal[chan]

        if self.isControlSignal[chan]:
            self.emg.setControlSignal(chan)
        else:
            self.emg.removeControlSignal(chan)

    def updateFilterText(self):
        filter_str = self.widgets.lineEdit.text()
        if filter_str == "":
            filter_str = ".*"

        # check valid regex string
        try:
            re.compile(filter_str)
        except re.error:
            logger.error("regex not valid")
            return

        self.channels = self.emg.searchChannels(filter_str)
        self.updateChannelBox()

    def importEMGBtnClicked(self):
        # load EMG file
        file, extension = QFileDialog.getOpenFileName(
            None,
            caption="open EMG file",
            dir=self.root,
            filter="EMG Files (*.c3d *.mat)",
        )
        if file == "":
            return
        self.file = file
        # open up emg MVC file
        try:
            self.emg = emg(file)
        except Exception:
            QMessageBox.critical(
                None, "error", "Selected emg file is invalid!", QMessageBox.Ok
            )
            return

        # get channels and update list
        self.channels = self.emg.getChannels()

        self.widgets.label_3.setText(file)
        # auto apply joint matching on joint mapping
        self.applyFuzzMatchOnJoint()
        self.updateChannelBox()

    def importMVCBtnClicked(self):
        if len(self.channels) == 0:
            QMessageBox.critical(
                None, "error", "Please select emg file before MVC file!", QMessageBox.Ok
            )
            return

        btn = self.sender()
        chan = btn.objectName()

        files, extension = QFileDialog.getOpenFileNames(
            None,
            caption="open MVC file",
            dir=self.root,
            filter="EMG Files (*.c3d *.mat)",
        )

        # clear old, set new val
        self.mvcfilesMap.clear()
        self.mvcfiles = files

        # auto apply fuzz matching on MVC mapping
        self.applyFuzzMatchOnMVC()
        self.updateChannelBox()

    def applyFuzzMatchOnMVC(self):
        filenames = [os.path.basename(f) for f in self.mvcfiles]
        for c in self.channels:
            # set only when possiblity bigger than 50%
            candidate_list = self.workspace.matchChanToMVCFile(
                c, filenames, lower_bound=50
            )
            if len(candidate_list) == 0:
                continue
            else:
                file, possibility = candidate_list[0]
                logger.info(
                    "EMG ADD MVC: selecting file {} for chan {}, possibility {}".format(
                        file, c, possibility
                    )
                )
                self.mvcfilesMap[c] = filenames.index(file)

    def applyFuzzMatchOnJoint(self):
        for c in self.channels:
            # set only when possiblity bigger than 50%
            candidate_list = self.workspace.matchChanToJoint(
                c, jointName.short, lower_bound=50
            )
            if len(candidate_list) == 0:
                continue
            else:
                joint, possibility = candidate_list[0]
                logger.info(
                    "EMG Select Joint: selecting Joint {} for chan {}, possibility {}".format(
                        joint, c, possibility
                    )
                )
                self.jointMap[c] = joint

    def sanity(self):
        # check emg file is selected
        if self.emg is None:
            QMessageBox.critical(None, "error", "No EMG file selected!", QMessageBox.Ok)
            return False
        # check mvc file is complete
        if not self.emg.isMVCComplete():
            QMessageBox.critical(
                None, "error", "MVC file not complete!", QMessageBox.Ok
            )
            return False
        # check pariticipant name is complete
        name = self.widgets.lineEdit_3.text()
        if name == "":
            QMessageBox.critical(
                None, "error", "Name of pariticipant not set!", QMessageBox.Ok
            )
            return False
        # check all joint names are selected
        for c in self.channels:
            if c not in self.jointMap and self.isControlSignal[c] == False:
                QMessageBox.critical(
                    None,
                    "error",
                    "Joint of channel {} not set!".format(c),
                    QMessageBox.Ok,
                )
                return False
        # check joint name is unique
        used_joint = {}
        for chan, joint in self.jointMap.items():
            if joint in used_joint:
                line1 = self.channels.index(used_joint[joint]) + 1
                line2 = self.channels.index(chan) + 1
                QMessageBox.critical(
                    None,
                    "error",
                    "Duplicated joint name founded, please check line {} and {}".format(
                        line1, line2
                    ),
                    QMessageBox.Ok,
                )
                return False
            used_joint[joint] = chan
        return True

    def confirmBtnClicked(self):
        if not self.sanity():
            return

        # creat person
        name = self.widgets.lineEdit_3.text()
        self.person = person(name, "N/A", "N/A")
        self.kinematic = kinematic(self.file)

        # filter and rename channels
        old = self.emg.getChannels()
        for c in old:
            if c not in self.channels:
                self.emg.removeChannel(c)

        for old, new in self.jointMap.items():
            self.emg.renameChannel(old, new)

        # update MVC file name matching fuzz string
        for chan, index in self.mvcfilesMap.items():
            self.workspace.addChanToMVCFileMap(
                chan, os.path.basename(self.mvcfiles[index])
            )

        for chan, joint in self.jointMap.items():
            self.workspace.addChanToJointMap(chan, joint)

        self.close()

    def cancelBtnClicked(self):
        self.person = None
        self.emg = None
        self.close()


class ConfigWindow(QDialog):
    def __init__(self, width, height, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Ui_Configuration()
        self.ui.setupUi(self)

        self.resize(width, height)
        self.setWindowTitle("Configuration")

        self.widgets = self.ui

    def run(self):
        self.exec()
        return self.person, self.emg, self.kinematic

    def confirmBtnClicked(self):
        return

    def cancelBtnClicked(self):
        self.close()


class MainWindow(QMainWindow):
    # SIGNALS
    sigUpdateParticipants = Signal()

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
        widgets.btn_share.clicked.connect(self.saveProjectButtonClick)
        widgets.btn_adjustments.clicked.connect(self.loadProjectButtonClick)
        self.sigUpdateParticipants.connect(self.updateEMGParticipantBox)

        # General
        widgets.settingsMenu.clicked.connect(self.configButtonClick)

        # EMG Page
        widgets.pushButton_10.clicked.connect(self.addEMGButtonClick)
        widgets.pushButton_11.clicked.connect(self.singleEMGButtonClick)
        widgets.listWidget.itemDoubleClicked.connect(
            self.EMGConfigurationListDoubleClicked
        )
        widgets.checkBox_4.stateChanged.connect(self.EMGConfigureToggleConfiguration)
        widgets.checkBox_11.stateChanged.connect(self.EMGConfigureToggleConfiguration)
        widgets.checkBox_12.stateChanged.connect(self.EMGConfigureToggleConfiguration)
        widgets.checkBox_13.stateChanged.connect(self.EMGConfigureToggleConfiguration)
        widgets.comboBox_2.currentIndexChanged.connect(
            self.EMGChannelSelectorIndexChanged
        )
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
        widgets.lineEdit_3.textChanged.connect(self.updateFilterText)
        widgets.checkBox_3.stateChanged.connect(self.EMGParticipantSelectAllClicked)

        # Freqency Page
        widgets.pushButton_29.clicked.connect(self.addNewFFTtoFreqAnalysisFFTPanel)
        widgets.pushButton_28.clicked.connect(self.FFTPlotPrevPageClicked)
        widgets.pushButton_30.clicked.connect(self.FFTPlotNextPageClicked)
        widgets.comboBox_19.currentIndexChanged.connect(self.FFTPlotPerPageSelected)
        widgets.comboBox_20.currentIndexChanged.connect(self.FFTPlotPageIndexSelected)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////

        # self.show()
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
        self.workspace = None
        self.home = None

        self.participant_filter = ""
        self.filesystemTree = (
            QFileSystemModel()
        )  # file system tree for workspace directory
        self.selectedParticipants = []  # key of selected participants
        self.singleEMG = (
            None,
            None,
            None,
        )  # sm for single EMG Process, (Participant, Steps, channel)
        self.inputBuffer = None  # buffer for single EMG process
        self.outputBuffer = None  # buffer for single EMG process

        # FrequencyAnalysis State Machine
        self.freqAnalysis = (None, None)  # (Participant, channel)
        self.freqAnalysisPlots = []  # plot diagram for frequency analysis
        self.plotsPerPage_list = [0, 1, 3, 5, 10]  # correspond to ui combox_19 setting

        # self.test()

    def test(self):
        self.newWorkSpace(os.getcwd(), "test")
        f = os.getcwd() + "/ERRPT.c3d"
        # "\\test\\Data\\lifting+bending\\LDH\\duchunguang\\2021-12-06-17-57_lift.mat"
        memg = emg(f)
        kin = kinematic(f)

        # add people
        p1 = person("Guo Chen", "1995/08/05", "male")

        # add data
        self.workspace.addParticipant(p1, memg, kin)

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
            self.preloadKinematicPage()
            return

        if btnName == "btn_frequency":
            widgets.stackedWidget.setCurrentWidget(widgets.frequency_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU
            self.preloadFreqAnalysisPage()

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
        p, emgdata, kinematic = EMGAddWindow(self.workspace, self.home, 1200, 800).run()
        if p is None:
            return

        logger.info("added participate {}".format(p.name))

        # add to workspace
        self.workspace.addParticipant(p, emgdata, kinematic)

        # update UI
        self.updateEMGParticipantBox()
        self.updateWorkSpaceParticipantBox()

    def configButtonClick(self):
        rc = ConfigWindow(1200, 800).run()

    def ifOldProjectOpened(self):
        if self.workspace is not None:
            relpy = QMessageBox.question(
                None,
                "warning",
                "Current workspace not closed, do you want to save and continue?",
                QMessageBox.Yes | QMessageBox.No,
            )

            if relpy == QMessageBox.Yes:
                self.saveWorkSpace()
                self.reset()
                return 0
            else:
                return -1
        return 0

    def newProjectButtonClick(self):
        if self.ifOldProjectOpened():
            return -1

        filename = QFileDialog.getSaveFileName(
            None,
            "New Project",
            self.home,
            "Project files (*.myo)",
            None,
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )
        if filename[0] == "":
            return

        proj_full_name = os.path.basename(filename[0])
        dir = filename[0][: -len(proj_full_name)]

        proj_name = proj_full_name[: -len(PROJ_EXT)]
        print("#############################", dir)
        print("#############################", proj_name)
        if not checkValidPath(dir):
            QMessageBox.critical(
                None, "error", "Selected path does not exist!", QMessageBox.Ok
            )

        p = Path(dir)
        if self.newWorkSpace(p, proj_name):
            QMessageBox.critical(
                None, "error", "Failed to create new Workspace!", QMessageBox.Ok
            )

        logger.info("workspace path: {}".format(self.home))
        logger.info("workspace name: {}".format(self.workspace.name))

        # Jump to EMG page
        widgets.stackedWidget.setCurrentWidget(widgets.emg_page)

    def saveProjectButtonClick(self):
        if self.workspace is None:
            logger.info("workspace is empty, nothing to save")
            return

        if self.saveWorkSpace():
            QMessageBox.critical(
                None, "error", "Failed to save Workspace!", QMessageBox.Ok
            )
            return
        logger.info("workspace is saved")

    def loadProjectButtonClick(self):
        if self.ifOldProjectOpened():
            return -1

        filepath, extension = QFileDialog.getOpenFileNames(
            None,
            caption="open Project file",
            dir=MyotionPath,
            filter="Project Files (*.myo)",
        )

        if len(filepath) == 0:
            return

        file = os.path.basename(filepath[0])
        path = filepath[0][: -len(file)]

        if self.loadWorkSpace(path, file):
            QMessageBox.critical(
                None, "error", "Failed to load Workspace!", QMessageBox.Ok
            )
            return

        # Jump to EMG page
        widgets.stackedWidget.setCurrentWidget(widgets.emg_page)

    def singleEMGButtonClick(self):
        p, step, chan = self.singleEMG

        if len(self.selectedParticipants) == 0:
            QMessageBox.critical(
                None, "error", "No participant selected!", QMessageBox.Ok
            )
            return

        if len(self.selectedParticipants) > 1:
            QMessageBox.critical(
                None, "error", "Only one participant can be selected!", QMessageBox.Ok
            )
            return

        if p is not None:
            QMessageBox.critical(
                None, "error", "Current EMG process is not finished!", QMessageBox.Ok
            )
            return
        p_name = self.selectedParticipants[0]
        p = self.workspace.findParticipant(p_name)
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
        logger.info(
            "EMG process step {}, configuration {} set to {}".format(
                step, cfg.getStepStringList()[step], state
            )
        )
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
            0: emgFilterEnum.BAND_PASS,
            1: emgFilterEnum.LOW_PASS,
        }
        filter_type = filtertypename[widgets.comboBox_7.currentIndex()]
        cutoff_b_h_text = widgets.lineEdit_10.text()
        cutoff_b_l_text = widgets.lineEdit_11.text()
        cutoff_l_l_text = widgets.lineEdit_12.text()
        # order set from 2,3,4
        order = widgets.comboBox_8.currentIndex() + 2
        cutoff_b_l = None
        cutoff_b_h = None
        cutoff_l_l = None
        if cutoff_b_l_text != "":
            cutoff_b_l = int(cutoff_b_l_text)
        if cutoff_b_h_text != "":
            cutoff_b_h = int(cutoff_b_h_text)
        if cutoff_l_l_text != "":
            cutoff_l_l = int(cutoff_l_l_text)

        fs = self.workspace[p].emg.getfs()
        # sanity
        if filter_type == emgFilterEnum.BAND_PASS:
            if cutoff_b_h is None or cutoff_b_l is None:
                QMessageBox.critical(
                    None, "error", "cut off frequency is not complete!", QMessageBox.Ok
                )
                return
            if (
                cutoff_b_h >= fs / 2
                or cutoff_b_h < 0
                or cutoff_b_l >= fs / 2
                or cutoff_b_l < 0
            ):
                QMessageBox.critical(
                    None,
                    "error",
                    "cut off frequency has to be between 0 and {}!".format(fs / 2),
                    QMessageBox.Ok,
                )
                return
            if cutoff_b_l >= cutoff_b_h:
                QMessageBox.critical(
                    None,
                    "error",
                    "cut off low has to be smaller than cut off high!",
                    QMessageBox.Ok,
                )
                return
        elif filter_type == emgFilterEnum.LOW_PASS:
            if cutoff_l_l is None:
                QMessageBox.critical(
                    None, "error", "cut off frequency is not complete!", QMessageBox.Ok
                )
                return
            if cutoff_l_l >= fs / 2 or cutoff_l_l < 0:
                QMessageBox.critical(
                    None,
                    "error",
                    "cut off frequency has to be between 0 and {}!".format(fs / 2),
                    QMessageBox.Ok,
                )
                return

        cfg[step].type = filter_type
        if filter_type == emgFilterEnum.BAND_PASS:
            cfg[step].cutoff_l = cutoff_b_l
            cfg[step].cutoff_h = cutoff_b_h
        elif filter_type == emgFilterEnum.LOW_PASS:
            cfg[step].cutoff_l = cutoff_l_l
        cfg[step].order = order

        logger.info(
            "EMG process step {}, configuration filter,"
            " type {}, high {}, low {}, order {}".format(
                step, filter_type, cutoff_b_h, cutoff_b_l, order
            )
        )

        self.__updateEMGRenderBuffer(prev=False)
        self.updateEMGSignalProcessPanel(prev=False)

    def EMGChannelSelectorIndexChanged(self, idx):
        p, step, chan = self.singleEMG
        if p is None:
            return
        newchan = widgets.comboBox_2.currentText()
        if chan == newchan:
            return
        logger.info("EMG channel selector index changed to {}".format(newchan))
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
            QMessageBox.critical(None, "error", "end of emg process!", QMessageBox.Ok)
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
            QMessageBox.critical(
                None, "error", "Single EMG not started!", QMessageBox.Ok
            )
            return
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            QMessageBox.critical(
                None, "error", "EMG process file not available!", QMessageBox.Ok
            )
            return

        cfgname = p.name + "'s EMGConfig"
        self.workspace.saveEMGConfigure(p, cfgname)
        self.updateEMGSavedConfigureList()

    def EMGBatchProcessButtonClicked(self):
        # sanity for pariticpants
        if len(self.selectedParticipants) == 0:
            QMessageBox.critical(
                None, "error", "Please select participants first!", QMessageBox.Ok
            )
            return

        listofpeople = []
        for p_name in self.selectedParticipants:
            p = self.workspace.findParticipant(p_name)
            if p is not None:
                listofpeople.append(p)

        logger.info(
            "batch process: selected participants {}".format(
                [",".join(p.name) for p in listofpeople]
            )
        )

        # if report has been generated, generate warning

        # check configure file
        configureList = self.workspace.getEMGConfigures()
        if len(configureList) == 0:
            QMessageBox.critical(
                None,
                "error",
                "No saved configuration file found, please use single EMG to generate configure file!",
                QMessageBox.Ok,
            )
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

    def EMGParticipantSelectAllClicked(self, state):
        self.selectedParticipants.clear()
        participants = self.workspace.getFilteredParticipants(self.participant_filter)
        for p in participants:
            if state:
                self.selectedParticipants.append(p)
            else:
                self.selectedParticipants.remove(p)

        self.updateEMGParticipantBox()

    def FFTPlotNextPageClicked(self):
        widgets.scrollArea_3.nextPage()
        self.updateFreqAnalysisFFTPanel()

    def FFTPlotPrevPageClicked(self):
        widgets.scrollArea_3.prevPage()
        self.updateFreqAnalysisFFTPanel()

    def FFTPlotPerPageSelected(self, index):
        self.updateFreqAnalysisFFTPanel()

    def FFTPlotPageIndexSelected(self, index):
        widgets.scrollArea_3.setCurrentPage(index)
        widgets.scrollArea_3.show()

    # WIDGET
    # //////////////////////////////////////////////////////////////
    def EMGCreateParticipantCheckBox(self, name):
        checkbox = QCheckBox(widgets.tableWidget_2)
        checkbox.setObjectName(name)

        # select state according to selectedpartipant
        if name in self.selectedParticipants:
            checkbox.setChecked(True)
        else:
            checkbox.setChecked(False)
        checkbox.stateChanged.connect(self.participantCheckBoxChanged)
        return checkbox

    def EMGCreateHBox(self, w, parent=None):
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.addWidget(w, alignment=Qt.AlignHCenter)
        w.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        return container

    # draw FFT
    def FreqAnalysisCreateQPlotView(self, p, channel, l, r, title):
        pv = QPlotView()
        # calcuate FFT
        tst = self.workspace[p].emg.getTST()
        freq, v = tst.fft_db(channel, l, r)
        # delete negliable value
        to_del = np.argwhere(v <= 1e-3)
        freq = np.delete(freq, to_del)
        v = np.delete(v, to_del)
        # pv.bar(freq, v, channel, title=title,xlabel='Frequency', ylabel='dB')
        # pv.show()
        pv.line(freq, v, channel, title=title, xlabel="Frequency", ylabel="dB")
        return pv

    # Signals
    # //////////////////////////////////////////////////////////////
    def emitPariticipantUpdate(self):
        self.sigUpdateParticipants.emit()

    # UPDATE UI EVENTS/Slots
    # //////////////////////////////////////////////////////////////
    @Slot()
    def updateEMGParticipantBox(self):
        participants = self.workspace.getFilteredParticipants(self.participant_filter)
        n = len(participants)
        widgets.tableWidget_2.clearContents()
        widgets.tableWidget_2.setRowCount(n)
        for i in range(0, n):
            p = participants[i]
            name = p.name
            # checkbox
            chb = self.EMGCreateParticipantCheckBox(p.name)
            widgets.tableWidget_2.setCellWidget(i, 0, chb)
            # name
            q = QTableWidgetItem(name)
            q.setTextAlignment(Qt.AlignCenter)
            widgets.tableWidget_2.setItem(i, 1, q)
            # status
            h = widgets.tableWidget_2.rowHeight(i)
            col2w = widgets.tableWidget_2.columnWidth(2)
            col3w = widgets.tableWidget_2.columnWidth(3)
            ready = statusLED(col2w, h, not self.workspace[p].isLoading())
            report = statusLED(col3w, h, self.workspace[p].isReportReady())
            widgets.tableWidget_2.setCellWidget(i, 2, ready)
            widgets.tableWidget_2.setCellWidget(i, 3, report)

    def updateWorkSpaceParticipantBox(self):
        # listwidget_3
        participants = self.workspace.getParticipants()
        n = len(participants)
        widgets.listWidget_3.clear()
        for i in range(0, n):
            p = participants[i]
            name = p.name
            # name

            item = QListWidgetItem(name)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            widgets.listWidget_3.addItem(item)
            widgets.listWidget_3.item(i).setForeground(Qt.black)

    # update waveform regarding to config step and user input metrics
    def updateEMGSignalProcessPanel(self, prev=True, post=True):
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
            emgConfigureEnum.DC_OFFSET: 0,
            emgConfigureEnum.FULL_W_RECT: 1,
            emgConfigureEnum.FILTER: 2,
            emgConfigureEnum.NORMALIZATION: 3,
            emgConfigureEnum.ACTIVATION: 4,
            emgConfigureEnum.SUMMARY: 5,
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
            widgets.checkBox_4.setCheckState(
                Qt.Checked if cfg[step].enable else Qt.Unchecked
            )
        elif type == emgConfigureEnum.FULL_W_RECT:
            widgets.checkBox_11.setCheckState(
                Qt.Checked if cfg[step].enable else Qt.Unchecked
            )
        elif type == emgConfigureEnum.FILTER:
            widgets.checkBox_13.setCheckState(
                Qt.Checked if cfg[step].enable else Qt.Unchecked
            )
            if cfg[step].type == emgFilterEnum.BAND_PASS:
                widgets.comboBox_7.setCurrentIndex(0)
                widgets.lineEdit_10.setText(str(cfg[step].cutoff_h))
                widgets.lineEdit_11.setText(str(cfg[step].cutoff_l))
                widgets.lineEdit_12.setText("")
            else:
                widgets.comboBox_7.setCurrentIndex(1)
                widgets.lineEdit_12.setText(str(cfg[step].cutoff_l))
                widgets.lineEdit_10.setText("")
                widgets.lineEdit_11.setText("")
        elif type == emgConfigureEnum.NORMALIZATION:
            widgets.checkBox_12.setCheckState(
                Qt.Checked if cfg[step].enable else Qt.Unchecked
            )
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
            # load workspace file exploer
            self.filesystemTree.setRootPath(self.home)
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
        n = len(self.workspace.getEMGConfigures())
        widgets.listWidget_2.clear()
        widgets.listWidget_2.setSortingEnabled(False)
        i = 0
        for key, item in self.workspace.getEMGConfigures().items():
            widgets.listWidget_2.addItem(key)
            widgets.listWidget_2.item(i).setForeground(Qt.black)
            i += 1

    def updateFilterText(self):
        filter_str = widgets.lineEdit_3.text()
        # check valid regex string
        try:
            re.compile(filter_str)
        except re.error:
            logger.error("regex not valid")
            return

        if filter_str == self.participant_filter:
            return

        self.participant_filter = filter_str
        self.selectedParticipants.clear()
        self.updateEMGParticipantBox()

    def updateFreqAnalysisParticipantTree(self, participants):
        widgets.frequency_participants.clear()
        widgets.frequency_participants.setColumnCount(1)
        for p in participants:
            treeItem = QTreeWidgetItem()
            treeItem.setText(0, p.name)
            widgets.frequency_participants.addTopLevelItem(treeItem)
            emg = self.workspace[p].emg
            for c in emg.getChannels():
                treeItem2 = QTreeWidgetItem(treeItem)
                treeItem2.setText(0, c)  # channel name
                treeItem.addChild(treeItem2)
        # connect slots
        widgets.frequency_participants.itemDoubleClicked.connect(
            self.updateFreqAnalysisWaveformPanel
        )
        widgets.frequency_participants.setHeaderItem(QTreeWidgetItem(["Participant"]))
        widgets.frequency_participants.addTopLevelItem(treeItem)

    def updateFreqAnalysisWaveformPanel(self, item, column):
        # if item is top level, return
        if item.parent() is None:
            return

        p_name = item.parent().text(column)
        channel = item.text(column)
        p = self.workspace.findParticipant(p_name)
        x = self.workspace[p].emg.getLinspace()

        # set state machine
        logger.info(
            "Frequency Analysis - selecting {} channel {}".format(p.name, channel)
        )
        self.freqAnalysis = (p, channel)
        self.freqAnalysisPlots.clear()

        widgets.freq_timedomain.line(x, self.workspace[p].emg[channel], channel)
        widgets.freq_timedomain.show()
        self.updateFreqAnalysisFFTPanel()

    def updateFreqAnalysisFFTPanel(self):
        # update control ui
        # get pages per frame
        plotsPerPage = self.plotsPerPage_list[widgets.comboBox_19.currentIndex()]
        widgets.scrollArea_3.setPlotsPerPage(plotsPerPage)
        # page index selector
        currentpage = widgets.scrollArea_3.currentPage()
        widgets.comboBox_20.clear()
        widgets.comboBox_20.addItems(
            [str(i + 1) for i in range(0, widgets.scrollArea_3.pages())]
        )

        widgets.scrollArea_3.setCurrentPage(currentpage)
        widgets.comboBox_20.setCurrentIndex(widgets.scrollArea_3.currentPage())
        widgets.scrollArea_3.show()
        logger.info(
            "Updating FFT Analysis figure, nums_per_page: {} total page: {}, total plots:{}, current page: {}".format(
                widgets.scrollArea_3.plotsPerPage(),
                widgets.scrollArea_3.pages(),
                widgets.scrollArea_3.size(),
                widgets.scrollArea_3.currentPage(),
            )
        )

    # Application Logic
    # ///////////////////////////////////////////////////////////////
    def reset(self):
        self.singleEMG = (None, None, None)
        self.inputBuffer = None
        self.outputBuffer = None
        self.workspace = None
        self.home = None
        self.filesystemTree = QFileSystemModel()
        self.selectedParticipants = []

    def newWorkSpace(self, fpath, name):
        # create new project
        # self.workspace = workspace(name)
        self.workspace = workspace(str(fpath), name)
        self.home = str(fpath)

        # clear GUI
        self.updateEMGSignalProcessPanel()
        self.updateEMGConfigureList()
        self.updateEMGParticipantBox()
        self.updateWorkSpaceParticipantBox()
        self.updateWorkProjectTreeWidget()
        self.updateEMGChannelSelectorContent()

        # notify rserver
        self.rserver.UpdateProjectPath(self.home)
        return 0

    def saveWorkSpace(self):
        self.workspace.saveWorkSpace(self.home)
        return 0

    def loadWorkSpace(self, path, file):
        self.workspace = workspace.loadWorkSpace(
            path, file, self.emitPariticipantUpdate
        )
        if self.workspace == None:
            return -1
        self.home = self.workspace.fpath

        # load workspace file exploer
        self.filesystemTree.setRootPath(self.home)

        # clear and load GUI
        self.updateEMGSignalProcessPanel()
        self.updateEMGConfigureList()
        self.updateEMGParticipantBox()
        self.updateWorkSpaceParticipantBox()
        self.updateWorkProjectTreeWidget()
        self.updateEMGChannelSelectorContent()

        return 0

    def populateKinematicTree(self, tree: QTreeWidget, participants):
        tree.clear()
        tree.setColumnCount(1)
        tree.setDragEnabled(True)
        tree.setDropIndicatorShown(True)
        tree.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        for p in participants:
            treeItem = QTreeWidgetItem()
            treeItem.setText(0, p.name)
            tree.addTopLevelItem(treeItem)
            person = self.workspace[p]
            emg = person.emg
            k = person.kinematic
            for point in k.reallabels:
                tr = QTreeWidgetItem(treeItem)
                tr.setFlags(tr.flags() | Qt.ItemIsDragEnabled | Qt.ItemIsSelectable)
                tr.setText(0, point)
                treeItem.addChild(tr)
            for c in emg.getChannels():
                treeItem2 = QTreeWidgetItem(treeItem)
                treeItem2.setText(0, c)
                treeItem.addChild(treeItem2)
        tree.setHeaderItem(QTreeWidgetItem(["Participant"]))
        tree.addTopLevelItem(treeItem)

    def preloadKinematicPage(self):
        ps = self.workspace.getParticipants()
        self.populateKinematicTree(widgets.kinematics_label_tree, ps)
        p = ps[0]

        if p is None:
            return

        self.model = Model(self.workspace[p])
        top = widgets.graph_top
        top.setModel(self.model, widgets.kinematics_label_tree)
        # bottom = widgets.graph_bottom
        # bottom.setModel(self.model, widgets.kinematics_label_tree)
        Controller(
            self.model,
            widgets.renderWidget,
            widgets.playSlider,
            widgets.kinematic_analysis,
            None,
            widgets.kinematics_label_tree,
        )

    def preloadFreqAnalysisPage(self):
        self.updateFreqAnalysisParticipantTree(self.workspace.getParticipants())
        self.freqAnalysisPlots.clear()

    def addNewFFTtoFreqAnalysisFFTPanel(self):
        p, chan = self.freqAnalysis
        tst = self.workspace[p].emg.getTST()
        try:
            left = float(widgets.lineEdit_5.text())
            right = float(widgets.lineEdit_4.text())
            # check sanity
            if left < 0 or left > tst.time:
                left = 0.0
            if right < 0 or right > tst.time:
                right = float(tst.time)
        except Exception:
            left = 0.0
            right = float(tst.time)

        widgets.lineEdit_5.setText(str(left))
        widgets.lineEdit_4.setText(str(right))

        num_plots = 1
        if widgets.lineEdit_6.text() != "":
            num_plots = int(widgets.lineEdit_6.text())

        curr_time = left
        step = (right - left) / num_plots
        for i in range(0, num_plots):
            title = "Frequency Analysis: {} s to {} s".format(
                curr_time, curr_time + step
            )
            newPlot = self.FreqAnalysisCreateQPlotView(
                p, chan, curr_time, curr_time + step, title=title
            )
            self.freqAnalysisPlots.append(newPlot)
            widgets.scrollArea_3.append(newPlot)
            curr_time += step
        self.updateFreqAnalysisFFTPanel()

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

        # update summary toolbox
        cfg = self.workspace[p].emg.getProcessConfig()
        if cfg is None:
            return
        idx = widgets.listWidget.currentRow()
        type, str = cfg.getTypeInfo(idx)
        self.updateEMGToolBox(type)

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
            logger.info("Batch Process: processing data for {}".format(p.name))
            # process data
            self.workspace[p].emg.setProcessConfig(configure)
            self.workspace[p].emg.processWithConfigure()
            # save report
            self.workspace.genReport(p)
            self.workspace.saveReport(p, self.home)

        # clear selectedparitipant
        self.selectedParticipants.clear()
        self.updateEMGParticipantBox()


# setting up Url Scheme string before app starts
# this is for qplotview setup
def QPlotViewSetup():
    scheme = QWebEngineUrlScheme(bytes("local", "ascii"))
    scheme.setFlags(
        QWebEngineUrlScheme.Flag.SecureScheme
        | QWebEngineUrlScheme.Flag.LocalScheme
        | QWebEngineUrlScheme.Flag.LocalAccessAllowed
    )
    QWebEngineUrlScheme.registerScheme(scheme)


if __name__ == "__main__":
    from PySide6.QtQuick import QQuickWindow, QSGRendererInterface

    # DO NOT REMOVE enforce pyside to use opengl for underlying graphics render.
    QQuickWindow.setGraphicsApi(QSGRendererInterface.GraphicsApi.OpenGL)

    # Setup Url scheme handler for WebEngineView
    QPlotViewSetup()

    qApp = QApplication(sys.argv)
    qApp.setWindowIcon(QIcon("Myotion_logo.png"))
    window = MainWindow()
    qApp.exec()
    window.rserver.join()
    sys.exit(0)
