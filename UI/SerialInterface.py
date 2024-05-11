import serial
import serial.tools.list_ports as get_ports

import threading
import time

from typing import Callable

class Serial:
    _conn = None
    _sent = False
    
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

    def send_command(cmd: str, on_response: Callable[[str], None]):
        if not Serial._sent:
            def aresponse():
                while Serial._conn.in_waiting < 1:
                    time.sleep(0.1)
                
                on_response(Serial.read())
                
                Serial._sent = False
            
            t = threading.Thread(target=aresponse, args=[])
            Serial._sent = True
            Serial.send(cmd)
            t.start()
        
    def get_port_name() -> str:
        return Serial._conn.port
    
    def disconnect():
        Serial._conn.close()