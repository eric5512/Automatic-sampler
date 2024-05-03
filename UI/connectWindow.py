from PySide6.QtWidgets import QDialog

from ui_connect import Ui_Dialog

from SerialInterface import Serial

class ConnectWindow(QDialog):
    def __init__(self):
        super(ConnectWindow, self).__init__()
        self.ui = Ui_Dialog()
        
        self.ui.setupUi(self)
        
        self.devices = Serial.get_devices()
        
        self.ui.comboDevice.addItems(map(lambda x: x.name, self.devices))
        
        if Serial.is_connected():
            self.ui.lineStatus.setText(f"Connected to {Serial.get_port_name()}")
        
        self.ui.buttonConnect.clicked.connect(self._clicked_buttonConnect)
        
    def _clicked_buttonConnect(self):
        if not Serial.is_connected():
            Serial.connect(self.devices[self.ui.comboDevice.currentIndex()].name)
            if Serial.is_connected():
                self.ui.lineStatus.setText(f"Connected to {Serial.get_port_name()}")