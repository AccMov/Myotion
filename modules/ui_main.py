# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,QMetaObject, QRect,QSize,  Qt) 
from PySide6.QtGui import (QBrush, QColor, QCursor,QFont,QIcon,QPalette)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea,
    QScrollBar, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QTreeWidget, QVBoxLayout, QWidget, QTreeView)
 
from modules.kinematics.bodyrender import BodyRender
from modules.kinematics.renderwidget import RenderWidget
from modules.kinematics.playbarwidget import PlayBarWidget, SliderWidget

from . resources_rc import *
from rserver import RServerBrowser
from qplotview import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_35 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setStyleSheet(u"background:url(:/images/Myotion_logo.png)")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setBold(True)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setStyleSheet(u"font-size:12px;\n"
"font-weight:bold;")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setStyleSheet(u"color:#ff6900;\n"
"font-size:10px;\n"
"")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_start = QPushButton(self.topMenu)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QSize(0, 45))
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setLayoutDirection(Qt.LeftToRight)
        self.btn_start.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_start)

        self.btn_emg = QPushButton(self.topMenu)
        self.btn_emg.setObjectName(u"btn_emg")
        sizePolicy.setHeightForWidth(self.btn_emg.sizePolicy().hasHeightForWidth())
        self.btn_emg.setSizePolicy(sizePolicy)
        self.btn_emg.setMinimumSize(QSize(0, 45))
        self.btn_emg.setFont(font)
        self.btn_emg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_emg.setLayoutDirection(Qt.LeftToRight)
        self.btn_emg.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder.png);")

        self.verticalLayout_8.addWidget(self.btn_emg)

        self.btn_kinematic = QPushButton(self.topMenu)
        self.btn_kinematic.setObjectName(u"btn_kinematic")
        sizePolicy.setHeightForWidth(self.btn_kinematic.sizePolicy().hasHeightForWidth())
        self.btn_kinematic.setSizePolicy(sizePolicy)
        self.btn_kinematic.setMinimumSize(QSize(0, 45))
        self.btn_kinematic.setFont(font)
        self.btn_kinematic.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_kinematic.setLayoutDirection(Qt.LeftToRight)
        self.btn_kinematic.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-people.png);")

        self.verticalLayout_8.addWidget(self.btn_kinematic)

        self.btn_frequency = QPushButton(self.topMenu)
        self.btn_frequency.setObjectName(u"btn_frequency")
        sizePolicy.setHeightForWidth(self.btn_frequency.sizePolicy().hasHeightForWidth())
        self.btn_frequency.setSizePolicy(sizePolicy)
        self.btn_frequency.setMinimumSize(QSize(0, 45))
        self.btn_frequency.setFont(font)
        self.btn_frequency.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_frequency.setLayoutDirection(Qt.LeftToRight)
        self.btn_frequency.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_8.addWidget(self.btn_frequency)

        self.btn_advanced = QPushButton(self.topMenu)
        self.btn_advanced.setObjectName(u"btn_advanced")
        sizePolicy.setHeightForWidth(self.btn_advanced.sizePolicy().hasHeightForWidth())
        self.btn_advanced.setSizePolicy(sizePolicy)
        self.btn_advanced.setMinimumSize(QSize(0, 45))
        self.btn_advanced.setFont(font)
        self.btn_advanced.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_advanced.setLayoutDirection(Qt.LeftToRight)
        self.btn_advanced.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-signal-cellular-3.png)")

        self.verticalLayout_8.addWidget(self.btn_advanced)

        self.btn_stats = QPushButton(self.topMenu)
        self.btn_stats.setObjectName(u"btn_stats")
        sizePolicy.setHeightForWidth(self.btn_stats.sizePolicy().hasHeightForWidth())
        self.btn_stats.setSizePolicy(sizePolicy)
        self.btn_stats.setMinimumSize(QSize(0, 45))
        self.btn_stats.setFont(font)
        self.btn_stats.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stats.setLayoutDirection(Qt.LeftToRight)
        self.btn_stats.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_8.addWidget(self.btn_stats)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(300, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setStyleSheet(u"background-color:rgba(255,105,0,1);")
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"")
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        self.extraLabel.setStyleSheet(u"font-weight: bold;\n"
"")

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.btn_new = QPushButton(self.extraTopMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_new)

        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-folder-open.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.extraCenter)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"border:none;")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_50)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.workspace_tree = QFrame(self.frame_50)
        self.workspace_tree.setObjectName(u"workspace_tree")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.workspace_tree.sizePolicy().hasHeightForWidth())
        self.workspace_tree.setSizePolicy(sizePolicy1)
        self.workspace_tree.setFrameShape(QFrame.StyledPanel)
        self.workspace_tree.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.workspace_tree)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.workspace_tree)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"\n"
"border-top:1px solid rgba(255,255,255,0.2);")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_55)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"border:none;\n"
"margin:6px 6px;")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_56)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font-weight: bold;\n"
"font-size:12px;")

        self.horizontalLayout_39.addWidget(self.label_39)

        self.horizontalSpacer_18 = QSpacerItem(120, 8, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_18)


        self.verticalLayout_78.addWidget(self.frame_56)


        self.verticalLayout_79.addWidget(self.frame_55)

        self.treeView = QTreeView(self.workspace_tree)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"font-size:14px;\n"
"color: rgba(0,0,0,0.8);\n"
"")

        self.verticalLayout_79.addWidget(self.treeView)


        self.verticalLayout_64.addWidget(self.workspace_tree)

        self.paticipant_list = QFrame(self.frame_50)
        self.paticipant_list.setObjectName(u"paticipant_list")
        sizePolicy1.setHeightForWidth(self.paticipant_list.sizePolicy().hasHeightForWidth())
        self.paticipant_list.setSizePolicy(sizePolicy1)
        self.paticipant_list.setFrameShape(QFrame.StyledPanel)
        self.paticipant_list.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.paticipant_list)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.paticipant_list)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setStyleSheet(u"\n"
"border-top:1px solid rgba(255,255,255,0.2);")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_51)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.frame_51)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"border:none;\n"
"margin:6px 6px;")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_52)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font-weight: bold;\n"
"font-size:12px;")

        self.horizontalLayout_34.addWidget(self.label_38)

        self.horizontalSpacer_16 = QSpacerItem(120, 8, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_16)


        self.verticalLayout_77.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_51)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"margin:0px 6px;\n"
"border: none;")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.checkBox_3 = QCheckBox(self.frame_53)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_33.addWidget(self.checkBox_3)

        self.horizontalSpacer_17 = QSpacerItem(93, 11, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_17)

        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setStyleSheet(u"border: none;\n"
"")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.pushButton_17 = QPushButton(self.frame_54)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"background-color:rgba(0,0,0,0.8);\n"
"margin:3px 2px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon1)

        self.horizontalLayout_32.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_54)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet(u"background-color:rgba(0,0,0,0.8);\n"
"margin:3px 2px;\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon2)

        self.horizontalLayout_32.addWidget(self.pushButton_18)


        self.horizontalLayout_33.addWidget(self.frame_54)


        self.verticalLayout_77.addWidget(self.frame_53)


        self.verticalLayout_65.addWidget(self.frame_51)

        self.listWidget_3 = QListWidget(self.paticipant_list)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout_65.addWidget(self.listWidget_3)


        self.verticalLayout_64.addWidget(self.paticipant_list)


        self.verticalLayout_10.addWidget(self.frame_50)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setMinimumSize(QSize(0, 33))
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font-weight:bold;\n"
"font-size:16px;")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.menuBox = QFrame(self.contentTopBg)
        self.menuBox.setObjectName(u"menuBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(6)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.menuBox.sizePolicy().hasHeightForWidth())
        self.menuBox.setSizePolicy(sizePolicy4)
        self.menuBox.setStyleSheet(u"border:none;\n"
"font-size:11px;")
        self.menuBox.setFrameShape(QFrame.StyledPanel)
        self.menuBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.menuBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(26, 0, 26, 0)
        self.fileMenu = QPushButton(self.menuBox)
        self.fileMenu.setObjectName(u"fileMenu")
        self.fileMenu.setStyleSheet(u"background-color:#2a2e37;\n"
"border-radius:24px;\n"
"padding:6px 0px;")

        self.horizontalLayout_6.addWidget(self.fileMenu)

        self.displayMenu = QPushButton(self.menuBox)
        self.displayMenu.setObjectName(u"displayMenu")
        self.displayMenu.setStyleSheet(u"background-color:#2a2e37;\n"
"border-radius:24px;\n"
"padding:6px 0px;")

        self.horizontalLayout_6.addWidget(self.displayMenu)

        self.toolsMenu = QPushButton(self.menuBox)
        self.toolsMenu.setObjectName(u"toolsMenu")
        self.toolsMenu.setStyleSheet(u"background-color:#2a2e37;\n"
"border-radius:24px;\n"
"padding:6px 0px;")

        self.horizontalLayout_6.addWidget(self.toolsMenu)

        self.settingsMenu = QPushButton(self.menuBox)
        self.settingsMenu.setObjectName(u"settingsMenu")
        self.settingsMenu.setStyleSheet(u"background-color:#2a2e37;\n"
"border-radius:24px;\n"
"padding:6px 0px;")

        self.horizontalLayout_6.addWidget(self.settingsMenu)

        self.helpMenu = QPushButton(self.menuBox)
        self.helpMenu.setObjectName(u"helpMenu")
        self.helpMenu.setStyleSheet(u"background-color:#2a2e37;\n"
"border-radius:24px;\n"
"padding:6px 0px;")

        self.horizontalLayout_6.addWidget(self.helpMenu)


        self.horizontalLayout.addWidget(self.menuBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        sizePolicy2.setHeightForWidth(self.rightButtons.sizePolicy().hasHeightForWidth())
        self.rightButtons.setSizePolicy(sizePolicy2)
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon3)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon4)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon5)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        self.horizontalLayout_7 = QHBoxLayout(self.start_page)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.start_left = QFrame(self.start_page)
        self.start_left.setObjectName(u"start_left")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.start_left.sizePolicy().hasHeightForWidth())
        self.start_left.setSizePolicy(sizePolicy5)
        self.start_left.setStyleSheet(u"")
        self.start_left.setFrameShape(QFrame.StyledPanel)
        self.start_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.start_left)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.start_left)
        self.top.setObjectName(u"top")
        sizePolicy1.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy1)
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.top)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_2 = QLabel(self.top)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size:26px;\n"
"font-weight:bold;")

        self.verticalLayout_22.addWidget(self.label_2)

        self.label_3 = QLabel(self.top)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-size:11px")

        self.verticalLayout_22.addWidget(self.label_3)


        self.verticalLayout_21.addWidget(self.top)

        self.middle = QFrame(self.start_left)
        self.middle.setObjectName(u"middle")
        sizePolicy1.setHeightForWidth(self.middle.sizePolicy().hasHeightForWidth())
        self.middle.setSizePolicy(sizePolicy1)
        self.middle.setFrameShape(QFrame.StyledPanel)
        self.middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.middle)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_4 = QLabel(self.middle)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-size:16px;\n"
