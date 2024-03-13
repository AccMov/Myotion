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
from  pathlib import Path
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTimer, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QToolBar, QMessageBox,
    QWidget, QFileDialog, QTableWidgetItem)

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

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
        self.participants = []              # particpate list
        self.singleEMG = (None, None)        # Participant, Steps
        self.batchEMG = (None, None)         # Participant list, configure file

        self.test()

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
            self.test()

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

        # load EMG file
        file = QFileDialog.getOpenFileName(None, 'open EMG file', self.home, "EMG Files (*.c3d *.mat)")
        
        # add to list
        #self.participants.insert()

        # update UI
        return

    def newProjectButtonClick(self):
        dir = QFileDialog.getExistingDirectory(None, 'New Project', self.home, 
                    QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        
        if not self.__checkValidPath__(dir):
            QMessageBox.critical(None, 'error', 'Selected path does not exist!', QMessageBox.Ok)

        p = Path(dir)
        if self.newWorkSpace(p.parent, p.name):
            QMessageBox.critical(None, 'error', 'Failed to create new Workspace!', QMessageBox.Ok)
        
        print('workspace path: {}'.format(self.home))
        print('workspace name: {}'.format(self.workspace.name))

    # UPDATE UI EVENTS
    # //////////////////////////////////////////////////////////////
    def updateparticipantBox(self):
        # emg panel
        n = len(self.participants)
        widgets.tableWidget_2.setRowCount(n)
        for i in range(0, n):
            q = QTableWidgetItem(self.participants[i].name)
            q.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)
            widgets.tableWidget_2.setItem(i, 1, q)

    # Application Logic
    # ///////////////////////////////////////////////////////////////
    def __checkValidPath__(self, fpath):
        return os.path.exists(fpath)
    
    def newWorkSpace(self, fpath, name=''):
        if self.workspace is not None:
            self.saveWorkSpace()
            self.workspace.clear()
            self.updateparticipantTable()
        
        # create new project
        self.workspace = pm.workspace(name)
        
        self.home = fpath
        return 0
    
    def saveWorkSpace(self):
        return
    
    
    def addSingleEMGFile(self, fpath):
        if self.__checkValidPath__(fpath):
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
