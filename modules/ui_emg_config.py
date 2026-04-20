# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emg_config.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_EMGConfigWindow(object):
    def setupUi(self, EMGConfigWindow):
        if not EMGConfigWindow.objectName():
            EMGConfigWindow.setObjectName(u"EMGConfigWindow")
        EMGConfigWindow.resize(281, 425)
        self.verticalLayout = QVBoxLayout(EMGConfigWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dc_offset = QCheckBox(EMGConfigWindow)
        self.dc_offset.setObjectName(u"dc_offset")

        self.verticalLayout.addWidget(self.dc_offset)

        self.full_wave_rectification = QCheckBox(EMGConfigWindow)
        self.full_wave_rectification.setObjectName(u"full_wave_rectification")

        self.verticalLayout.addWidget(self.full_wave_rectification)

        self.normalization = QCheckBox(EMGConfigWindow)
        self.normalization.setObjectName(u"normalization")

        self.verticalLayout.addWidget(self.normalization)

        self.band_pass = QGroupBox(EMGConfigWindow)
        self.band_pass.setObjectName(u"band_pass")
        self.verticalLayout_2 = QVBoxLayout(self.band_pass)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.band_pass_switch = QCheckBox(self.band_pass)
        self.band_pass_switch.setObjectName(u"band_pass_switch")

        self.verticalLayout_2.addWidget(self.band_pass_switch)

        self.band_pass_order = QComboBox(self.band_pass)
        self.band_pass_order.addItem("")
        self.band_pass_order.addItem("")
        self.band_pass_order.addItem("")
        self.band_pass_order.setObjectName(u"band_pass_order")

        self.verticalLayout_2.addWidget(self.band_pass_order)

        self.groupBox_3 = QGroupBox(self.band_pass)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.band_pass_low = QDoubleSpinBox(self.groupBox_3)
        self.band_pass_low.setObjectName(u"band_pass_low")

        self.horizontalLayout.addWidget(self.band_pass_low)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.band_pass)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.band_pass_high = QDoubleSpinBox(self.groupBox_4)
        self.band_pass_high.setObjectName(u"band_pass_high")

        self.horizontalLayout_2.addWidget(self.band_pass_high)


        self.verticalLayout_2.addWidget(self.groupBox_4)


        self.verticalLayout.addWidget(self.band_pass)

        self.low_pass = QGroupBox(EMGConfigWindow)
        self.low_pass.setObjectName(u"low_pass")
        self.verticalLayout_3 = QVBoxLayout(self.low_pass)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.low_pass_switch = QCheckBox(self.low_pass)
        self.low_pass_switch.setObjectName(u"low_pass_switch")

        self.verticalLayout_3.addWidget(self.low_pass_switch)

        self.low_pass_order = QComboBox(self.low_pass)
        self.low_pass_order.addItem("")
        self.low_pass_order.addItem("")
        self.low_pass_order.addItem("")
        self.low_pass_order.setObjectName(u"low_pass_order")

        self.verticalLayout_3.addWidget(self.low_pass_order)

        self.groupBox_5 = QGroupBox(self.low_pass)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.low_pass_value = QDoubleSpinBox(self.groupBox_5)
        self.low_pass_value.setObjectName(u"low_pass_value")

        self.horizontalLayout_3.addWidget(self.low_pass_value)


        self.verticalLayout_3.addWidget(self.groupBox_5)


        self.verticalLayout.addWidget(self.low_pass)

        self.groupBox = QGroupBox(EMGConfigWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cancel = QPushButton(self.groupBox)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_5.addWidget(self.cancel)

        self.start = QPushButton(self.groupBox)
        self.start.setObjectName(u"start")

        self.horizontalLayout_5.addWidget(self.start)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(EMGConfigWindow)

        QMetaObject.connectSlotsByName(EMGConfigWindow)
    # setupUi

    def retranslateUi(self, EMGConfigWindow):
        EMGConfigWindow.setWindowTitle(QCoreApplication.translate("EMGConfigWindow", u"Form", None))
        self.dc_offset.setText(QCoreApplication.translate("EMGConfigWindow", u"DC_OFFSET", None))
        self.full_wave_rectification.setText(QCoreApplication.translate("EMGConfigWindow", u"Full Wave Rectification", None))
        self.normalization.setText(QCoreApplication.translate("EMGConfigWindow", u"Normalization", None))
        self.band_pass.setTitle(QCoreApplication.translate("EMGConfigWindow", u"Band Pass", None))
        self.band_pass_switch.setText(QCoreApplication.translate("EMGConfigWindow", u"Switch", None))
        self.band_pass_order.setItemText(0, QCoreApplication.translate("EMGConfigWindow", u"order 2", None))
        self.band_pass_order.setItemText(1, QCoreApplication.translate("EMGConfigWindow", u"order 3", None))
        self.band_pass_order.setItemText(2, QCoreApplication.translate("EMGConfigWindow", u"order 4", None))

        self.band_pass_order.setCurrentText(QCoreApplication.translate("EMGConfigWindow", u"order 2", None))
        self.groupBox_3.setTitle("")
        self.label.setText(QCoreApplication.translate("EMGConfigWindow", u"Low", None))
        self.groupBox_4.setTitle("")
        self.label_2.setText(QCoreApplication.translate("EMGConfigWindow", u"High", None))
        self.low_pass.setTitle(QCoreApplication.translate("EMGConfigWindow", u"Low Pass", None))
        self.low_pass_switch.setText(QCoreApplication.translate("EMGConfigWindow", u"Switch", None))
        self.low_pass_order.setItemText(0, QCoreApplication.translate("EMGConfigWindow", u"order 2", None))
        self.low_pass_order.setItemText(1, QCoreApplication.translate("EMGConfigWindow", u"order 3", None))
        self.low_pass_order.setItemText(2, QCoreApplication.translate("EMGConfigWindow", u"order 4", None))

        self.low_pass_order.setCurrentText(QCoreApplication.translate("EMGConfigWindow", u"order 2", None))
        self.groupBox_5.setTitle("")
        self.label_3.setText(QCoreApplication.translate("EMGConfigWindow", u"value", None))
        self.groupBox.setTitle("")
        self.cancel.setText(QCoreApplication.translate("EMGConfigWindow", u"Cancel", None))
        self.start.setText(QCoreApplication.translate("EMGConfigWindow", u"Start", None))
    # retranslateUi

