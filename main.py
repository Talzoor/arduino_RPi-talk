# main
import serial
import time


class MySerial:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)

    def query(self, cmd, terminal_char="\r"):
        self.ser.write(cmd)
        return ''.join(iter(self.ser.read, terminal_char))


s = MySerial("/dev/ttyAMA0", 9600)
result = s.query("get -temp\r")
print(result)
