# Usage: mitmdump -s "modify_response_body.py mitmproxy bananas"
# (this script works best with --anticache)
from libmproxy.models import decoded
from pprint import pprint
from netlib.http.http1 import assemble
from datetime import datetime

#def request(context, flow):
    #print(assemble.assemble_request(flow.request))

def response(context, flow):
    print("================================================================")
    print(flow.request.url + ' ' + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print("================================================================")
    print(assemble.assemble_request(flow.request))
    print("================================================================")
    print(assemble.assemble_response(flow.response))
    print("================================================================")
    #pprint(dir(flow.request))
    #print(flow.request.url)
    #print(flow.request.method + ' ' + flow.request.path + ' ' + flow.request.http_version)
    #print(flow.request.headers)
    #print(flow.request.body)
    #    flow.response.content = flow.response.content.replace(
    #        context.old,
    #        context.new)
