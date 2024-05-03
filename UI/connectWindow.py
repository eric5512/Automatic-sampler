from PySide6.QtWidgets import QDialog

from ui_connect import Ui_Dialog

class ConnectWindow(QDialog):
    def __init__(self):
        super(ConnectWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)