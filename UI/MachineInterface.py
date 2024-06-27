import serial
import serial.tools.list_ports as get_ports

import threading
import time

from typing import Callable

class Machine:
    _conn = None
    _sent = False
    
    MAX_X = 400
    MAX_Y = 163
    MAX_Z = 163
    
    def get_devices():
        return get_ports.comports()
    
    def is_connected() -> bool:
        return False if Machine._conn == None else Machine._conn.is_open
    
    def connect(port: str):
        Machine._conn = serial.Serial(port)
        Machine.send('INIT')
        while Machine._conn.in_waiting < 1:
            pass
        Machine.read()

    def send(data: str):
        Machine._conn.write(data.encode("utf-8"))
        
    def send_wait(data: str):
        if not Machine._sent:
            Machine._sent = True
            Machine.send(data)
            while Machine._conn.in_waiting < 1:
                        time.sleep(0.05)
            Machine._sent = False
            return Machine.read()
        
        
    def read() -> str:
        return Machine._conn.read().decode("utf-8")

    def send_command_async(cmd: str, on_response: Callable[[str], None]):
        if not Machine._sent:
            def aresponse():
                while Machine._conn.in_waiting < 1:
                    time.sleep(0.1)
                
                on_response(Machine.read())
                
                Machine._sent = False
            
            t = threading.Thread(target=aresponse, args=[])
            Machine._sent = True
            Machine.send(cmd)
            t.start()
        
    def get_port_name() -> str:
        return Machine._conn.port
    
    def disconnect():
        Machine._conn.close()