#!/usr/bin/python
import sys

all_options = sys.argv

print all_options;

for option in all_options:
   if option.isdigit():
      print "Turning on pin " + option


