from PySide6.QtWidgets import QDialog

from ui_connect import Ui_Dialog

import serial.tools.list_ports as get_ports

from SensorInterface import EFSensor

class ConnectSensorWindow(QDialog):
    _DLLPATH = ""

    def __init__(self):
        super(ConnectSensorWindow, self).__init__()
        self.ui = Ui_Dialog()
        
        self.ui.setupUi(self)
        
        self._devices = ConnectSensorWindow._get_devices()
        
        self.ui.comboDevice.addItems(map(lambda x: x.name, self._devices))
        
        if EFSensor.is_connected():
            self.ui.lineStatus.setText(f"Sensor already connected")
        
        self._device = EFSensor(ConnectSensorWindow._DLLPATH)

        self.ui.buttonConnect.clicked.connect(self._clicked_buttonConnect)

    def _get_devices():
        return get_ports.comports()

    def _clicked_buttonConnect(self):
        if not EFSensor.is_connected():
            self._device.connect(self.devices[self.ui.comboDevice.currentIndex()].name)
            if EFSensor.is_connected():
                self.ui.lineStatus.setText(f"Sensor connected")

    def _get_sensor(self):
        return self._device