"font-weight:bold;")

        self.verticalLayout_23.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.middle)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"")

        self.verticalLayout_23.addWidget(self.lineEdit_2)


        self.verticalLayout_21.addWidget(self.middle)

        self.bottom = QFrame(self.start_left)
        self.bottom.setObjectName(u"bottom")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(8)
        sizePolicy6.setHeightForWidth(self.bottom.sizePolicy().hasHeightForWidth())
        self.bottom.setSizePolicy(sizePolicy6)
        self.bottom.setStyleSheet(u"")
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.bottom)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_5 = QLabel(self.bottom)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setStyleSheet(u"font-size:16px;\n"
"font-weight:bold;")

        self.verticalLayout_26.addWidget(self.label_5)

        self.frame_7 = QFrame(self.bottom)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(6)
        sizePolicy7.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy7)
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_7)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 60))
        self.pushButton_2.setStyleSheet(u"font-size:11px;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-library.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon6)

        self.verticalLayout_27.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 60))
        self.pushButton_3.setStyleSheet(u"font-size:11px;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-view-quilt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon7)

        self.verticalLayout_27.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 60))
        self.pushButton_4.setStyleSheet(u"font-size:11px;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon8)

        self.verticalLayout_27.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 60))
        self.pushButton_5.setStyleSheet(u"font-size:11px;")

        self.verticalLayout_27.addWidget(self.pushButton_5)


        self.verticalLayout_26.addWidget(self.frame_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_2)


        self.verticalLayout_21.addWidget(self.bottom)


        self.horizontalLayout_7.addWidget(self.start_left)

        self.start_middle = QFrame(self.start_page)
        self.start_middle.setObjectName(u"start_middle")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(5)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.start_middle.sizePolicy().hasHeightForWidth())
        self.start_middle.setSizePolicy(sizePolicy8)
        self.start_middle.setStyleSheet(u"background-color: white;\n"
"border: none;")
        self.start_middle.setFrameShape(QFrame.StyledPanel)
        self.start_middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.start_middle)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.start_middle)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollBar:vertical{\n"
"	\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"	background-color:#595c64;\n"
"}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 274, 1200))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"")
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.middle_main = QFrame(self.scrollAreaWidgetContents_2)
        self.middle_main.setObjectName(u"middle_main")
        self.middle_main.setMinimumSize(QSize(0, 1200))
        self.middle_main.setStyleSheet(u"background-color:#f4f4f4;")
        self.middle_main.setFrameShape(QFrame.StyledPanel)
        self.middle_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.middle_main)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.guide_card01 = QFrame(self.middle_main)
        self.guide_card01.setObjectName(u"guide_card01")
        self.guide_card01.setMinimumSize(QSize(0, 160))
        self.guide_card01.setMaximumSize(QSize(16777215, 160))
        self.guide_card01.setStyleSheet(u"border:1px solid #f3f3f3;\n"
"background-color:white;\n"
"")
        self.guide_card01.setFrameShape(QFrame.StyledPanel)
        self.guide_card01.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.guide_card01)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.guide_card01)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 36))
        self.label_6.setStyleSheet(u"border: none;\n"
"font-size:21px;\n"
"color: rgba(0,0,0,0.8);\n"
"margin-left:6px;\n"
"")

        self.verticalLayout_29.addWidget(self.label_6)

        self.plainTextEdit_2 = QPlainTextEdit(self.guide_card01)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setStyleSheet(u"border: none;\n"
"font-size:12px;\n"
"color:rgba(0,0,0,0.3);\n"
"padding:0px 8px;")
        self.plainTextEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.plainTextEdit_2.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setOverwriteMode(True)

        self.verticalLayout_29.addWidget(self.plainTextEdit_2)

        self.frame_6 = QFrame(self.guide_card01)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border: none;\n"
