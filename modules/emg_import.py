# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emg_import.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(646, 487)
        Form.setStyleSheet(u"background-color:#2c3039;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top = QFrame(Form)
        self.top.setObjectName(u"top")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.top.sizePolicy().hasHeightForWidth())
        self.top.setSizePolicy(sizePolicy)
        self.top.setStyleSheet(u"border:none;")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.top)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.input = QFrame(self.top)
        self.input.setObjectName(u"input")
        self.input.setFrameShape(QFrame.StyledPanel)
        self.input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.input)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name = QFrame(self.input)
        self.name.setObjectName(u"name")
        self.name.setFrameShape(QFrame.StyledPanel)
        self.name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.name)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.name)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight:bold;\n"
"color:#f4f4f4;\n"
"font-size:18px;")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_3 = QLineEdit(self.name)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(8)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy1)
        self.lineEdit_3.setMinimumSize(QSize(180, 32))
        self.lineEdit_3.setStyleSheet(u"background-color: rgba(255,255,255,1);\n"
                                      "font-size:18px;")

        self.horizontalLayout.addWidget(self.lineEdit_3)


        self.horizontalLayout_2.addWidget(self.name)

        self.horizontalSpacer = QSpacerItem(213, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.import_btn = QPushButton(self.input)
        self.import_btn.setObjectName(u"import_btn")
        self.import_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.import_btn.setStyleSheet(u"color:#f4f4f4;\n"
"background-color: #333b46;\n"
"padding:8px 8px;\n"
"marging:2px 2px;\n"
"border-radius:8px;")
        icon = QIcon()
        icon.addFile(u"images/icons/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.import_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.import_btn)

        self.importMVC_btn = QPushButton(self.input)
        self.importMVC_btn.setObjectName(u"importMVC_btn")
        self.importMVC_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.importMVC_btn.setStyleSheet(u"color:#f4f4f4;\n"
"background-color: #333b46;\n"
"padding:8px 8px;\n"
"marging:2px 2px;\n"
"border-radius:8px;")
        self.importMVC_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.importMVC_btn)

        self.verticalLayout_3.addWidget(self.input)

        self.path = QFrame(self.top)
        self.path.setObjectName(u"path")
        self.path.setFrameShape(QFrame.StyledPanel)
        self.path.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.path)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.path)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-weight: 1;\n"
"font-size:18px;\n"
"color:#f4f4f4;")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.label_3 = QLabel(self.path)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-weight: 1;\n"
"font-size:18px;\n"
"color:#f4f4f4;")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(499, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.path)


        self.verticalLayout.addWidget(self.top)

        self.body = QFrame(Form)
        self.body.setObjectName(u"body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(8)
        sizePolicy2.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy2)
        self.body.setStyleSheet(u"background-color:#f4f4f4;\n"
"border:none;")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.body)
#ifndef Q_OS_MAC
        self.verticalLayout_2.setSpacing(-1)
#endif
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: #cccccc;\n"
"padding:2px 0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgba(255,255,255,1);\n"
"margin:2px 2px;")

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(268, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.tableWidget = QTableWidget(self.body)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setStyleSheet(u"font-size:14px;")
        self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.verticalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.body)

        self.bottom = QFrame(Form)
        self.bottom.setObjectName(u"bottom")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.bottom.sizePolicy().hasHeightForWidth())
        self.bottom.setSizePolicy(sizePolicy3)
        self.bottom.setStyleSheet(u"border:none;")
        self.bottom.setFrameShape(QFrame.StyledPanel)
        self.bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.bottom)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(482, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.frame = QFrame(self.bottom)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.import_btn_2 = QPushButton(self.frame)
        self.import_btn_2.setObjectName(u"import_btn_2")
        self.import_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.import_btn_2.setStyleSheet(u"color:#f4f4f4;\n"
"background-color: #333b46;\n"
"padding:8px 8px;\n"
"marging:2px 2px;\n"
"border-radius:8px;")

        self.horizontalLayout_3.addWidget(self.import_btn_2)

        self.import_btn_3 = QPushButton(self.frame)
        self.import_btn_3.setObjectName(u"import_btn_3")
        self.import_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.import_btn_3.setStyleSheet(u"color:#f4f4f4;\n"
"background-color: #333b46;\n"
"padding:8px 8px;\n"
"marging:2px 2px;\n"
"border-radius:8px;")

        self.horizontalLayout_3.addWidget(self.import_btn_3)


        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout.addWidget(self.bottom)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Participant Name:", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText("")
        self.import_btn.setText(QCoreApplication.translate("Form", u"Import File", None))
        self.importMVC_btn.setText(QCoreApplication.translate("Form", u"Import MVC Files", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"EMG File:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"[File Path]", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Filter:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Channels", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"IsControlSignal", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Muscle Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"MVC Trail File", None));
        self.import_btn_2.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.import_btn_3.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

