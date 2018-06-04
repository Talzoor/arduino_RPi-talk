# main
import serial
import time
import curses

window = curses.initscr()
window.nodelay(1)



class MySerial:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)

    def write(self, cmd):
        self.ser.write(cmd.encode())
        return 'done'

    def read(self):
        if self.ser.in_waiting:
            self.ch_r += self.ser.read()
        line = ''.join(self.ch_r.decode())
        print(line)
        return ''


s = MySerial("/dev/ttyS0", 9600)

while True:
    ch = window.getch()

    result = s.write("Test\n")
    result = s.read()
    #print(result)

    try:
        if chr(ch).lower() == 'q':
            break
    except:
        pass

curses.endwin()

