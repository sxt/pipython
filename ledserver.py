#!/usr/bin/python
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import RPi.GPIO as GPIO
import time

import cgi

class FormPage(Resource):
    def __init__(self):
        return

    def render_GET(self, request):
        return '<html><body><form method="POST">Toggle LED: <input type="submit" name="Go" /></form></body></html>'

    def render_POST(self, request):
        state = ""
        if GPIO.input(7) == 0:
          GPIO.output(7, True)
          state = "ON"
        else:
          GPIO.output(7, False)
          state = "OFF"
        return '<html><body><p>Toggled! Light is now ' + state +  '</p><form method="POST">Toggle LED:<input type="submit" name="Go" /></form></body></html>'

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(7, GPIO.OUT)
root = Resource()
root.putChild("form", FormPage())
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
