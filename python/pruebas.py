import serial, time
arduino = serial.Serial('COM6', 9600)
time.sleep(2)
rawString = arduino.readline()
print(rawString)
arduino.close()