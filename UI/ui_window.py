# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 657)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionConnectMachine = QAction(MainWindow)
        self.actionConnectMachine.setObjectName(u"actionConnectMachine")
        self.actionConnectSensor = QAction(MainWindow)
        self.actionConnectSensor.setObjectName(u"actionConnectSensor")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.config_tab = QWidget()
        self.config_tab.setObjectName(u"config_tab")
        self.gridLayout_3 = QGridLayout(self.config_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_11 = QLabel(self.config_tab)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_10.addWidget(self.label_11, 0, 0, 1, 1)

        self.checkManualReading = QCheckBox(self.config_tab)
        self.checkManualReading.setObjectName(u"checkManualReading")

        self.gridLayout_10.addWidget(self.checkManualReading, 0, 1, 1, 1)

        self.textManualPositions = QPlainTextEdit(self.config_tab)
        self.textManualPositions.setObjectName(u"textManualPositions")
        self.textManualPositions.setEnabled(False)
        self.textManualPositions.setReadOnly(False)

        self.gridLayout_10.addWidget(self.textManualPositions, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_10, 7, 0, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_8 = QLabel(self.config_tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_6.addWidget(self.label_8, 3, 0, 1, 1)

        self.spinXPoints = QSpinBox(self.config_tab)
        self.spinXPoints.setObjectName(u"spinXPoints")
        self.spinXPoints.setMinimum(1)
        self.spinXPoints.setMaximum(999)

        self.gridLayout_6.addWidget(self.spinXPoints, 1, 1, 1, 1)

        self.spinYPoints = QSpinBox(self.config_tab)
        self.spinYPoints.setObjectName(u"spinYPoints")
        self.spinYPoints.setMinimum(1)
        self.spinYPoints.setMaximum(999)

        self.gridLayout_6.addWidget(self.spinYPoints, 2, 1, 1, 1)

        self.spinTotalPoints = QSpinBox(self.config_tab)
        self.spinTotalPoints.setObjectName(u"spinTotalPoints")
        self.spinTotalPoints.setReadOnly(True)
        self.spinTotalPoints.setMaximum(999999)
        self.spinTotalPoints.setValue(1)

        self.gridLayout_6.addWidget(self.spinTotalPoints, 4, 1, 1, 1)

        self.label_9 = QLabel(self.config_tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_6.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_5 = QLabel(self.config_tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.config_tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_7 = QLabel(self.config_tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_6.addWidget(self.label_7, 2, 0, 1, 1)

        self.spinZPoints = QSpinBox(self.config_tab)
        self.spinZPoints.setObjectName(u"spinZPoints")
        self.spinZPoints.setMinimum(1)
        self.spinZPoints.setMaximum(999)

        self.gridLayout_6.addWidget(self.spinZPoints, 3, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 11, 0, 1, 1)

        self.buttonBeginMovement = QPushButton(self.config_tab)
        self.buttonBeginMovement.setObjectName(u"buttonBeginMovement")

        self.gridLayout_3.addWidget(self.buttonBeginMovement, 13, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkBoxY = QCheckBox(self.config_tab)
        self.checkBoxY.setObjectName(u"checkBoxY")
        self.checkBoxY.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBoxY, 3, 1, 1, 1)

        self.label_10 = QLabel(self.config_tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)

        self.checkBoxX = QCheckBox(self.config_tab)
        self.checkBoxX.setObjectName(u"checkBoxX")
        self.checkBoxX.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBoxX, 1, 1, 1, 1)

        self.checkBoxZ = QCheckBox(self.config_tab)
        self.checkBoxZ.setObjectName(u"checkBoxZ")
        self.checkBoxZ.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBoxZ, 4, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 9, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 10, 0, 1, 1)

        self.progressBar = QProgressBar(self.config_tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_3.addWidget(self.progressBar, 14, 0, 1, 1)

        self.tabWidget.addTab(self.config_tab, "")
        self.manual_tab = QWidget()
        self.manual_tab.setObjectName(u"manual_tab")
        self.gridLayout_8 = QGridLayout(self.manual_tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_17 = QLabel(self.manual_tab)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_12 = QLabel(self.manual_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_12, 1, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButtonRelativeX = QPushButton(self.manual_tab)
        self.pushButtonRelativeX.setObjectName(u"pushButtonRelativeX")

        self.gridLayout_4.addWidget(self.pushButtonRelativeX, 0, 2, 1, 1)

        self.label_2 = QLabel(self.manual_tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.manual_tab)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)

        self.spinRelativeX = QSpinBox(self.manual_tab)
        self.spinRelativeX.setObjectName(u"spinRelativeX")
        self.spinRelativeX.setMinimum(-1000)
        self.spinRelativeX.setMaximum(1000)

        self.gridLayout_4.addWidget(self.spinRelativeX, 0, 1, 1, 1)

        self.spinRelativeY = QSpinBox(self.manual_tab)
        self.spinRelativeY.setObjectName(u"spinRelativeY")
        self.spinRelativeY.setMinimum(-1000)
        self.spinRelativeY.setMaximum(1000)

        self.gridLayout_4.addWidget(self.spinRelativeY, 1, 1, 1, 1)

        self.spinRelativeZ = QSpinBox(self.manual_tab)
        self.spinRelativeZ.setObjectName(u"spinRelativeZ")
        self.spinRelativeZ.setMinimum(-1000)
        self.spinRelativeZ.setMaximum(1000)

        self.gridLayout_4.addWidget(self.spinRelativeZ, 2, 1, 1, 1)

        self.label_4 = QLabel(self.manual_tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.pushButtonRelativeY = QPushButton(self.manual_tab)
        self.pushButtonRelativeY.setObjectName(u"pushButtonRelativeY")

        self.gridLayout_4.addWidget(self.pushButtonRelativeY, 1, 2, 1, 1)

        self.pushButtonRelativeZ = QPushButton(self.manual_tab)
        self.pushButtonRelativeZ.setObjectName(u"pushButtonRelativeZ")

        self.gridLayout_4.addWidget(self.pushButtonRelativeZ, 2, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        self.label_13 = QLabel(self.manual_tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_13, 3, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_14 = QLabel(self.manual_tab)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 0, 0, 1, 1)

        self.spinBoxAbsoluteY = QSpinBox(self.manual_tab)
        self.spinBoxAbsoluteY.setObjectName(u"spinBoxAbsoluteY")
        self.spinBoxAbsoluteY.setMaximum(1000)

        self.gridLayout_7.addWidget(self.spinBoxAbsoluteY, 1, 1, 1, 1)

        self.label_15 = QLabel(self.manual_tab)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 1, 0, 1, 1)

        self.spinBoxAbsoluteZ = QSpinBox(self.manual_tab)
        self.spinBoxAbsoluteZ.setObjectName(u"spinBoxAbsoluteZ")
        self.spinBoxAbsoluteZ.setMaximum(1000)

        self.gridLayout_7.addWidget(self.spinBoxAbsoluteZ, 2, 1, 1, 1)

        self.spinBoxAbsoluteX = QSpinBox(self.manual_tab)
        self.spinBoxAbsoluteX.setObjectName(u"spinBoxAbsoluteX")
        self.spinBoxAbsoluteX.setMaximum(1000)

        self.gridLayout_7.addWidget(self.spinBoxAbsoluteX, 0, 1, 1, 1)

        self.label_16 = QLabel(self.manual_tab)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_7.addWidget(self.label_16, 2, 0, 1, 1)

        self.pushButtonAbsoluteX = QPushButton(self.manual_tab)
        self.pushButtonAbsoluteX.setObjectName(u"pushButtonAbsoluteX")

        self.gridLayout_7.addWidget(self.pushButtonAbsoluteX, 0, 2, 1, 1)

        self.pushButtonAbsoluteY = QPushButton(self.manual_tab)
        self.pushButtonAbsoluteY.setObjectName(u"pushButtonAbsoluteY")

        self.gridLayout_7.addWidget(self.pushButtonAbsoluteY, 1, 2, 1, 1)

        self.pushButtonAbsoluteZ = QPushButton(self.manual_tab)
        self.pushButtonAbsoluteZ.setObjectName(u"pushButtonAbsoluteZ")

        self.gridLayout_7.addWidget(self.pushButtonAbsoluteZ, 2, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 4, 0, 1, 1)

        self.buttonOrigin = QPushButton(self.manual_tab)
        self.buttonOrigin.setObjectName(u"buttonOrigin")

        self.gridLayout_8.addWidget(self.buttonOrigin, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.manual_tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineResponse = QLineEdit(self.manual_tab)
        self.lineResponse.setObjectName(u"lineResponse")
        self.lineResponse.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineResponse)


        self.gridLayout_8.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.label_18 = QLabel(self.manual_tab)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_18, 8, 0, 1, 1)

        self.buttonReadSensor = QPushButton(self.manual_tab)
        self.buttonReadSensor.setObjectName(u"buttonReadSensor")

        self.gridLayout_8.addWidget(self.buttonReadSensor, 9, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_21 = QLabel(self.manual_tab)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_4.addWidget(self.label_21)

        self.lineSensorTotal = QLineEdit(self.manual_tab)
        self.lineSensorTotal.setObjectName(u"lineSensorTotal")
        self.lineSensorTotal.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineSensorTotal)


        self.gridLayout_8.addLayout(self.horizontalLayout_4, 10, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_22 = QLabel(self.manual_tab)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_5.addWidget(self.label_22)

        self.lineSensorX = QLineEdit(self.manual_tab)
        self.lineSensorX.setObjectName(u"lineSensorX")
        self.lineSensorX.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineSensorX)


        self.gridLayout_8.addLayout(self.horizontalLayout_5, 11, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_23 = QLabel(self.manual_tab)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_6.addWidget(self.label_23)

        self.lineSensorY = QLineEdit(self.manual_tab)
        self.lineSensorY.setObjectName(u"lineSensorY")
        self.lineSensorY.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineSensorY)


        self.gridLayout_8.addLayout(self.horizontalLayout_6, 12, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_24 = QLabel(self.manual_tab)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_7.addWidget(self.label_24)

        self.lineSensorZ = QLineEdit(self.manual_tab)
        self.lineSensorZ.setObjectName(u"lineSensorZ")
        self.lineSensorZ.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineSensorZ)


        self.gridLayout_8.addLayout(self.horizontalLayout_7, 13, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.tabWidget.addTab(self.manual_tab, "")
        self.view_tab = QWidget()
        self.view_tab.setObjectName(u"view_tab")
        self.gridLayout_2 = QGridLayout(self.view_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.graphSelectFile = QPushButton(self.view_tab)
        self.graphSelectFile.setObjectName(u"graphSelectFile")

        self.gridLayout_2.addWidget(self.graphSelectFile, 0, 1, 1, 1)

        self.graph = QGridLayout()
        self.graph.setObjectName(u"graph")

        self.gridLayout_2.addLayout(self.graph, 1, 0, 1, 3)

        self.tabWidget.addTab(self.view_tab, "")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.tabWidget)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 865, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionConnectSensor)
        self.menuFile.addAction(self.actionConnectMachine)
        self.menuHelp.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionConnectMachine.setText(QCoreApplication.translate("MainWindow", u"Connect machine", None))
        self.actionConnectSensor.setText(QCoreApplication.translate("MainWindow", u"Connect sensor", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Manual reading (Input coordinates separated by commas in tuples, ex. \"(20,30,40),(10,100,20)\")", None))
        self.checkManualReading.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Z points", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Total points", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Number of points", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"X points", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y points", None))
        self.buttonBeginMovement.setText(QCoreApplication.translate("MainWindow", u"Start measurement", None))
        self.checkBoxY.setText(QCoreApplication.translate("MainWindow", u"Y axis", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Planes", None))
        self.checkBoxX.setText(QCoreApplication.translate("MainWindow", u"X axis", None))
        self.checkBoxZ.setText(QCoreApplication.translate("MainWindow", u"Z axis", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config_tab), QCoreApplication.translate("MainWindow", u"Automatic", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Relative", None))
        self.pushButtonRelativeX.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButtonRelativeY.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.pushButtonRelativeZ.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Absolute", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.pushButtonAbsoluteX.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.pushButtonAbsoluteY.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.pushButtonAbsoluteZ.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.buttonOrigin.setText(QCoreApplication.translate("MainWindow", u"Origin", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Response: ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Sensor", None))
        self.buttonReadSensor.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Total value: ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"X value: ", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Y value:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Z value:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manual_tab), QCoreApplication.translate("MainWindow", u"Manual", None))
        self.graphSelectFile.setText(QCoreApplication.translate("MainWindow", u"Select file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view_tab), QCoreApplication.translate("MainWindow", u"View", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

