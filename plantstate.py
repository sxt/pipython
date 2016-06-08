#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import urllib2
import json
import sys

if len(sys.argv) != 2:
   print 'Usage: ', sys.argv[0], ' Server-Address'
   sys.exit()

ip = sys.argv[1]

GPIO.setmode(GPIO.BOARD)
plantStatePin = 7
GPIO.setup(plantStatePin, GPIO.IN)

if GPIO.input(7) == 1:
  print("Pin 7 initial state: ON")
else:
  print("Pin 7 initial state: OFF")

def edge(channel):
  #urlBase = "http://127.0.0.1:8880/api"
  urlBase = ip
  newState = GPIO.input(7)
  eventid = 0
  if newState == 1:
    # OK
    print("Pin 7 ON")
    eventid=5
  else:
    # Thirsty
    print("Pin 7 OFF")
    eventid=4

  url = urlBase + "?eventid=" + str(eventid)
  print "Trying API: " + url
  result = json.load(urllib2.urlopen(url))
  print "API Result" + json.dumps(result)

GPIO.add_event_detect(plantStatePin, GPIO.BOTH, callback=edge)

while(1):
  c=0
  #print "Hello\n"

GPIO.cleanup()

