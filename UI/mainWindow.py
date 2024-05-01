import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

def create_error_box(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec_()

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

    window.show()

    sys.exit(app.exec())