"padding: 0;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(433, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.pushButton_6 = QPushButton(self.frame_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"font-size:10px;\n"
"background-color:#2a2e37;\n"
"padding:6px 12px;")

        self.horizontalLayout_8.addWidget(self.pushButton_6)


        self.verticalLayout_29.addWidget(self.frame_6)


        self.verticalLayout_28.addWidget(self.guide_card01)

        self.guide_card01_2 = QFrame(self.middle_main)
        self.guide_card01_2.setObjectName(u"guide_card01_2")
        self.guide_card01_2.setMinimumSize(QSize(0, 160))
        self.guide_card01_2.setMaximumSize(QSize(16777215, 160))
        self.guide_card01_2.setStyleSheet(u"border:1px solid #f3f3f3;\n"
"background-color:white;\n"
"")
        self.guide_card01_2.setFrameShape(QFrame.StyledPanel)
        self.guide_card01_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.guide_card01_2)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.guide_card01_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 36))
        self.label_7.setStyleSheet(u"border: none;\n"
"font-size:21px;\n"
"color: rgba(0,0,0,0.8);\n"
"margin-left:6px;\n"
"")

        self.verticalLayout_30.addWidget(self.label_7)

        self.plainTextEdit_3 = QPlainTextEdit(self.guide_card01_2)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setStyleSheet(u"border: none;\n"
"font-size:12px;\n"
"color:rgba(0,0,0,0.3);\n"
"padding:0px 8px;")
        self.plainTextEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.plainTextEdit_3.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setOverwriteMode(True)

        self.verticalLayout_30.addWidget(self.plainTextEdit_3)

        self.frame_8 = QFrame(self.guide_card01_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border: none;\n"
"padding: 0;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(434, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"font-size:10px;\n"
"background-color:#2a2e37;\n"
"padding:6px 12px;")

        self.horizontalLayout_10.addWidget(self.pushButton_7)


        self.verticalLayout_30.addWidget(self.frame_8)


        self.verticalLayout_28.addWidget(self.guide_card01_2)

        self.guide_card01_3 = QFrame(self.middle_main)
        self.guide_card01_3.setObjectName(u"guide_card01_3")
        self.guide_card01_3.setMinimumSize(QSize(0, 160))
        self.guide_card01_3.setMaximumSize(QSize(16777215, 160))
        self.guide_card01_3.setStyleSheet(u"border:1px solid #f3f3f3;\n"
"background-color:white;\n"
"")
        self.guide_card01_3.setFrameShape(QFrame.StyledPanel)
        self.guide_card01_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.guide_card01_3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.guide_card01_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 36))
        self.label_8.setStyleSheet(u"border: none;\n"
"font-size:21px;\n"
"color: rgba(0,0,0,0.8);\n"
"margin-left:6px;\n"
"")

        self.verticalLayout_31.addWidget(self.label_8)

        self.plainTextEdit_4 = QPlainTextEdit(self.guide_card01_3)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setStyleSheet(u"border: none;\n"
"font-size:12px;\n"
"color:rgba(0,0,0,0.3);\n"
"padding:0px 8px;")
        self.plainTextEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.plainTextEdit_4.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_4.setOverwriteMode(True)

        self.verticalLayout_31.addWidget(self.plainTextEdit_4)

        self.frame_9 = QFrame(self.guide_card01_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border: none;\n"
"padding: 0;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_3 = QSpacerItem(434, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.pushButton_8 = QPushButton(self.frame_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"font-size:10px;\n"
"background-color:#2a2e37;\n"
"padding:6px 12px;")

        self.horizontalLayout_13.addWidget(self.pushButton_8)


        self.verticalLayout_31.addWidget(self.frame_9)


        self.verticalLayout_28.addWidget(self.guide_card01_3)

        self.guide_card01_4 = QFrame(self.middle_main)
        self.guide_card01_4.setObjectName(u"guide_card01_4")
        self.guide_card01_4.setMinimumSize(QSize(0, 160))
        self.guide_card01_4.setMaximumSize(QSize(16777215, 160))
        self.guide_card01_4.setStyleSheet(u"border:1px solid #f3f3f3;\n"
"background-color:white;\n"
"")
        self.guide_card01_4.setFrameShape(QFrame.StyledPanel)
        self.guide_card01_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.guide_card01_4)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.guide_card01_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 36))
        self.label_9.setStyleSheet(u"border: none;\n"
"font-size:21px;\n"
"color: rgba(0,0,0,0.8);\n"
"margin-left:6px;\n"
"")

        self.verticalLayout_32.addWidget(self.label_9)

        self.plainTextEdit_5 = QPlainTextEdit(self.guide_card01_4)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setStyleSheet(u"border: none;\n"
"font-size:12px;\n"
"color:rgba(0,0,0,0.3);\n"
"padding:0px 8px;")
        self.plainTextEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.plainTextEdit_5.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self.plainTextEdit_5.setReadOnly(True)
        self.plainTextEdit_5.setOverwriteMode(True)

        self.verticalLayout_32.addWidget(self.plainTextEdit_5)

        self.frame_10 = QFrame(self.guide_card01_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border: none;\n"
"padding: 0;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_4 = QSpacerItem(434, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)

        self.pushButton_9 = QPushButton(self.frame_10)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"font-size:10px;\n"
"background-color:#2a2e37;\n"
"padding:6px 12px;")

        self.horizontalLayout_14.addWidget(self.pushButton_9)


        self.verticalLayout_32.addWidget(self.frame_10)


        self.verticalLayout_28.addWidget(self.guide_card01_4)

        self.verticalSpacer = QSpacerItem(20, 469, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer)


        self.verticalLayout_25.addWidget(self.middle_main)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_24.addWidget(self.scrollArea_2)


        self.horizontalLayout_7.addWidget(self.start_middle)

        self.start_right = QFrame(self.start_page)
        self.start_right.setObjectName(u"start_right")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(2)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.start_right.sizePolicy().hasHeightForWidth())
        self.start_right.setSizePolicy(sizePolicy9)
        self.start_right.setStyleSheet(u"background-color:#f4f4f4;")
        self.start_right.setFrameShape(QFrame.StyledPanel)
        self.start_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.start_right)

        self.stackedWidget.addWidget(self.start_page)
        
        
        
        
        self.emg_page = QWidget()
        self.emg_page.setObjectName(u"emg_page")
        self.horizontalLayout_16 = QHBoxLayout(self.emg_page)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.emg_left_body = QFrame(self.emg_page)
        self.emg_left_body.setObjectName(u"emg_left_body")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(7)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.emg_left_body.sizePolicy().hasHeightForWidth())
        self.emg_left_body.setSizePolicy(sizePolicy10)
        self.emg_left_body.setStyleSheet(u"")
        self.emg_left_body.setFrameShape(QFrame.StyledPanel)
        self.emg_left_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.emg_left_body)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.data_process = QFrame(self.emg_left_body)
        self.data_process.setObjectName(u"data_process")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(7)
        sizePolicy11.setHeightForWidth(self.data_process.sizePolicy().hasHeightForWidth())
        self.data_process.setSizePolicy(sizePolicy11)
        self.data_process.setStyleSheet(u"background-color:#f4f4f4;\n"
"border: none;")
        self.data_process.setFrameShape(QFrame.StyledPanel)
        self.data_process.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.data_process)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.data_process_graphic = QFrame(self.data_process)
        self.data_process_graphic.setObjectName(u"data_process_graphic")
        sizePolicy10.setHeightForWidth(self.data_process_graphic.sizePolicy().hasHeightForWidth())
        self.data_process_graphic.setSizePolicy(sizePolicy10)
        self.data_process_graphic.setFrameShape(QFrame.StyledPanel)
        self.data_process_graphic.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.data_process_graphic)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.data_process_graphic_top = QFrame(self.data_process_graphic)
        self.data_process_graphic_top.setObjectName(u"data_process_graphic_top")
        sizePolicy1.setHeightForWidth(self.data_process_graphic_top.sizePolicy().hasHeightForWidth())
        self.data_process_graphic_top.setSizePolicy(sizePolicy1)
        self.data_process_graphic_top.setFrameShape(QFrame.StyledPanel)
        self.data_process_graphic_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.data_process_graphic_top)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.data_process_graphic_top)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"border-bottom:1px solid rgba(0,0,0,0.1);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-weight: bold;\n"
"font-size:12px;\n"
"color: rgba(0,0,0,0.8);\n"
"margin-left: 4px;\n"
"border: none;")

        self.horizontalLayout_19.addWidget(self.label_11)

        self.horizontalSpacer_6 = QSpacerItem(524, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_6)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(226, 0))
        self.frame_11.setStyleSheet(u"border:none;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.comboBox_2 = QComboBox(self.frame_11)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font)
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:0;\n"
"font-size:12px;\n"
"color: rgba(0,0,0,0.8);\n")
        self.comboBox_2.setIconSize(QSize(16, 16))
        self.comboBox_2.setFrame(True)

        self.horizontalLayout_38.addWidget(self.comboBox_2)


        self.horizontalLayout_19.addWidget(self.frame_11)


        self.verticalLayout_40.addWidget(self.frame_2)

        self.plot_input = QPlotView()
        self.plot_input.setObjectName(u"QPlotView_input")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(9)
        sizePolicy12.setHeightForWidth(self.plot_input.sizePolicy().hasHeightForWidth())
        self.plot_input.setSizePolicy(sizePolicy12)

        self.verticalLayout_40.addWidget(self.plot_input)


        self.verticalLayout_39.addWidget(self.data_process_graphic_top)

        self.data_process_graphic_bottom = QFrame(self.data_process_graphic)
        self.data_process_graphic_bottom.setObjectName(u"data_process_graphic_bottom")
        sizePolicy1.setHeightForWidth(self.data_process_graphic_bottom.sizePolicy().hasHeightForWidth())
        self.data_process_graphic_bottom.setSizePolicy(sizePolicy1)
        self.data_process_graphic_bottom.setFrameShape(QFrame.StyledPanel)
        self.data_process_graphic_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.data_process_graphic_bottom)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.data_process_graphic_bottom)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setStyleSheet(u"border-bottom:1px solid rgba(0,0,0,0.1);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-weight: bold;\n"
"font-size:12px;\n"
"color: rgba(0,0,0,0.8);\n"
"margin-left: 4px;\n"
"border: none;")

        self.horizontalLayout_20.addWidget(self.label_12)

        self.horizontalSpacer_7 = QSpacerItem(530, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_7)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border:none;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_12)


        self.verticalLayout_41.addWidget(self.frame_4)

        self.plot_output = QPlotView()
        self.plot_output.setObjectName(u"QPlotView_output")
        sizePolicy12.setHeightForWidth(self.plot_output.sizePolicy().hasHeightForWidth())
        self.plot_output.setSizePolicy(sizePolicy12)

        self.verticalLayout_41.addWidget(self.plot_output)


        self.verticalLayout_39.addWidget(self.data_process_graphic_bottom)


        self.horizontalLayout_18.addWidget(self.data_process_graphic)

        self.data_process_instruction = QFrame(self.data_process)
        self.data_process_instruction.setObjectName(u"data_process_instruction")
        sizePolicy9.setHeightForWidth(self.data_process_instruction.sizePolicy().hasHeightForWidth())
        self.data_process_instruction.setSizePolicy(sizePolicy9)
        self.data_process_instruction.setStyleSheet(u"border-left:1px solid rgba(0,0,0,0.1);")
        self.data_process_instruction.setFrameShape(QFrame.StyledPanel)
        self.data_process_instruction.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.data_process_instruction)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.data_process_instruction)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBox.setStyleSheet(u"color: rgba(0,0,0,0.6);\n"
"border:none;\n"
"font-weight:bold;")
        self.toolBox.setFrameShape(QFrame.Box)
        self.toolBox.setFrameShadow(QFrame.Raised)
        self.toolBox.setLineWidth(1)
        self.page_1_remove_dc = QWidget()
        self.page_1_remove_dc.setObjectName(u"page_1_remove_dc")
        self.page_1_remove_dc.setGeometry(QRect(0, 0, 157, 286))
        self.verticalLayout_51 = QVBoxLayout(self.page_1_remove_dc)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.page_1_remove_dc)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_19)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.checkBox_4 = QCheckBox(self.frame_19)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy13)
        self.checkBox_4.setStyleSheet(u"font-weight:1;\n"
"font-size:12px;")

        self.verticalLayout_50.addWidget(self.checkBox_4)

        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font-weight:1;\n"
