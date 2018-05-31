# main
import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.close()
ser.open()

data = "test!"
ser.write(data.encode())

try:
    while 1:
        response = ser.readline()
        print(response)

except KeyboardInterrupt:
    ser.close()
