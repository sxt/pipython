#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

motionPin = 7
green = 11

GPIO.setup(motionPin, GPIO.IN)
GPIO.setup(green, GPIO.OUT)

while (1==1):
 GPIO.wait_for_edge(motionPin, GPIO.RISING)
 print "motion Detected"
 GPIO.output(green, True)
 GPIO.wait_for_edge(motionPin, GPIO.FALLING)
 print "NO motion Detected"
 GPIO.output(green, False)

GPIO.cleanup()
