#!/usr/bin/python
import sys

option = sys.argv[1]

for option in sys.argv:
   if option.isdigit():
      print "Turning on pin " + option


