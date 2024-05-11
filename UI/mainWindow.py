import sys

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_window import Ui_MainWindow

from SerialInterface import Serial
from connectWindow import ConnectWindow

def create_error_box(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec_()

def check_connected():
    if  Serial.is_connected():
        return True
    create_error_box("Connection error", "Error: the device is not connected")
    return False

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def closeEvent(self, event: QCloseEvent) -> None:
        if Serial.is_connected():
            Serial.disconnect()
        
        return super().closeEvent(event)

def toggle_checkManualReading(state):
    nstate = not state
    ui.spinTotalPoints.setEnabled(nstate)
    ui.spinXPoints.setEnabled(nstate)
    ui.spinYPoints.setEnabled(nstate)
    ui.spinZPoints.setEnabled(nstate)
    ui.checkBoxX.setEnabled(nstate)
    ui.checkBoxY.setEnabled(nstate)
    ui.checkBoxZ.setEnabled(nstate)
    ui.textManualPositions.setEnabled(state)

def calculate_total_points():
    x = ui.spinXPoints.value() if ui.checkBoxX.isChecked() else 1
    y = ui.spinYPoints.value() if ui.checkBoxY.isChecked() else 1
    z = ui.spinZPoints.value() if ui.checkBoxZ.isChecked() else 1

    ui.spinTotalPoints.setValue(x*y*z)

def toggle_checkBoxX(state):
    ui.spinXPoints.setEnabled(state)
    calculate_total_points()

def toggle_checkBoxY(state):
    ui.spinYPoints.setEnabled(state)
    calculate_total_points()

def toggle_checkBoxZ(state):
    ui.spinZPoints.setEnabled(state)
    calculate_total_points()

def click_actionConnect():
    con = ConnectWindow()
    con.exec()

def manual_movement(cmd):
    if check_connected():
        ui.lineResponse.setText("Moving...")
        Serial.send_command(cmd, lambda s: ui.lineResponse.setText('OK' if s == '1' else 'NOK'))

def click_buttonMoveXRel():
    num = ui.spinRelativeX.value()
    manual_movement(f"X{'+' if num > 0 else '-'}{num if num > 0 else -num}")

def click_buttonMoveYRel():
    num = ui.spinRelativeY.value()
    manual_movement(f"Y{'+' if num > 0 else '-'}{num if num > 0 else -num}")
    
def click_buttonMoveZRel():
    num = ui.spinRelativeZ.value()
    manual_movement(f"Z{'+' if num > 0 else '-'}{num if num > 0 else -num}")
    
def click_buttonMoveXAbs():
    manual_movement(f"X{ui.spinBoxAbsoluteX.value()}")
    
def click_buttonMoveYAbs():
    manual_movement(f"Y{ui.spinBoxAbsoluteY.value()}")
    
def click_buttonMoveZAbs():
    manual_movement(f"Z{ui.spinBoxAbsoluteZ.value()}")
    
def click_buttonOrigin():
    manual_movement("CAL")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()

    ui = window.ui

    ui.checkManualReading.toggled.connect(toggle_checkManualReading)

    ui.checkBoxX.toggled.connect(toggle_checkBoxX)
    ui.checkBoxY.toggled.connect(toggle_checkBoxY)
    ui.checkBoxZ.toggled.connect(toggle_checkBoxZ)

    ui.spinXPoints.valueChanged.connect(calculate_total_points)
    ui.spinYPoints.valueChanged.connect(calculate_total_points)
    ui.spinZPoints.valueChanged.connect(calculate_total_points)

    ui.actionConnect.triggered.connect(click_actionConnect)
    
    ui.buttonOrigin.clicked.connect(click_buttonOrigin)
    
    ui.pushButtonRelativeX.clicked.connect(click_buttonMoveXRel)
    ui.pushButtonRelativeY.clicked.connect(click_buttonMoveYRel)
    ui.pushButtonRelativeZ.clicked.connect(click_buttonMoveZRel)
    ui.pushButtonAbsoluteX.clicked.connect(click_buttonMoveXAbs)
    ui.pushButtonAbsoluteY.clicked.connect(click_buttonMoveYAbs)
    ui.pushButtonAbsoluteZ.clicked.connect(click_buttonMoveZAbs)

    window.show()

    sys.exit(app.exec())