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
            #print('in_w:{}'.format(self.ser.in_waiting))
            nbChars = self.ser.in_waiting
            if nbChars > 0:
                ch_r = self.ser.read(nbChars)
                print(ch_r)
                #ch_r_d = ch_r.decode()
                #time.sleep(0.0005)
                #print('{}'.format(ch_r_d), end='')
                #self.ch_r += self.ser.read()

            #line = ''.join(self.ch_r.decode())
            #print(line)
        except:
            pass
        return ch_r


s = MySerial("/dev/ttyS0", 9600)
i=0
while True:
    #ch = window.getch()
    i += 1
    result = s.write("Test{}\n".format(i))
    time.sleep(0.5)
    result = s.read()

    if not result=='':
        print(result)

    #try:
        #if chr(ch).lower() == 'q':
            #break
    #except:
    #    pass

#curses.endwin()

