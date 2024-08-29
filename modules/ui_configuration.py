# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuration.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_Configuration(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(646, 487)
        Form.setStyleSheet("background-color:#2c3039;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.body = QFrame(Form)
        self.body.setObjectName("body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setStyleSheet("border:none;")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        # ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
        # endif
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.body)
        self.left_menu.setObjectName("left_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy1)
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.general = QFrame(self.left_menu)
        self.general.setObjectName("general")
        self.general.setMinimumSize(QSize(0, 45))
        self.general.setMaximumSize(QSize(16777215, 45))
        self.general.setCursor(QCursor(Qt.PointingHandCursor))
        self.general.setStyleSheet("")
        self.general.setFrameShape(QFrame.StyledPanel)
        self.general.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.general)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.general)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(
            "color:rgba(255,255,255,0.8);\n"
            "border-bottom:0.5px solid rgba(255,255,255,0.1);\n"
            "padding:10px;"
        )

        self.verticalLayout_3.addWidget(self.pushButton)

        self.verticalLayout_2.addWidget(self.general)

        self.general_2 = QFrame(self.left_menu)
        self.general_2.setObjectName("general_2")
        self.general_2.setMinimumSize(QSize(0, 45))
        self.general_2.setMaximumSize(QSize(16777215, 45))
        self.general_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.general_2.setStyleSheet("")
        self.general_2.setFrameShape(QFrame.StyledPanel)
        self.general_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.general_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.general_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(
            "color:rgba(255,255,255,0.8);\n"
            "border-bottom:0.5px solid rgba(255,255,255,0.1);\n"
            "padding:10px;"
        )

        self.verticalLayout_4.addWidget(self.pushButton_2)

        self.verticalLayout_2.addWidget(self.general_2)

        self.general_3 = QFrame(self.left_menu)
        self.general_3.setObjectName("general_3")
        self.general_3.setMinimumSize(QSize(0, 45))
        self.general_3.setMaximumSize(QSize(16777215, 45))
        self.general_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.general_3.setFrameShape(QFrame.StyledPanel)
        self.general_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.general_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.general_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(
            "color:rgba(255,255,255,0.8);\n"
            "border-bottom:0.5px solid rgba(255,255,255,0.1);\n"
            "padding:10px;"
        )

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.verticalLayout_2.addWidget(self.general_3)

        self.general_4 = QFrame(self.left_menu)
        self.general_4.setObjectName("general_4")
        self.general_4.setMinimumSize(QSize(0, 45))
        self.general_4.setMaximumSize(QSize(16777215, 45))
        self.general_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.general_4.setFrameShape(QFrame.StyledPanel)
        self.general_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.general_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.general_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(
            "color:rgba(255,255,255,0.8);\n"
            "border-bottom:0.5px solid rgba(255,255,255,0.1);\n"
            "padding:10px;"
        )

        self.verticalLayout_6.addWidget(self.pushButton_4)

        self.verticalLayout_2.addWidget(self.general_4)

        self.general_5 = QFrame(self.left_menu)
        self.general_5.setObjectName("general_5")
        self.general_5.setMinimumSize(QSize(0, 45))
        self.general_5.setMaximumSize(QSize(16777215, 45))
        self.general_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.general_5.setFrameShape(QFrame.StyledPanel)
        self.general_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.general_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.general_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(
            "color:rgba(255,255,255,0.8);\n"
            "border-bottom:0.5px solid rgba(255,255,255,0.1);\n"
            "padding:10px;"
        )

        self.verticalLayout_7.addWidget(self.pushButton_5)

        self.verticalLayout_2.addWidget(self.general_5)

        self.general_6 = QFrame(self.left_menu)
        self.general_6.setObjectName("general_6")
        self.general_6.setMinimumSize(QSize(0, 45))
        self.general_6.setMaximumSize(QSize(16777215, 45))
        self.general_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.general_6.setFrameShape(QFrame.StyledPanel)
        self.general_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.general_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.general_6)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet(
            "color:rgba(255,255,255,0.8);\n" "\n" "padding:10px;"
        )

        self.verticalLayout_8.addWidget(self.pushButton_6)

        self.verticalLayout_2.addWidget(self.general_6)

        self.verticalSpacer = QSpacerItem(
            20, 190, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout.addWidget(self.left_menu)

        self.right_content = QStackedWidget(self.body)
        self.right_content.setObjectName("right_content")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(8)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.right_content.sizePolicy().hasHeightForWidth()
        )
        self.right_content.setSizePolicy(sizePolicy2)
        self.right_content.setStyleSheet("background-color:rgba(45,56,56,0.1);")
        self.preference = QWidget()
        self.preference.setObjectName("preference")
        self.verticalLayout_9 = QVBoxLayout(self.preference)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.body_2 = QFrame(self.preference)
        self.body_2.setObjectName("body_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(9)
        sizePolicy3.setHeightForWidth(self.body_2.sizePolicy().hasHeightForWidth())
        self.body_2.setSizePolicy(sizePolicy3)
        self.body_2.setStyleSheet("background-color:rgba(255,255,255,1);")
        self.body_2.setFrameShape(QFrame.StyledPanel)
        self.body_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.body_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_check = QFrame(self.body_2)
        self.left_check.setObjectName("left_check")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.left_check.sizePolicy().hasHeightForWidth())
        self.left_check.setSizePolicy(sizePolicy4)
        self.left_check.setFrameShape(QFrame.StyledPanel)
        self.left_check.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.left_check)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame = QFrame(self.left_check)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(
            24, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.checkbox_list = QFrame(self.frame)
        self.checkbox_list.setObjectName("checkbox_list")
        self.checkbox_list.setStyleSheet("padding:10px;")
        self.checkbox_list.setFrameShape(QFrame.StyledPanel)
        self.checkbox_list.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.checkbox_list)
        # ifndef Q_OS_MAC
        self.verticalLayout_10.setSpacing(-1)
        # endif
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 12, -1, -1)
        self.checkBox = QCheckBox(self.checkbox_list)
        self.checkBox.setObjectName("checkBox")

        self.verticalLayout_10.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.checkbox_list)
        self.checkBox_2.setObjectName("checkBox_2")

        self.verticalLayout_10.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.checkbox_list)
        self.checkBox_3.setObjectName("checkBox_3")

        self.verticalLayout_10.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.checkbox_list)
        self.checkBox_4.setObjectName("checkBox_4")

        self.verticalLayout_10.addWidget(self.checkBox_4)

        self.horizontalLayout_4.addWidget(self.checkbox_list)

        self.horizontalSpacer_3 = QSpacerItem(
            1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_11.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(
            20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_11.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3.addWidget(self.left_check)

        self.right_check = QFrame(self.body_2)
        self.right_check.setObjectName("right_check")
        sizePolicy4.setHeightForWidth(self.right_check.sizePolicy().hasHeightForWidth())
        self.right_check.setSizePolicy(sizePolicy4)
        self.right_check.setFrameShape(QFrame.StyledPanel)
        self.right_check.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.right_check)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_2 = QFrame(self.right_check)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalSpacer_6 = QSpacerItem(
            119, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.checkbox_list_3 = QFrame(self.frame_2)
        self.checkbox_list_3.setObjectName("checkbox_list_3")
        self.checkbox_list_3.setStyleSheet("padding:10px;")
        self.checkbox_list_3.setFrameShape(QFrame.StyledPanel)
        self.checkbox_list_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.checkbox_list_3)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 12, -1, -1)
        self.checkBox_9 = QCheckBox(self.checkbox_list_3)
        self.checkBox_9.setObjectName("checkBox_9")

        self.verticalLayout_13.addWidget(self.checkBox_9)

        self.checkBox_10 = QCheckBox(self.checkbox_list_3)
        self.checkBox_10.setObjectName("checkBox_10")

        self.verticalLayout_13.addWidget(self.checkBox_10)

        self.checkBox_11 = QCheckBox(self.checkbox_list_3)
        self.checkBox_11.setObjectName("checkBox_11")

        self.verticalLayout_13.addWidget(self.checkBox_11)

        self.checkBox_12 = QCheckBox(self.checkbox_list_3)
        self.checkBox_12.setObjectName("checkBox_12")

        self.verticalLayout_13.addWidget(self.checkBox_12)

        self.horizontalLayout_6.addWidget(self.checkbox_list_3)

        self.horizontalSpacer_7 = QSpacerItem(
            119, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.verticalLayout_14.addWidget(self.frame_2)

        self.verticalSpacer_3 = QSpacerItem(
            20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3.addWidget(self.right_check)

        self.verticalLayout_9.addWidget(self.body_2)

        self.button_group = QFrame(self.preference)
        self.button_group.setObjectName("button_group")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(
            self.button_group.sizePolicy().hasHeightForWidth()
        )
        self.button_group.setSizePolicy(sizePolicy5)
        self.button_group.setFrameShape(QFrame.StyledPanel)
        self.button_group.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.button_group)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(
            340, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.import_btn_2 = QPushButton(self.button_group)
        self.import_btn_2.setObjectName("import_btn_2")
        self.import_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.import_btn_2.setStyleSheet(
            "color:#f4f4f4;\n"
            "background-color: #333b46;\n"
            "padding:8px 8px;\n"
            "marging:2px 2px;\n"
            "border-radius:8px;"
        )

        self.horizontalLayout_2.addWidget(self.import_btn_2)

        self.import_btn_3 = QPushButton(self.button_group)
        self.import_btn_3.setObjectName("import_btn_3")
        self.import_btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.import_btn_3.setStyleSheet(
            "color:#f4f4f4;\n"
            "background-color: #333b46;\n"
            "padding:8px 8px;\n"
            "marging:2px 2px;\n"
            "border-radius:8px;"
        )

        self.horizontalLayout_2.addWidget(self.import_btn_3)

        self.verticalLayout_9.addWidget(self.button_group)

        self.right_content.addWidget(self.preference)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.right_content.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.right_content)

        self.verticalLayout.addWidget(self.body)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", "Preferences", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", "EMG", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("Form", "Kinematics", None)
        )
        self.pushButton_4.setText(QCoreApplication.translate("Form", "Frequency", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", "Advanced", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", "Stats", None))
        self.checkBox.setText(QCoreApplication.translate("Form", "CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", "CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", "CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", "CheckBox", None))
        self.checkBox_9.setText(QCoreApplication.translate("Form", "CheckBox", None))
        self.checkBox_10.setText(QCoreApplication.translate("Form", "CheckBox", None))
        self.checkBox_11.setText(QCoreApplication.translate("Form", "CheckBox", None))
        self.checkBox_12.setText(QCoreApplication.translate("Form", "CheckBox", None))
        self.import_btn_2.setText(QCoreApplication.translate("Form", "Confirm", None))
        self.import_btn_3.setText(QCoreApplication.translate("Form", "Cancel", None))

    # retranslateUi
