# main
import serial
import time
import curses

#window = curses.initscr()
#window.nodelay(1)



class MySerial:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)

    def write(self, cmd):
        self.ser.write(cmd.encode())
        return 'done'

    def read(self):
        ch_r_d = ''
        ch_r = ''
        try:
            nbChars = self.ser.in_waiting
            if nbChars > 0:
                time.sleep(0.005)
                nbChars = self.ser.in_waiting
                ch_r = self.ser.read(nbChars).decode()
        except:
            pass
        return ch_r


s = MySerial("/dev/ttyS0", 9600)
i=0
while True:
    #ch = window.getch()
    i += 1
    #result = s.write("Test{}\n".format(i))
    time.sleep(0.05)
    result = s.read()

    if not result == '':
        #print(result, end='')
        result_w = s.write("Echo:{}\n".format(result))


