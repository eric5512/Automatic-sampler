# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'connect.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(317, 234)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 170, 251, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 70, 63, 20))
        self.comboDevice = QComboBox(Dialog)
        self.comboDevice.setObjectName(u"comboDevice")
        self.comboDevice.setGeometry(QRect(100, 70, 82, 28))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 110, 63, 20))
        self.lineStatus = QLineEdit(Dialog)
        self.lineStatus.setObjectName(u"lineStatus")
        self.lineStatus.setGeometry(QRect(100, 110, 113, 28))
        self.lineStatus.setReadOnly(True)
        self.buttonConnect = QPushButton(Dialog)
        self.buttonConnect.setObjectName(u"buttonConnect")
        self.buttonConnect.setGeometry(QRect(190, 70, 75, 23))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Connect", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Device", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Status", None))
        self.buttonConnect.setText(QCoreApplication.translate("Dialog", u"Connect", None))
    # retranslateUi