"font-size:12px;\n"
"margin-left:1px;")
        self.label_17.setWordWrap(True)

        self.verticalLayout_50.addWidget(self.label_17)


        self.verticalLayout_51.addWidget(self.frame_19)

        self.pushButton_19 = QPushButton(self.page_1_remove_dc)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(150, 40))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        self.pushButton_19.setFont(font5)
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:6px 6px;\n"
"border:1px solid rgba(0,0,0,0.1);\n"
"")

        self.verticalLayout_51.addWidget(self.pushButton_19)

        self.verticalSpacer_3 = QSpacerItem(20, 159, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacer_3)

        self.toolBox.addItem(self.page_1_remove_dc, u"\u00b7 Remove dc offset")
        self.page_2_full_wave = QWidget()
        self.page_2_full_wave.setObjectName(u"page_2_full_wave")
        self.page_2_full_wave.setGeometry(QRect(0, 0, 157, 286))
        self.verticalLayout_62 = QVBoxLayout(self.page_2_full_wave)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.page_2_full_wave)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_29)
#ifndef Q_OS_MAC
        self.verticalLayout_63.setSpacing(-1)
#endif
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.checkBox_11 = QCheckBox(self.frame_29)
        self.checkBox_11.setObjectName(u"checkBox_11")
        sizePolicy13.setHeightForWidth(self.checkBox_11.sizePolicy().hasHeightForWidth())
        self.checkBox_11.setSizePolicy(sizePolicy13)
        self.checkBox_11.setStyleSheet(u"font-weight:1;\n"
"font-size:12px;\n"
"margin:4px 12px;")

        self.verticalLayout_63.addWidget(self.checkBox_11)

        self.pushButton_20 = QPushButton(self.frame_29)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(150, 40))
        self.pushButton_20.setFont(font5)
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:6px 6px;\n"
"border:1px solid rgba(0,0,0,0.1);\n"
"")

        self.verticalLayout_63.addWidget(self.pushButton_20)

        self.verticalSpacer_4 = QSpacerItem(20, 219, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_4)


        self.verticalLayout_62.addWidget(self.frame_29)

        self.toolBox.addItem(self.page_2_full_wave, u"\u00b7 Full wave rectification")
        self.page_3_filter = QWidget()
        self.page_3_filter.setObjectName(u"page_3_filter")
        self.page_3_filter.setGeometry(QRect(0, 0, 157, 286))
        self.page_3_filter.setStyleSheet(u"QScrollBar::handle:vertical{ \n"
"    background: #353a45;\n"
"    visible:none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{ \n"
"    background: #353a45;\n"
"	visible:none;\n"
"   }")
        self.verticalLayout_43 = QVBoxLayout(self.page_3_filter)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page_3_filter)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_13)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, -1)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy13.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy13)
        self.frame_14.setStyleSheet(u"margin-bottom:4px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_14)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_14)
        self.label_34.setObjectName(u"label_34")
        sizePolicy13.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy13)
        self.label_34.setStyleSheet(u"margin-left:11px;\n"
"font-size:12px;\n"
"\n"
"font-weight:1;\n"
"")

        self.verticalLayout_58.addWidget(self.label_34)

        self.frame_40 = QFrame(self.frame_14)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy13.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy13)
        self.frame_40.setStyleSheet(u"font-weight:1;\n"
"margin:2px 0px;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_40)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)

        self.checkBox_13 = QCheckBox(self.frame_40)
        self.checkBox_13.setObjectName(u"checkBox_13")
        sizePolicy13.setHeightForWidth(self.checkBox_13.sizePolicy().hasHeightForWidth())
        self.checkBox_13.setSizePolicy(sizePolicy13)
        self.checkBox_13.setStyleSheet(u"font-weight:1;\n"
"font-size:12px;")
        self.verticalLayout_59.addWidget(self.checkBox_13)
        
        self.comboBox_7 = QComboBox(self.frame_40)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setFont(font3)
        self.comboBox_7.setAutoFillBackground(False)
        self.comboBox_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:0px 10px;\n"
"font-weight: bold;\n"
"font-size:12px;")
        self.comboBox_7.setIconSize(QSize(16, 16))
        self.comboBox_7.setFrame(True)

        self.verticalLayout_59.addWidget(self.comboBox_7)

        self.comboBox_8 = QComboBox(self.frame_40)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setFont(font3)
        self.comboBox_8.setAutoFillBackground(False)
        self.comboBox_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:0px 10px;\n"
"font-weight: bold;\n"
"font-size:12px;")
        self.comboBox_8.setIconSize(QSize(16, 16))
        self.comboBox_8.setFrame(True)

        self.verticalLayout_59.addWidget(self.comboBox_8)


        self.verticalLayout_58.addWidget(self.frame_40)


        self.verticalLayout_74.addWidget(self.frame_14)

        self.frame_41 = QFrame(self.frame_13)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy13.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy13)
        self.frame_41.setStyleSheet(u"margin:2px 0px;\n"
"")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_41)
#ifndef Q_OS_MAC
        self.verticalLayout_60.setSpacing(-1)
#endif
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_41)
        self.label_35.setObjectName(u"label_35")
        sizePolicy13.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy13)
        self.label_35.setStyleSheet(u"margin-left:11px;\n"
"font-size:12px;\n"
"\n"
"font-weight:1;\n"
"")

        self.verticalLayout_60.addWidget(self.label_35)

        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy13.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy13)
        self.frame_42.setStyleSheet(u"")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_42)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy13.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy13)
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_43)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_43)
        self.label_36.setObjectName(u"label_36")
        sizePolicy13.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy13)
        self.label_36.setStyleSheet(u"margin-left:12px;\n"
"font-weight:1;\n"
"font-size:12px;")

        self.verticalLayout_70.addWidget(self.label_36)

        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy13.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy13)
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_44)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(-1, 2, -1, 2)
        self.lineEdit_10 = QLineEdit(self.frame_44)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 30))
        self.lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:12px;")
        self.lineEdit_10.setMaxLength(16)

        self.verticalLayout_71.addWidget(self.lineEdit_10)

        self.lineEdit_11 = QLineEdit(self.frame_44)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 30))
        self.lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:12px;")
        self.lineEdit_11.setMaxLength(16)

        self.verticalLayout_71.addWidget(self.lineEdit_11)


        self.verticalLayout_70.addWidget(self.frame_44)


        self.verticalLayout_61.addWidget(self.frame_43)

        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy13.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy13)
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_45)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_45)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"margin-left:12px;\n"
"font-weight:1;\n"
"font-size:12px;")

        self.verticalLayout_72.addWidget(self.label_37)

        self.frame_46 = QFrame(self.frame_45)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_46)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(-1, 2, -1, 2)
        self.lineEdit_12 = QLineEdit(self.frame_46)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(0, 30))
        self.lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font-size:12px;")
        self.lineEdit_12.setMaxLength(16)

        self.verticalLayout_73.addWidget(self.lineEdit_12)


        self.verticalLayout_72.addWidget(self.frame_46)


        self.verticalLayout_61.addWidget(self.frame_45)


        self.verticalLayout_60.addWidget(self.frame_42)


        self.verticalLayout_74.addWidget(self.frame_41)

        self.pushButton_21 = QPushButton(self.frame_29)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(150, 40))
        self.pushButton_21.setFont(font5)
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:6px 6px;\n"
"border:1px solid rgba(0,0,0,0.1);\n"
"")
        self.verticalLayout_74.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_29)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(150, 40))
        self.pushButton_22.setFont(font5)
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:6px 6px;\n"
"border:1px solid rgba(0,0,0,0.1);\n"
"")
        self.verticalLayout_74.addWidget(self.pushButton_22)

        self.verticalSpacer_8 = QSpacerItem(20, 7, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_74.addItem(self.verticalSpacer_8)

        self.verticalLayout_43.addWidget(self.frame_13)
        

        self.toolBox.addItem(self.page_3_filter, u"\u00b7 Filter")
        self.page_4_norm = QWidget()
        self.page_4_norm.setObjectName(u"page_4_norm")
        self.page_4_norm.setGeometry(QRect(0, 0, 157, 286))
        self.verticalLayout_67 = QVBoxLayout(self.page_4_norm)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.page_4_norm)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_32)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.checkBox_12 = QCheckBox(self.frame_32)
        self.checkBox_12.setObjectName(u"checkBox_12")
        sizePolicy13.setHeightForWidth(self.checkBox_12.sizePolicy().hasHeightForWidth())
        self.checkBox_12.setSizePolicy(sizePolicy13)
        self.checkBox_12.setStyleSheet(u"font-weight:1;\n"
"font-size:12px;")

        self.verticalLayout_66.addWidget(self.checkBox_12)

        self.pushButton_23 = QPushButton(self.frame_32)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(150, 40))
        self.pushButton_23.setFont(font5)
        self.pushButton_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:6px 6px;\n"
