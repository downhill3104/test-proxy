#!/usr/bin/env python
"""
This example builds on mitmproxy's base proxying infrastructure to
implement functionality similar to the "sticky cookies" option.

Heads Up: In the majority of cases, you want to use inline scripts.
"""
import os
from libmproxy import controller, proxy
from libmproxy.proxy.server import ProxyServer
from libmproxy.models import decoded
from json import JSONEncoder

class StickyMaster(controller.Master):
    def __init__(self, server):
        controller.Master.__init__(self, server)
        self.stickyhosts = {}

    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, flow):
        flow.reply()

    def handle_response(self, flow):
        with decoded(flow.response):  # automatically decode gzipped responses.
            #print(flow.response.content)
            print(flow.response._assemble())
        
        flow.reply()


config = proxy.ProxyConfig(port=8080)
server = ProxyServer(config)
m = StickyMaster(server)
m.run()
