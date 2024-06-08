from PySide6.QtWidgets import QDialog

from ui_connect import Ui_Dialog

from MachineInterface import Machine

class ConnectMachineWindow(QDialog):
    def __init__(self):
        super(ConnectMachineWindow, self).__init__()
        self.ui = Ui_Dialog()
        
        self.ui.setupUi(self)
        
        self.devices = Machine.get_devices()
        
        self.ui.comboDevice.addItems(map(lambda x: x.name, self.devices))
        
        if Machine.is_connected():
            self.ui.lineStatus.setText(f"Connected to {Machine.get_port_name()}")
        
        self.ui.buttonConnect.clicked.connect(self._clicked_buttonConnect)
        
    def _clicked_buttonConnect(self):
        if not Machine.is_connected():
            Machine.connect(self.devices[self.ui.comboDevice.currentIndex()].name)
            if Machine.is_connected():
                self.ui.lineStatus.setText(f"Connected to {Machine.get_port_name()}")