import serial
import serial.tools.list_ports as get_ports

class Serial:
    _conn = None
    
    def get_devices():
        return get_ports.comports()
    
    def is_connected() -> bool:
        return False if Serial._conn == None else Serial._conn.is_open
    
    def connect(port: str):
        Serial._conn = serial.Serial(port)
        Serial.send('INIT')
        while Serial._conn.in_waiting < 1:
            pass
        Serial.read()

    def send(data: str):
        Serial._conn.write(data.encode("utf-8"))
        
    def read() -> str:
        return Serial._conn.read().decode("utf-8")

    def get_port_name() -> str:
        return Serial._conn.port
    
    def disconnect():
        Serial._conn.close()