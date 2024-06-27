import os
import subprocess
from typing import Self

class SensorProxy:
    __instance = None

    __slots__ = ('__proc')

    def __init(self):
        # Path to the 32-bit Python interpreter
        worker_script_path = os.path.curdir + "\\SensorInterface.py"

        # Start the 32-bit Python process
        self.__proc = subprocess.Popen(["py", "-3.12-32", worker_script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    @staticmethod
    def get_instance() -> Self:
        if SensorProxy.__instance == None:
            SensorProxy.__instance = SensorProxy()
            SensorProxy.__instance.__init()

        return SensorProxy.__instance

    def __getattr__(self, name: str) -> str:
        def ret(): # Returns a function, so it can be called through a thread
            self.__proc.stdin.write(name.encode() + b'\n')
            self.__proc.stdin.flush()
            return self.__proc.stdout.readline().decode().strip()

        return ret 

if __name__=='__main__':
    sp = SensorProxy.get_instance()
    sp.exit()
