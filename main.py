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
        try:
            #print('in_w:{}'.format(self.ser.in_waiting))
            if self.ser.in_waiting:
                time.sleep(0.005)
                ch_r = self.ser.read()
                print('{}'.format(ch_r.decode()), end='')
                #self.ch_r += self.ser.read()

            #line = ''.join(self.ch_r.decode())
            #print(line)
        except:
            pass
        return ''


s = MySerial("/dev/ttyS0", 9600)
i=0
while True:
    #ch = window.getch()
    i += 1
    result = s.write("Test{}\n".format(i))
    time.sleep(0.5)
    result = s.read()

    #print(result)

    #try:
        #if chr(ch).lower() == 'q':
            #break
    #except:
    #    pass

#curses.endwin()

