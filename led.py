#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(7, GPIO.OUT)
state7 = GPIO.input(7)
GPIO.output(7, True)
time.sleep(5)
GPIO.output(7, False)
