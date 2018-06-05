# main
from __future__ import print_function
import serial
import time
import curses

#window = curses.initscr()
#window.nodelay(1)


class SendCommand:
    def __init__(self, stp_pin, dir_pin, en_pin):
        self.stp_pin = stp_pin
        self.dir_pin = dir_pin
        self.en_pin = en_pin

    def init_seq(self):
        _str_to_send = ''
        return _str_to_send

    def move(self, _steps, _dir):
        _str_to_send = ''
        return _str_to_send

    def moveto(self, _pos, _dir):
        _str_to_send = ''
        return _str_to_send

    def define_vel_acc(self, _vel, _acc):
        _str_to_send = ''
        return _str_to_send





class MySerial:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)

    def write(self, cmd):
        if not cmd='':
            print('cmd:{}'.format(cmd))
            self.ser.write(cmd.encode())
        return 'done'

    def read(self):
        ch_r_d = ''
        ch_r = ''
        try:
            nbChars = self.ser.in_waiting
            if nbChars > 0:
                time.sleep(0.05)
                nbChars = self.ser.in_waiting
                ch_r = self.ser.read(nbChars)
                ch_r = ch_r.decode()
        except:
            pass
        return ch_r


s = MySerial("/dev/ttyS0", 9600)
command = SendCommand(0, 1, 2)
i=0
while True:
    #ch = window.getch()
    i += 1
    #result = s.write("Test{}\n".format(i))
    time.sleep(0.05)
    result = s.read()

    if not result == '':
        print('Got:{0}'.format(result), end='')
        result_w = s.write('Echo:{}'.format(result))


