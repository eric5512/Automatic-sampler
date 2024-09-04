from PySide6.QtWidgets import QDialog

from ui_connect import Ui_Dialog

import serial.tools.list_ports as get_ports

from SensorProxy import SensorProxy

class ConnectSensorWindow(QDialog):
    def __init__(self):
        super(ConnectSensorWindow, self).__init__()
        self.ui = Ui_Dialog()
        
        self.ui.setupUi(self)
        
        self._devices = ConnectSensorWindow._get_devices()
        
        self.ui.comboDevice.addItems(map(lambda x: x.name, self._devices))
        
        sp = SensorProxy.get_instance()

        if sp.is_connected() == "True":
            self.ui.lineStatus.setText(f"Sensor already connected")

        self.ui.buttonConnect.clicked.connect(self._clicked_buttonConnect)

    def _get_devices():
        return get_ports.comports()

    def _clicked_buttonConnect(self):
        sp = SensorProxy.get_instance()

        if sp.is_connected() == "False":
            sp.connect(self.devices[self.ui.comboDevice.currentIndex()].name)
            if sp.is_connected() == "True":
                self.ui.lineStatus.setText(f"Sensor connected")