#!/usr/bin/python

import serial
# set up the serial connection speed
ser = serial.Serial('/dev/ttyACM0', 9600)

# main loop
while 1:
    c = input('Enter a char: ')
    if len(c) == 1:
        # send data to the Arduino
        ser.write(c.encode())
        
        # receive data from the Arduino
        response = ser.readline()
        print(response.decode().strip())

