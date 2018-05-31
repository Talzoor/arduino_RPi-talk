# main
import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.close()
ser.open()

data = "test!"

try:
    while 1:
        print('here')

        ser.write(data.encode())
        print('sent')
        time.sleep(1)
        if ser.inWaiting():
            response = ser.readline()
            print(response)

except KeyboardInterrupt:
    ser.close()