"border:1px solid rgba(0,0,0,0.1);\n"
"")
        self.verticalLayout_66.addWidget(self.pushButton_23)

        self.verticalSpacer_5 = QSpacerItem(20, 219, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_66.addItem(self.verticalSpacer_5)


        self.verticalLayout_67.addWidget(self.frame_32)

        self.toolBox.addItem(self.page_4_norm, u"\u00b7 Normalization")
        self.page_5_activation = QWidget()
        self.page_5_activation.setObjectName(u"page_5_activation")
        self.page_5_activation.setGeometry(QRect(0, 0, 157, 286))
        self.verticalLayout_52 = QVBoxLayout(self.page_5_activation)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.page_5_activation)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"font-size:12px")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_20)
#ifndef Q_OS_MAC
        self.verticalLayout_53.setSpacing(-1)
#endif
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy13.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy13)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_21)
#ifndef Q_OS_MAC
        self.verticalLayout_68.setSpacing(-1)
#endif
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")
        sizePolicy13.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy13)
        self.label_18.setStyleSheet(u"margin-left:11px;\n"
"font-size:12px;\n"
"\n"
"font-weight:1;\n"
"")

        self.verticalLayout_68.addWidget(self.label_18)

        self.lineEdit_7 = QLineEdit(self.frame_21)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy13.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy13)
        self.lineEdit_7.setMinimumSize(QSize(0, 30))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:0px 10px;\n"
"font-weight: bold;")
        self.lineEdit_7.setMaxLength(16)

        self.verticalLayout_68.addWidget(self.lineEdit_7)


        self.verticalLayout_53.addWidget(self.frame_21)

        self.frame_33 = QFrame(self.frame_20)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy13.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy13)
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_33)
#ifndef Q_OS_MAC
        self.verticalLayout_69.setSpacing(-1)
#endif
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_33)
        self.label_19.setObjectName(u"label_19")
        sizePolicy13.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy13)
        self.label_19.setStyleSheet(u"margin-left:11px;\n"
"font-size:12px;\n"
"\n"
"font-weight:1;\n"
"")

        self.verticalLayout_69.addWidget(self.label_19)

        self.lineEdit_8 = QLineEdit(self.frame_33)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy13.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy13)
        self.lineEdit_8.setMinimumSize(QSize(0, 30))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:0px 10px;\n"
"font-weight:bold;")
        self.lineEdit_8.setMaxLength(16)

        self.verticalLayout_69.addWidget(self.lineEdit_8)

        self.label_20 = QLabel(self.frame_33)
        self.label_20.setObjectName(u"label_20")
        sizePolicy13.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy13)
        self.label_20.setStyleSheet(u"margin-left:11px;\n"
"font-size:12px;\n"
"\n"
"font-weight:1;\n"
"")

        self.verticalLayout_69.addWidget(self.label_20)

        self.lineEdit_9 = QLineEdit(self.frame_33)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy13.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy13)
        self.lineEdit_9.setMinimumSize(QSize(0, 30))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:0px 10px;\n"
"font-weight:bold;")
        self.lineEdit_9.setMaxLength(16)

        self.verticalLayout_69.addWidget(self.lineEdit_9)

        self.pushButton_24 = QPushButton(self.frame_33)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(150, 40))
        self.pushButton_24.setFont(font5)
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:6px 6px;\n"
"border:1px solid rgba(0,0,0,0.1);\n"
"")
        self.verticalLayout_69.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.frame_33)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(150, 40))
        self.pushButton_25.setFont(font5)
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:6px 6px;\n"
"border:1px solid rgba(0,0,0,0.1);\n"
"")
        self.verticalLayout_69.addWidget(self.pushButton_25)

        self.verticalLayout_53.addWidget(self.frame_33)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_6)

        self.verticalLayout_52.addWidget(self.frame_20)

        self.toolBox.addItem(self.page_5_activation, u"\u00b7 Activation")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 157, 286))
        self.verticalLayout_54 = QVBoxLayout(self.page_6)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.page_6)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"font-size:12px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_22)
#ifndef Q_OS_MAC
        self.verticalLayout_55.setSpacing(-1)
#endif
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(14, 0, 14, 0)
        self.frame_34 = QFrame(self.frame_22)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"font-weight:1;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_34)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_24.addWidget(self.label_22)

        self.horizontalSpacer_9 = QSpacerItem(90, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_9)

        self.label_23 = QLabel(self.frame_34)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_24.addWidget(self.label_23)


        self.verticalLayout_55.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_22)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"font-weight:1;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_35)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_25.addWidget(self.label_24)

        self.horizontalSpacer_10 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)

        self.label_25 = QLabel(self.frame_35)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_25.addWidget(self.label_25)


        self.verticalLayout_55.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_22)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"font-weight:1;")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.frame_36)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_26.addWidget(self.label_26)

        self.horizontalSpacer_11 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_11)

        self.label_27 = QLabel(self.frame_36)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_26.addWidget(self.label_27)


        self.verticalLayout_55.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_22)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"font-weight:1;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_37)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_27.addWidget(self.label_28)

        self.horizontalSpacer_12 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_12)

        self.label_29 = QLabel(self.frame_37)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_27.addWidget(self.label_29)


        self.verticalLayout_55.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_22)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"font-weight:1;")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_38)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_28.addWidget(self.label_30)

        self.horizontalSpacer_13 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_13)

        self.label_31 = QLabel(self.frame_38)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_28.addWidget(self.label_31)


        self.verticalLayout_55.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_22)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"font-weight:1;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_39)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_29.addWidget(self.label_32)

        self.horizontalSpacer_14 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_14)

        self.label_33 = QLabel(self.frame_39)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_29.addWidget(self.label_33)


        self.verticalLayout_55.addWidget(self.frame_39)

        self.pushButton_26 = QPushButton(self.frame_22)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(150, 40))
        self.pushButton_26.setFont(font5)
        self.pushButton_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_26.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:6px 6px;\n"
"border:1px solid rgba(0,0,0,0.1);\n"
"")
        self.verticalLayout_55.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.frame_22)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(150, 40))
        self.pushButton_27.setFont(font5)
        self.pushButton_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_27.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin:6px 6px;\n"
"border:1px solid rgba(0,0,0,0.1);\n"
"")
        self.verticalLayout_55.addWidget(self.pushButton_27)

        self.verticalSpacer_7 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_7)


        self.verticalLayout_54.addWidget(self.frame_22)

        self.toolBox.addItem(self.page_6, u"\u00b7 Summary")

        self.verticalLayout_42.addWidget(self.toolBox)


        self.horizontalLayout_18.addWidget(self.data_process_instruction)


        self.verticalLayout_33.addWidget(self.data_process)

        self.configuration_list = QFrame(self.emg_left_body)
        self.configuration_list.setObjectName(u"configuration_list")
        sizePolicy14 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(3)
        sizePolicy14.setHeightForWidth(self.configuration_list.sizePolicy().hasHeightForWidth())
        self.configuration_list.setSizePolicy(sizePolicy14)
        self.configuration_list.setStyleSheet(u"background-color:#f4f4f4;\n"
"border:none;")
        self.configuration_list.setFrameShape(QFrame.StyledPanel)
        self.configuration_list.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.configuration_list)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.list_title = QFrame(self.configuration_list)
        self.list_title.setObjectName(u"list_title")
        sizePolicy1.setHeightForWidth(self.list_title.sizePolicy().hasHeightForWidth())
        self.list_title.setSizePolicy(sizePolicy1)
        self.list_title.setStyleSheet(u"border-bottom:1px solid rgba(0,0,0,0.1)")
        self.list_title.setFrameShape(QFrame.StyledPanel)
        self.list_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.list_title)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.list_title)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-weight: bold;\n"
"font-size:12px;\n"
"color: rgba(0,0,0,0.8);\n"
"margin-left: 4px;\n"
"border: none;")

        self.horizontalLayout_23.addWidget(self.label_10)

        self.horizontalSpacer_5 = QSpacerItem(680, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_5)

        self.frame = QFrame(self.list_title)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: none;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"background-color:rgba(0,0,0,0.8);\n"
