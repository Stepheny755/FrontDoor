import serial

arduino = serial.Serial('COM7',115200,timeout=0.1)

while True:
	data = arduino.readline()[:-2]
	if data:
		print(data)
