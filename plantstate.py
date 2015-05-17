#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import urllib2
import json

GPIO.setmode(GPIO.BOARD)
plantStatePin = 7
GPIO.setup(plantStatePin, GPIO.IN)

if GPIO.input(7) == 1:
  print("Pin 7 initial state: ON")
else:
  print("Pin 7 initial state: OFF")

def edge(channel):
  #urlBase = "http://127.0.0.1:8880/api"
  urlBase = "http://192.168.1.13:8081/"
  newState = GPIO.input(7)
  if newState == 1:
    print("Pin 7 ON")
  else:
    print("Pin 7 OFF")

  url = urlBase + "?state=" + str(newState)
  print "Trying API: " + url
  result = json.load(urllib2.urlopen(url))

GPIO.add_event_detect(plantStatePin, GPIO.BOTH, callback=edge)

while(1):
  c=0
  #print "Hello\n"

GPIO.cleanup()