"margin:3px 2px;")
        self.pushButton_14.setIcon(icon1)

        self.horizontalLayout_17.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.frame)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"background-color:rgba(0,0,0,0.8);\n"
"margin:3px 2px;\n"
"")
        self.pushButton_13.setIcon(icon2)

        self.horizontalLayout_17.addWidget(self.pushButton_13)


        self.horizontalLayout_23.addWidget(self.frame)


        self.verticalLayout_37.addWidget(self.list_title)

        self.list_body = QFrame(self.configuration_list)
        self.list_body.setObjectName(u"list_body")
        sizePolicy12.setHeightForWidth(self.list_body.sizePolicy().hasHeightForWidth())
        self.list_body.setSizePolicy(sizePolicy12)
        self.list_body.setFrameShape(QFrame.StyledPanel)
        self.list_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.list_body)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.list_body)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"font-size:11px;\n"
"color:rgba(0,0,0,0.5);\n"
"")
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)

        self.verticalLayout_38.addWidget(self.listWidget)


        self.verticalLayout_37.addWidget(self.list_body)


        self.verticalLayout_33.addWidget(self.configuration_list)


        self.horizontalLayout_16.addWidget(self.emg_left_body)

        self.emg_right_body = QFrame(self.emg_page)
        self.emg_right_body.setObjectName(u"emg_right_body")
        sizePolicy5.setHeightForWidth(self.emg_right_body.sizePolicy().hasHeightForWidth())
        self.emg_right_body.setSizePolicy(sizePolicy5)
        self.emg_right_body.setStyleSheet(u"")
        self.emg_right_body.setFrameShape(QFrame.StyledPanel)
        self.emg_right_body.setFrameShadow(QFrame.Raised)
        self.emg_right_body.setLineWidth(1)
        self.verticalLayout_34 = QVBoxLayout(self.emg_right_body)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.emg_right_body)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy11.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy11)
        self.frame_23.setStyleSheet(u"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_23)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.emg_right_btn_group = QFrame(self.frame_23)
        self.emg_right_btn_group.setObjectName(u"emg_right_btn_group")
        sizePolicy14.setHeightForWidth(self.emg_right_btn_group.sizePolicy().hasHeightForWidth())
        self.emg_right_btn_group.setSizePolicy(sizePolicy14)
        self.emg_right_btn_group.setStyleSheet(u"")
        self.emg_right_btn_group.setFrameShape(QFrame.StyledPanel)
        self.emg_right_btn_group.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.emg_right_btn_group)
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.verticalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.emg_right_btn_group)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_47)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_47)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy13.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy13)
        self.pushButton_10.setMinimumSize(QSize(0, 56))
        self.pushButton_10.setMaximumSize(QSize(16777215, 56))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon9)

        self.verticalLayout_35.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_47)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy13.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy13)
        self.pushButton_11.setMinimumSize(QSize(0, 56))
        self.pushButton_11.setMaximumSize(QSize(16777215, 56))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon10)

        self.verticalLayout_35.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_47)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy13.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy13)
        self.pushButton_12.setMinimumSize(QSize(0, 56))
        self.pushButton_12.setMaximumSize(QSize(16777215, 56))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon11)

        self.verticalLayout_35.addWidget(self.pushButton_12)


        self.verticalLayout_75.addWidget(self.frame_47)

        self.verticalSpacer_9 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_75.addItem(self.verticalSpacer_9)


        self.verticalLayout_36.addWidget(self.emg_right_btn_group)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy15 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(5)
        sizePolicy15.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy15)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_24)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"margin:2px 0px;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_26)
#ifndef Q_OS_MAC
        self.horizontalLayout_21.setSpacing(-1)
#endif
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_26)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy16 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy16.setHorizontalStretch(8)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy16)
        self.lineEdit_3.setMinimumSize(QSize(0, 40))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"")

        self.horizontalLayout_21.addWidget(self.lineEdit_3)


        self.verticalLayout_76.addWidget(self.frame_26)

        self.frame_48 = QFrame(self.frame_24)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"margin:4px 0px;")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_48)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frame_48)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"margin-top:2px;\n"
"margin-bottom:2px;")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.checkBox_2 = QCheckBox(self.frame_49)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setStyleSheet(u"border-radius:0;")

        self.horizontalLayout_31.addWidget(self.checkBox_2)

        self.horizontalSpacer_15 = QSpacerItem(259, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_15)

        self.pushButton_16 = QPushButton(self.frame_49)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"background-color:rgba(0,0,0,0.8);\n"
"margin:3px 2px;")
        self.pushButton_16.setIcon(icon1)

        self.horizontalLayout_31.addWidget(self.pushButton_16)


        self.verticalLayout_56.addWidget(self.frame_49)

        self.tableWidget_2 = QTableWidget(self.frame_48)
        self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget_2.rowCount() < 16):
            self.tableWidget_2.setRowCount(16)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem22)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy17 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy17)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.tableWidget_2.setPalette(palette)
        self.tableWidget_2.setStyleSheet(u"\n"
"\n"
"QScrollBar::handle:vertical{ \n"
"    background: #353a45;\n"
"    \n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{ \n"
"    background: #353a45;\n"
"    \n"
"}\n"
"\n"
"QTableWidget::item:selected\n"
"{\n"
"    color:#ff0000;\n"
"    background:#454a55;\n"
"}\n"
"\n"
"")
        self.tableWidget_2.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(66)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(106)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)

        self.verticalLayout_56.addWidget(self.tableWidget_2)


        self.verticalLayout_76.addWidget(self.frame_48)


        self.verticalLayout_36.addWidget(self.frame_24)


        self.verticalLayout_34.addWidget(self.frame_23)

        self.frame_25 = QFrame(self.emg_right_body)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy14.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy14)
        self.frame_25.setStyleSheet(u"background-color:#f4f4f4;\n"
"border: none;\n"
"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_25)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy1.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy1)
        self.frame_27.setStyleSheet(u"border-bottom:1px solid rgba(0,0,0,0.1);\n"
"margin-top:2px;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_27)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font-weight: bold;\n"
"font-size:12px;\n"
"color: rgba(0,0,0,0.8);\n"
"margin-left: 4px;\n"
"border: none;")

        self.horizontalLayout_22.addWidget(self.label_21)

        self.horizontalSpacer_8 = QSpacerItem(227, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_8)

        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"border:none;")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.pushButton_15 = QPushButton(self.frame_28)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"background-color:rgba(0,0,0,0.8);\n"
