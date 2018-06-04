# main
import serial
import time


class MySerial:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)

    def query(self, cmd, terminal_char="\n"):
        self.ser.write(cmd.encode())
        print('here1')
        print(self.ser.read())
        print('here2')
        return ''.join(iter(self.ser.read, terminal_char))


s = MySerial("/dev/ttyS0", 9600)
result = s.query("Test\n")
print(result)
