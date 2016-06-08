#!/usr/bin/python
import time
import urllib2
import json

#urlBase = "http://127.0.0.1:8880/api"
urlBase = "http://192.168.1.11:8081/"
eventid=5
url = urlBase + "?eventid=" + str(eventid)
print "Trying API: " + url
result = json.load(urllib2.urlopen(url))
print "API Result" + result