"margin:3px 2px;")
        self.pushButton_15.setIcon(icon1)

        self.horizontalLayout_30.addWidget(self.pushButton_15)


        self.horizontalLayout_22.addWidget(self.frame_28)


        self.verticalLayout_57.addWidget(self.frame_27)

        self.listWidget_2 = QListWidget(self.frame_25)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy12.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy12)
        self.listWidget_2.setStyleSheet(u"font-size:11px;\n"
"color:rgba(0,0,0,0.5);\n"
"")

        self.verticalLayout_57.addWidget(self.listWidget_2)


        self.verticalLayout_34.addWidget(self.frame_25)


        self.horizontalLayout_16.addWidget(self.emg_right_body)

        self.stackedWidget.addWidget(self.emg_page)
        
        self.kinematics_page = QWidget()
        self.kinematics_page.setObjectName(u"kinematics_page")
        self.horizontalLayout_36 = QHBoxLayout(self.kinematics_page)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.kinematics_left = QFrame(self.kinematics_page)
        self.kinematics_left.setObjectName(u"kinematics_left")
        sizePolicy18 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy18.setHorizontalStretch(8)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.kinematics_left.sizePolicy().hasHeightForWidth())
        self.kinematics_left.setSizePolicy(sizePolicy18)
        self.kinematics_left.setStyleSheet(u"\n"
"border:none;")
        self.kinematics_left.setFrameShape(QFrame.StyledPanel)
        self.kinematics_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.kinematics_left)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.kinematics_left_top = QFrame(self.kinematics_left)
        self.kinematics_left_top.setObjectName(u"kinematics_left_top")
        sizePolicy12.setHeightForWidth(self.kinematics_left_top.sizePolicy().hasHeightForWidth())
        self.kinematics_left_top.setSizePolicy(sizePolicy12)
        self.kinematics_left_top.setStyleSheet(u"background-color:#f4f4f4;")
        self.kinematics_left_top.setFrameShape(QFrame.StyledPanel)
        self.kinematics_left_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.kinematics_left_top)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.kinematics_render = QFrame(self.kinematics_left_top)
        self.kinematics_render.setObjectName(u"kinematics_render")
        self.kinematics_render.setStyleSheet(u"background-color:rgba(0,0,0,0.9);")
        self.kinematics_render.setFrameShape(QFrame.StyledPanel)
        self.kinematics_render.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.kinematics_render)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.renderWidget = RenderWidget(self.kinematics_render)
        # self.openGLWidget = BodyRender(self.kinematics_render)
        # self.openGLWidget.setObjectName(u"openGLWidget")

        self.verticalLayout_48.addWidget(self.renderWidget)


        self.horizontalLayout_37.addWidget(self.kinematics_render)

        self.kinematics_graphs = QFrame(self.kinematics_left_top)
        self.kinematics_graphs.setObjectName(u"kinematics_graphs")
        self.kinematics_graphs.setFrameShape(QFrame.StyledPanel)
        self.kinematics_graphs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.kinematics_graphs)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.graph_top = QFrame(self.kinematics_graphs)
        self.graph_top.setObjectName(u"graph_top")
        sizePolicy1.setHeightForWidth(self.graph_top.sizePolicy().hasHeightForWidth())
        self.graph_top.setSizePolicy(sizePolicy1)
        self.graph_top.setFrameShape(QFrame.StyledPanel)
        self.graph_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.graph_top)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.graph_top_title = QFrame(self.graph_top)
        self.graph_top_title.setObjectName(u"graph_top_title")
        sizePolicy1.setHeightForWidth(self.graph_top_title.sizePolicy().hasHeightForWidth())
        self.graph_top_title.setSizePolicy(sizePolicy1)
        self.graph_top_title.setFrameShape(QFrame.StyledPanel)
        self.graph_top_title.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.graph_top_title)
        
        self.label_current_process = QLabel()
        self.label_current_process.setAlignment(Qt.AlignCenter)
        self.label_current_process.setText("Current Process")
        self.label_current_process.setObjectName(u"label_11")
        self.label_current_process.setStyleSheet(u"font-weight: bold;\n"
"font-size:12px;\n"
"color: rgba(0,0,0,0.8);\n"
"margin-left: 4px;\n"
"border: none;")
        
        self.horizontalLayout_kcp = QHBoxLayout()
        self.horizontalLayout_kcp
        self.horizontalLayout_kcp.setSpacing(0)
        self.horizontalLayout_kcp.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_kcp.addWidget(self.label_current_process)
        self.graph_top_title.setLayout(self.horizontalLayout_kcp)
        self.graph_top_body = QFrame(self.graph_top)
        self.graph_top_body.setObjectName(u"graph_top_body")
        sizePolicy12.setHeightForWidth(self.graph_top_body.sizePolicy().hasHeightForWidth())
        self.graph_top_body.setSizePolicy(sizePolicy12)
        self.graph_top_body.setFrameShape(QFrame.StyledPanel)
        self.graph_top_body.setFrameShadow(QFrame.Raised)
        self.kinematic_analysis = QPlotView()
        self.kinematic_analysis.setObjectName(u"QPlotView_input")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(9)
        sizePolicy12.setHeightForWidth(self.kinematic_analysis.sizePolicy().hasHeightForWidth())
        self.kinematic_analysis.setSizePolicy(sizePolicy12)
        self.verticalLayout_46.addWidget(self.kinematic_analysis)
        self.verticalLayout_45.addWidget(self.graph_top)
        self.graph_bottom = QFrame(self.kinematics_graphs)
        self.graph_bottom.setObjectName(u"graph_bottom")
        sizePolicy1.setHeightForWidth(self.graph_bottom.sizePolicy().hasHeightForWidth())
        self.graph_bottom.setSizePolicy(sizePolicy1)
        self.graph_bottom.setFrameShape(QFrame.StyledPanel)
        self.graph_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.graph_bottom)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.graph_bottom_title = QFrame(self.graph_bottom)
        self.graph_bottom_title.setObjectName(u"graph_bottom_title")
        sizePolicy1.setHeightForWidth(self.graph_bottom_title.sizePolicy().hasHeightForWidth())
        self.graph_bottom_title.setSizePolicy(sizePolicy1)
        self.graph_bottom_title.setFrameShape(QFrame.StyledPanel)
        self.graph_bottom_title.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.graph_bottom_title)

        self.graph_bottom_body = QFrame(self.graph_bottom)
        self.graph_bottom_body.setObjectName(u"graph_bottom_body")
        sizePolicy12.setHeightForWidth(self.graph_bottom_body.sizePolicy().hasHeightForWidth())
        self.graph_bottom_body.setSizePolicy(sizePolicy12)
        self.graph_bottom_body.setFrameShape(QFrame.StyledPanel)
        self.graph_bottom_body.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.graph_bottom_body)


        self.verticalLayout_45.addWidget(self.graph_bottom)


        self.horizontalLayout_37.addWidget(self.kinematics_graphs)


        self.verticalLayout_44.addWidget(self.kinematics_left_top)

        self.kinematics_left_bottom = QFrame(self.kinematics_left)
        self.kinematics_left_bottom.setObjectName(u"kinematics_left_bottom")
        sizePolicy1.setHeightForWidth(self.kinematics_left_bottom.sizePolicy().hasHeightForWidth())
        self.kinematics_left_bottom.setSizePolicy(sizePolicy1)
        self.kinematics_left_bottom.setStyleSheet(u"")
        self.kinematics_left_bottom.setFrameShape(QFrame.StyledPanel)
        self.kinematics_left_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.kinematics_left_bottom)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        # Control bar
        self.playSlider = PlayBarWidget(self.kinematics_left_bottom)
        self.playSlider.setObjectName(u"playSlider")
        self.playSlider.setStyleSheet(u"")

        self.verticalLayout_49.addWidget(self.playSlider)


        self.verticalLayout_44.addWidget(self.kinematics_left_bottom)


        self.horizontalLayout_36.addWidget(self.kinematics_left)

        self.kinematics_right = QFrame(self.kinematics_page)
        self.kinematics_right.setObjectName(u"kinematics_right")
        sizePolicy9.setHeightForWidth(self.kinematics_right.sizePolicy().hasHeightForWidth())
        self.kinematics_right.setSizePolicy(sizePolicy9)
        self.kinematics_right.setStyleSheet(u"background-color:#f4f4f4;\n"
"border:none;")
        self.kinematics_right.setFrameShape(QFrame.StyledPanel)
        self.kinematics_right.setFrameShadow(QFrame.Raised)
        tmp_verticalLayout_50 = QVBoxLayout(self.kinematics_right)
        
        self.kinematics_label_tree = QTreeWidget(self.kinematics_right)
        self.kinematics_label_tree.setObjectName(u"kinematics_labels")
        self.kinematics_label_tree.setStyleSheet(u"font-size:11px;\n"
"color:rgba(#f4f4f4);")
        self.kinematics_label_tree.setFrameShape(QFrame.NoFrame)
        self.kinematics_label_tree.setFrameShadow(QFrame.Sunken)
        self.kinematics_label_tree.setLineWidth(1)
        self.kinematics_label_tree.setMidLineWidth(0)
        self.kinematics_label_tree.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.kinematics_label_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.kinematics_label_tree.setSelectionMode(QAbstractItemView.SingleSelection)
        tmp_verticalLayout_50.addWidget(self.kinematics_label_tree)
        self.horizontalLayout_36.addWidget(self.kinematics_right)
        self.stackedWidget.addWidget(self.kinematics_page)
        
        
        self.stats_page = RServerBrowser()
        self.stats_page.setObjectName(u"stats_page")

        self.stackedWidget.addWidget(self.stats_page)
        
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton.setIcon(icon9)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 224, 224))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon12)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font6);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem46)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy17.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy17)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)

        self.frequency_page = QWidget()
        self.frequency_page.setObjectName(u"frequency_page")
        self.horizontalLayout_40 = QHBoxLayout(self.frequency_page)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frequency_left = QFrame(self.frequency_page)
        self.frequency_left.setObjectName(u"frequency_left")
        sizePolicy18.setHeightForWidth(self.frequency_left.sizePolicy().hasHeightForWidth())
        self.frequency_left.setSizePolicy(sizePolicy18)
        self.frequency_left.setStyleSheet(u"border: none;")
        self.frequency_left.setFrameShape(QFrame.StyledPanel)
        self.frequency_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frequency_left)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)

        self.frequency_top = QFrame(self.frequency_left)
        self.frequency_top.setObjectName(u"frequency_top")
        sizePolicy19 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy19.setHorizontalStretch(0)
        sizePolicy19.setVerticalStretch(2)
        sizePolicy19.setHeightForWidth(self.frequency_top.sizePolicy().hasHeightForWidth())
        self.frequency_top.setSizePolicy(sizePolicy19)
        self.frequency_top.setStyleSheet(u"background-color:#f4f4f4;")
        self.frequency_top.setFrameShape(QFrame.StyledPanel)
        self.frequency_top.setFrameShadow(QFrame.Raised)

        self.verticalLayout_141 = QVBoxLayout(self.frequency_top)
        self.freq_timedomain = QPlotView()
        self.freq_timedomain.setObjectName(u"QPlotView_Freq_Timedomain")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(9)
        sizePolicy12.setHeightForWidth(self.freq_timedomain.sizePolicy().hasHeightForWidth())
        self.freq_timedomain.setSizePolicy(sizePolicy12)

        self.verticalLayout_141.addWidget(self.freq_timedomain)

        self.freq_plot_control = QWidget()
        self.horizontalLayout_141 = QHBoxLayout(self.freq_plot_control)

        self.freq_left_text = QLabel()
        self.freq_left_text.setObjectName(u"freq_left_text")
        sizePolicy16 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.freq_left_text.setSizePolicy(sizePolicy16)
        self.freq_left_text.setStyleSheet(u"margin-left:11px;\n"
"font-size:12px;\n"
"\n"
"font-weight:1;\n"
"")
        self.horizontalLayout_141.addWidget(self.freq_left_text)

        self.freq_left = QLineEdit()
        self.freq_left.setObjectName(u"freq_left")
        sizePolicy16 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy16.setHorizontalStretch(8)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.freq_left.sizePolicy().hasHeightForWidth())
        self.freq_left.setSizePolicy(sizePolicy16)
        self.freq_left.setMinimumSize(QSize(0, 40))
        self.freq_left.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"")
        self.freq_left.setMaxLength(16)
 
        self.horizontalLayout_141.addWidget(self.freq_left)

        self.freq_right_text = QLabel()
        self.freq_right_text.setObjectName(u"freq_right_text")
        sizePolicy16 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.freq_right_text.setSizePolicy(sizePolicy16)
        self.freq_right_text.setStyleSheet(u"margin-left:11px;\n"
"font-size:12px;\n"
"\n"
"font-weight:1;\n"
"")
        self.horizontalLayout_141.addWidget(self.freq_right_text)

        self.freq_right = QLineEdit()
        self.freq_right.setObjectName(u"freq_right")
        sizePolicy16 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy16.setHorizontalStretch(8)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.freq_right.sizePolicy().hasHeightForWidth())
        self.freq_right.setSizePolicy(sizePolicy16)
        self.freq_right.setMinimumSize(QSize(0, 40))
        self.freq_right.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"")
        self.freq_right.setMaxLength(16)

        self.horizontalLayout_141.addWidget(self.freq_right)

        self.freq_add = QPushButton()
        self.freq_add.setObjectName(u"freq_add")
        self.freq_add.setStyleSheet(u"font-size:10px;\n"
"background-color:#2a2e37;\n"
"padding:6px 12px;")
        sizePolicy16.setHeightForWidth(self.freq_right.sizePolicy().hasHeightForWidth())
        self.freq_add.setSizePolicy(sizePolicy16)
        self.horizontalLayout_141.addWidget(self.freq_add)
        self.verticalLayout_141.addWidget(self.freq_plot_control)

        self.verticalLayout_20.addWidget(self.frequency_top)

        self.frequency_bottom = QFrame(self.frequency_left)
        self.frequency_bottom.setObjectName(u"frequency_bottom")
        sizePolicy20 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy20.setHorizontalStretch(0)
        sizePolicy20.setVerticalStretch(4)
        sizePolicy20.setHeightForWidth(self.frequency_bottom.sizePolicy().hasHeightForWidth())
        self.frequency_bottom.setSizePolicy(sizePolicy20)
        self.frequency_bottom.setStyleSheet(u"background-color:#f4f4f4;")
        self.frequency_bottom.setFrameShape(QFrame.StyledPanel)
        self.frequency_bottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_142 = QVBoxLayout(self.frequency_bottom)

        self.verticalLayout_20.addWidget(self.frequency_bottom)

        self.horizontalLayout_40.addWidget(self.frequency_left)

        self.frequency_right = QFrame(self.frequency_page)
        self.frequency_right.setObjectName(u"frequency_right")
        sizePolicy9.setHeightForWidth(self.frequency_right.sizePolicy().hasHeightForWidth())
        self.frequency_right.setSizePolicy(sizePolicy9)
        self.frequency_right.setStyleSheet(u"background-color:#f4f4f4;")
        self.frequency_right.setFrameShape(QFrame.StyledPanel)
        self.frequency_right.setFrameShadow(QFrame.Raised)

        self.verticalLayout_140 = QVBoxLayout(self.frequency_right)
        self.frequency_participants = QTreeWidget()
        self.frequency_participants.setObjectName(u"frequency_participants")
        self.frequency_participants.setStyleSheet(u"font-size:11px;\n"
"color:rgba(#f4f4f4);")
        self.frequency_participants.setFrameShape(QFrame.NoFrame)
        self.frequency_participants.setFrameShadow(QFrame.Sunken)
        self.frequency_participants.setLineWidth(1)    
        self.frequency_participants.setMidLineWidth(0)
        self.frequency_participants.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.frequency_participants.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.frequency_participants.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_140.addWidget(self.frequency_participants)
        self.horizontalLayout_40.addWidget(self.frequency_right)

        self.stackedWidget.addWidget(self.frequency_page)

        '''
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.new_page)
        '''

        self.verticalLayout_15.addWidget(self.stackedWidget)
        

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font2)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_35.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"MSK Integrated Analysis", None))
        self.toggleButton.setText("")
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Quick Start", None))
        self.btn_emg.setText(QCoreApplication.translate("MainWindow", u"EMG Data Analysis", None))
        self.btn_kinematic.setText(QCoreApplication.translate("MainWindow", u"Kinematic Data Analysis", None))
        self.btn_frequency.setText(QCoreApplication.translate("MainWindow", u"Frequency Domain Analysis", None))
        self.btn_advanced.setText(QCoreApplication.translate("MainWindow", u"Advanced Signal Analysis", None))
        self.btn_stats.setText(QCoreApplication.translate("MainWindow", u"Statistical Analysis", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Extra ", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"WORKSPACE", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New Workspace", None))
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Save Workspace", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Load Workspace", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Workspace", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Participant List", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"MYOTION", None))
        self.fileMenu.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.displayMenu.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.toolsMenu.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.settingsMenu.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.helpMenu.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hello, Member", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to MSK workplace, let's get started!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Quick Search", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Quick Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"  Batch processing", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" Data visualization", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u" Tutorial ", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CTO Photos", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"How to use Myotion ...", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Learn More", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"How to use Myotion ...", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Learn More", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"How to use Myotion ...", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Learn More", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"How to use Myotion ...", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Learn More", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Previous Process", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Current Process", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u" Click to process", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"[Value] of dc offset that is removed.", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1_remove_dc), QCoreApplication.translate("MainWindow", u"\u00b7 Remove dc offset", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u" Click to process", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Save Configuration", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2_full_wave), QCoreApplication.translate("MainWindow", u"\u00b7 Full wave rectification", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"-Filter Type-", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"Band Pass", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"Low Pass", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Order 2", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Order 3", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Order 4", None))

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"-Cut-off frequency-", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"band pass:", None))
        self.freq_left_text.setText(QCoreApplication.translate("MainWindow", u"Time Start:", None))
        self.freq_right_text.setText(QCoreApplication.translate("MainWindow", u"Time End:", None))
        self.freq_add.setText(QCoreApplication.translate("MainWindow", u"Add Frequency Plot", None))
        self.lineEdit_10.setInputMask("")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cut-off frequency high", None))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cut-off frequency low", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Low Pass:", None))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cut-off frequency low", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3_filter), QCoreApplication.translate("MainWindow", u"\u00b7 Filter", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u" Click to process", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u" Click to process", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4_norm), QCoreApplication.translate("MainWindow", u"\u00b7 Normalization", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Threhold", None))
        self.lineEdit_7.setInputMask("")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input threhold here", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"n_above", None))
        self.lineEdit_8.setInputMask("")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input n_above here", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"n_below", None))
        self.lineEdit_9.setInputMask("")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input n_below here", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5_activation), QCoreApplication.translate("MainWindow", u"\u00b7 Activation", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"[Value]", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"[Value]", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Med:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"[Value]", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Rms:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"[Value]", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Peak-to-peak:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"[Value]", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Zero-crossing:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"[Value]", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"\u00b7 Summary", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Configuration Log", None))
        self.pushButton_14.setText("")
        self.pushButton_13.setText("")

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"1. remove dc offset", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"2. full wave rectification", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"LOAD EMG DATA", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"SIGNAL PROCESS", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"BATCH PROCESS", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Participant here", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Select All", None))
        self.pushButton_16.setText("")
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Selected", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Participant", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Data Valid", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Report", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget_2.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget_2.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget_2.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget_2.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget_2.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"David Lee", None));
        ___qtablewidgetitem21 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Yes", None));
        ___qtablewidgetitem22 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Yes", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Configuration File", None))
        self.pushButton_15.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem24 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem25 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem26 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem27 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem36 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem37 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem38 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem39 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem40 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem41 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem42 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem43 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem44 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem45 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem46 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled2)

        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"Copyright by Accmov Health Inc.", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

