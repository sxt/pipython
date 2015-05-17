#!/usr/bin/python
from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
import time

import cgi

class StateApi(Resource):
    def __init__(self):
        return

    def render_GET(self, request):
        print "Request Received"
        state = cgi.escape(request.args["state"][0])
        request.setHeader("content-type", "application/json")
        return '{ "result" : "success", "state" : ' + state + ' }'

root = Resource()
root.putChild("api", StateApi())
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()

