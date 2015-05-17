#!/usr/bin/python

import serial
# set up the serial connection speed
ser = serial.Serial('/dev/ttyACM0', 9600)

# main loop
while 1:
        # receive data from the Arduino
        response = ser.readline()
        decodedResponse = response.decode().strip()
	print(decodedResponse)

	
