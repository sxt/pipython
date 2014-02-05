#!/usr/bin/python
import sys

print "Hello " + sys.argv[1]

option = sys.argv[1]

if option == "1":
   print "Turning on pin 1"
else:
   print "Turning on pin 10"


