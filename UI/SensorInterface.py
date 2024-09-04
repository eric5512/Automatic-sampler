import ctypes
import ctypes.wintypes
from ctypes import wintypes, POINTER, byref, create_string_buffer
import os
import sys

class EFSensor():
    __connected = False
    __library = None
    _handle = wintypes.HANDLE()

    @staticmethod
    def is_connected() -> bool:
        return EFSensor.__connected

    @staticmethod
    def init(dll_filepath: str) -> None:
        EFSensor.__library = ctypes.windll.LoadLibrary(dll_filepath)
        EFSensor.__library.PMM_CreateProbe.argtypes = [ctypes.c_char_p, POINTER(wintypes.HANDLE), ctypes.c_char_p]
        EFSensor.__library.PMM_CreateProbe.restype = ctypes.c_int

        EFSensor.__library.PMM_ReadTotalField.argtypes = [wintypes.HANDLE, POINTER(ctypes.c_float)]
        EFSensor.__library.PMM_ReadTotalField.restype = ctypes.c_int

        EFSensor.__library.PMM_ReadAxisField.argtypes = [wintypes.HANDLE, POINTER(ctypes.c_float), POINTER(ctypes.c_float), POINTER(ctypes.c_float)]
        EFSensor.__library.PMM_ReadAxisField.restype = ctypes.c_int

        EFSensor.__library.PMM_SerialNumber.argtypes = [wintypes.HANDLE, ctypes.c_char_p, POINTER(ctypes.c_int)]
        EFSensor.__library.PMM_SerialNumber.restype = ctypes.c_int

    @staticmethod
    def handle_code(code: int) -> None:
        match code:
            case 1:
                raise RuntimeError("Bad Handle")
            case 2:
                raise RuntimeError("Unable to open port")
            case 3:
                raise RuntimeError("Not connected")
            case 4:
                raise RuntimeError("Wrong response")
            case 5:
                raise RuntimeError("No response")
            case 6:
                raise RuntimeError("Invalid parameter")
            case 7:
                raise RuntimeError("COMM port busy")
            case 8:
                raise RuntimeError("Timeout")
            case 9:
                raise RuntimeError("COMM port error")
            case 10:
                raise RuntimeError("Problem writing COMM port")
            case 11:
                raise RuntimeError("Read COMM port error")
            case 12:
                raise RuntimeError("Bad connection string")
            case 13:
                raise RuntimeError("Value cannot be set")
            case 14:
                raise RuntimeError("Probe not supported")
            case 15:
                raise RuntimeError("Probe over range")
            case 16:
                raise RuntimeError("Probe under range")
            case 17:
                raise RuntimeError("Error closing COMM port")
            case 18:
                raise RuntimeError("Error purging COMM port")

    @staticmethod
    def connect(comm_port: str) -> str:
        result = EFSensor.__library.PMM_CreateProbe(b'EP600', byref(EFSensor._handle), comm_port.encode('utf-8'))
        
        EFSensor.handle_code(result)
        EFSensor.__connected = True
        return f"Connected to port {comm_port}"


    @staticmethod
    def read_total_field() -> float:
        xyz_field = ctypes.c_float()

        result = EFSensor.__library.PMM_ReadTotalField(EFSensor._handle, byref(xyz_field))

        EFSensor.handle_code(result)

        return xyz_field.value

    @staticmethod
    def read_axis_field() -> tuple[float, float, float]:
        x_field = ctypes.c_float()
        y_field = ctypes.c_float()
        z_field = ctypes.c_float()

        result = EFSensor.__library.PMM_ReadAxisField(EFSensor._handle, byref(x_field), byref(y_field), byref(z_field))

        EFSensor.handle_code(result)

        return x_field.value, y_field.value, z_field.value
    
    @staticmethod
    def get_serial_number(buffer_size=256):
        serial_number = create_string_buffer(buffer_size)
        array_size = ctypes.c_int(buffer_size)

        result = EFSensor.__library.PMM_SerialNumber(EFSensor._handle, serial_number, byref(array_size))

        EFSensor.handle_code(result)

        return serial_number.value.decode('utf-8')
    
if __name__=='__main__':
    EFSensor.init(os.getenv("NARDA"))
    while True:
        try:
            func_name = sys.stdin.readline().strip()
            arg = None

            if func_name == "exit":
                break
            
            if ',' in func_name:
                func_name, arg = [i.strip() for i in func_name.split(',')]
            

            func = getattr(EFSensor, func_name, None)
            if func:
                if arg == None:
                    response = func()
                else:
                    response = func(arg)
                sys.stdout.write(str(response) + '\n')
                sys.stdout.flush()
            else:
                raise RuntimeError("Function or attr specified not present")
        except EOFError:
            break