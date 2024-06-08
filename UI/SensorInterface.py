import ctypes
from ctypes import wintypes, POINTER, byref, create_string_buffer

class EFSensor():
    __slots__ = ("_library", "_HANDLE", "_connected")

    def __init__(self, dll_filepath: str) -> None:
        self._library = ctypes.windll.LoadLibrary(dll_filepath)

        self._library.PMM_CreateProbe.argtypes = [ctypes.c_char_p, POINTER(wintypes.HANDLE), ctypes.c_char_p]
        self._library.PMM_CreateProbe.restype = ctypes.c_int

        self._library.PMM_ReadTotalField.argtypes = [wintypes.HANDLE, POINTER(ctypes.c_float)]
        self._library.PMM_ReadTotalField.restype = ctypes.c_int

        self._library.PMM_ReadAxisField.argtypes = [wintypes.HANDLE, POINTER(ctypes.c_float), POINTER(ctypes.c_float), POINTER(ctypes.c_float)]
        self._library.PMM_ReadAxisField.restype = ctypes.c_int

        self._library.PMM_SerialNumber.argtypes = [wintypes.HANDLE, ctypes.c_char_p, POINTER(ctypes.c_int)]
        self._library.PMM_SerialNumber.restype = ctypes.c_int

    def is_connected(self) -> bool:
        return self._connected

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


    def connect(self, name: str, comm_port: str) -> None:
        probe_handle = wintypes.HANDLE()

        result = self._library.PMM_CreateProbe(name.encode('utf-8'), byref(probe_handle), comm_port.encode('utf-8'))
        
        EFSensor.handle_code(result)

        self._connected = True
        self._HANDLE = probe_handle
        

    def read_total_field(self, probe_handle: wintypes.HANDLE) -> float:
        xyz_field = ctypes.c_float()

        result = self._library.PMM_ReadTotalField(probe_handle, byref(xyz_field))

        EFSensor.handle_code(result)

        return xyz_field.value

    def read_axis_field(self, probe_handle: wintypes.HANDLE) -> tuple[float, float, float]:
        x_field = ctypes.c_float()
        y_field = ctypes.c_float()
        z_field = ctypes.c_float()

        result = self._library.PMM_ReadAxisField(probe_handle, byref(x_field), byref(y_field), byref(z_field))

        EFSensor.handle_code(result)

        return x_field.value, y_field.value, z_field.value
    
    def get_serial_number(self, probe_handle, buffer_size=256):
        serial_number = create_string_buffer(buffer_size)
        array_size = ctypes.c_int(buffer_size)

        result = self._library.PMM_SerialNumber(probe_handle, serial_number, byref(array_size))

        EFSensor.handle_code(result)

        return serial_number.value.decode('utf-8')