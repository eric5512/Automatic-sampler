import sys

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import Qt, Signal
import PySide6.QtCore

from ui_window import Ui_MainWindow

from MachineInterface import Machine
from SensorProxy import SensorProxy

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

BOX_SIZE = (100, 20, 20)

class MainWindow(QMainWindow):
    progressBar = Signal(int, name="progressBar")
    sensorProxy = SensorProxy.get_instance()
    OUTPUT_FILE = "output.data"

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

        self.ui.buttonReadSensor.clicked.connect(self.__manual_reading)
        
        self.progressBar.connect(self.__change_progressBar)
    
    def __check_connected_machine():
        if Machine.is_connected():
            return True
        create_error_box("Connection error", "Error: the machine is not connected")
        return False

    def __check_connected_sensor():
        if Machine.is_connected():
            return True
        create_error_box("Connection error", "Error: the sensor is not connected")
        return False

    @PySide6.QtCore.Slot(int)
    def __change_progressBar(self, value):
        self.ui.progressBar.setValue(value)
    
    def closeEvent(self, event: QCloseEvent) -> None:
        if Machine.is_connected():
            Machine.disconnect()

        self.sensorProxy.exit()
        
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
        if self.__check_connected_machine():
            self.ui.lineResponse.setText("Moving...")
            Machine.send_command_async(cmd, lambda s: self.ui.lineResponse.setText('OK' if s == '1' else 'NOK'))

    def __manual_reading(self):
        pass

    def __automatic_movement(self, points: list[tuple[int, int, int]], progress, outputFile: str):
        data = []
        count = 1
        total = len(points)
        for point in points:
            x, y, z = point
            
            res = Machine.send_wait(f"X{int(x)}")
            if res != "1":
                raise RuntimeError("Machine failed")
                        
            res = Machine.send_wait(f"Y{int(y)}")
            if res != "1":
                raise RuntimeError("Machine failed")            
            
            res = Machine.send_wait(f"Z{int(z)}")
            if res != "1":
                raise RuntimeError("Machine failed")
            
            data.append((x, y, z, self.sensorProxy.read_total_field()))
            
            progress.emit(count*100//total)
            count += 1
    
        print(",".join(str(t) for t in data), file=outputFile)

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
        if self.__check_connected_machine() and self.__check_connected_sensor():
            if self.ui.checkManualReading.isChecked():
                text = self.ui.textManualPositions.toPlainText()
                commands = [tuple(float(i) for i in m.split(",")) for m in re.findall(r"\(( *\d+ *, *\d+ *, *\d+ *)\)", text)]
            else:
                posx = [Machine.MAX_X/self.ui.spinXPoints.value()*i for i in range(self.ui.spinXPoints.value())] if self.ui.checkBoxX.isChecked() else [Machine.MAX_X/2]
                posy = [Machine.MAX_Y/self.ui.spinYPoints.value()*i for i in range(self.ui.spinYPoints.value())] if self.ui.checkBoxY.isChecked() else [Machine.MAX_Y/2]
                posz = [Machine.MAX_Z/self.ui.spinZPoints.value()*i for i in range(self.ui.spinZPoints.value())] if self.ui.checkBoxZ.isChecked() else [Machine.MAX_Z/2]
                
                commands = [(i,j,k) for i in posx for j in posy for k in posz]
            
            self.ui.progressBar.setValue(1)
            # t = threading.Thread(target=Machine.send_sequence, args=[commands, self.progressBar])
            t = threading.Thread(target=self.__automatic_movement, args=[commands, self.progressBar, self.OUTPUT_FILE])
            t.start()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())