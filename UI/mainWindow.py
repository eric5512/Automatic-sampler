import sys

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

from ui_window import Ui_MainWindow

from MachineInterface import Machine
from SensorInterface import EFSensor

from Scatter3D import ScatterGraph

from connectMachineWindow import ConnectMachineWindow
from connectSensorWindow import ConnectSensorWindow

import threading

import re

def create_error_box(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec_()

def check_connected():
    if  Machine.is_connected():
        return True
    create_error_box("Connection error", "Error: the device is not connected")
    return False

BOX_SIZE = (100, 20, 20)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Automatic sampler")
        
        self.scatter = ScatterGraph()
        self.ui.graph.addWidget(self.scatter)

        self.ui.checkManualReading.toggled.connect(self.__toggle_checkManualReading)

        self.ui.checkBoxX.toggled.connect(self.__toggle_checkBoxX)
        self.ui.checkBoxY.toggled.connect(self.__toggle_checkBoxY)
        self.ui.checkBoxZ.toggled.connect(self.__toggle_checkBoxZ)

        self.ui.spinXPoints.valueChanged.connect(self.__calculate_total_points)
        self.ui.spinYPoints.valueChanged.connect(self.__calculate_total_points)
        self.ui.spinZPoints.valueChanged.connect(self.__calculate_total_points)

        self.ui.actionConnectMachine.triggered.connect(self.__click_actionConnectMachine)
        self.ui.actionConnectSensor.triggered.connect(self.__click_actionConnectSensor)
        
        self.ui.buttonOrigin.clicked.connect(self.__click_buttonOrigin)
        
        self.ui.pushButtonRelativeX.clicked.connect(self.__click_buttonMoveXRel)
        self.ui.pushButtonRelativeY.clicked.connect(self.__click_buttonMoveYRel)
        self.ui.pushButtonRelativeZ.clicked.connect(self.__click_buttonMoveZRel)
        self.ui.pushButtonAbsoluteX.clicked.connect(self.__click_buttonMoveXAbs)
        self.ui.pushButtonAbsoluteY.clicked.connect(self.__click_buttonMoveYAbs)
        self.ui.pushButtonAbsoluteZ.clicked.connect(self.__click_buttonMoveZAbs)

        self.ui.buttonBeginMovement.clicked.connect(self.__click_buttonStartMeasurement)
        
        self.ui.graphSelectFile.clicked.connect(self.__click_graphSelectFile)
        

    
    def closeEvent(self, event: QCloseEvent) -> None:
        if Machine.is_connected():
            Machine.disconnect()
        
        return super().closeEvent(event)
    
    def __click_graphSelectFile(self):
        fw = QFileDialog()
        path, _ = fw.getOpenFileName()

        if path == "":
            return
        
        with open(path, "rt") as file:
            text = file.read()
            values = [tuple(float(i) for i in m.split(",")) for m in re.findall(r"\(( *\d+ *, *\d+ *, *\d+, *\d+ *)\)", text)]

            self.scatter.plot(values, BOX_SIZE)

    def __toggle_checkManualReading(self, state):
        nstate = not state
        self.ui.spinTotalPoints.setEnabled(nstate)
        self.ui.spinXPoints.setEnabled(nstate)
        self.ui.spinYPoints.setEnabled(nstate)
        self.ui.spinZPoints.setEnabled(nstate)
        self.ui.checkBoxX.setEnabled(nstate)
        self.ui.checkBoxY.setEnabled(nstate)
        self.ui.checkBoxZ.setEnabled(nstate)
        self.ui.textManualPositions.setEnabled(state)

    def __calculate_total_points(self):
        x = self.ui.spinXPoints.value() if self.ui.checkBoxX.isChecked() else 1
        y = self.ui.spinYPoints.value() if self.ui.checkBoxY.isChecked() else 1
        z = self.ui.spinZPoints.value() if self.ui.checkBoxZ.isChecked() else 1

        self.ui.spinTotalPoints.setValue(x*y*z)

    def __toggle_checkBoxX(self, state):
        self.ui.spinXPoints.setEnabled(state)
        self.__calculate_total_points()

    def __toggle_checkBoxY(self, state):
        self.ui.spinYPoints.setEnabled(state)
        self.__calculate_total_points()

    def __toggle_checkBoxZ(self, state):
        self.ui.spinZPoints.setEnabled(state)
        self.__calculate_total_points()

    def __click_actionConnectMachine(self):
        con = ConnectMachineWindow()
        con.exec()

    def __click_actionConnectSensor(self):
        con = ConnectSensorWindow()
        con.exec()

    def __manual_movement(self, cmd):
        if check_connected():
            self.ui.lineResponse.setText("Moving...")
            Machine.send_command_async(cmd, lambda s: self.ui.lineResponse.setText('OK' if s == '1' else 'NOK'))

    def __click_buttonMoveXRel(self):
        num = self.ui.spinRelativeX.value()
        self.__manual_movement(f"X{'+' if num > 0 else '-'}{num if num > 0 else -num}")

    def __click_buttonMoveYRel(self):
        num = self.ui.spinRelativeY.value()
        self.__manual_movement(f"Y{'+' if num > 0 else '-'}{num if num > 0 else -num}")
        
    def __click_buttonMoveZRel(self):
        num = self.ui.spinRelativeZ.value()
        self.__manual_movement(f"Z{'+' if num > 0 else '-'}{num if num > 0 else -num}")
        
    def __click_buttonMoveXAbs(self):
        self.__manual_movement(f"X{self.ui.spinBoxAbsoluteX.value()}")
        
    def __click_buttonMoveYAbs(self):
        self.__manual_movement(f"Y{self.ui.spinBoxAbsoluteY.value()}")
        
    def __click_buttonMoveZAbs(self):
        self.__manual_movement(f"Z{self.ui.spinBoxAbsoluteZ.value()}")
        
    def __click_buttonOrigin(self):
        self.__manual_movement("CAL")
        
    def __click_buttonStartMeasurement(self):
        commands = [(10, 10, 10), (15, 15, 15)]
        if Machine.is_connected():
            self.ui.progressBar.setValue(1)
            t = threading.Thread(target=Machine.send_sequence, args=[commands, self.ui.progressBar])
            t.start()
            
        # TODO: write data to file
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    # EFSensor.init()

    window.show()

    sys.exit(app.exec())