# main
import serial
import time
import curses

window = curses.initscr()
window.nodelay(1)



class MySerial:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)

    def query(self, cmd, terminal_char="\n"):
        self.ser.write(cmd.encode())
        print('Ser.in_w:{}'.format(self.ser.in_waiting))
        cmd_read = self.ser.read()
        print(cmd_read.decode())
        return 'done'


while True:
    print("Hello, world!")
    ch = window.getch()
    time.sleep(0.5)
    print(ch)
    if ch == 'q':
        break

#s = MySerial("/dev/ttyS0", 9600)
#result = s.query("Test\n")
#print(result)
