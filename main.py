# main
import serial
import time


class MySerial:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)

    def query(self, cmd, terminal_char="\n"):
        self.ser.write(cmd.encode())
        print('here1')
        cmd_read = self.ser.read()
        print(cmd_read.decode())
        print('here2')
        return 'done'


s = MySerial("/dev/ttyS0", 9600)
result = s.query("Test\n")
print(result)
