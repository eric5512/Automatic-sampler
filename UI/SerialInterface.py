import serial
import serial.tools.list_ports as get_ports

class Serial:
    def get_status():
        raise NotImplementedError()
    
    def get_devices():
        return get_ports.comports()