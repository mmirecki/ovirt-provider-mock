'''
This is a test query the engine performs to check that connection to the
provider can be successfully established.
The reply is not parsed, only the status of the connection is checked.

Query from ovirt engine:
GET: http://<host>:<port-default:9696>/v2.0/
Headers:
     Accept=application/json
     X-Auth-Token=<token from authentication request>

Minimal response from provider:
Response code: 200
Required headers: "Content-Type", "Application/json"
Body: anything, ovirt engine just checks the response code
'''

from neutron.base import ResponseBase
from neutron_data import networks
from neutron_data import subnets
from neutron_data import ports
import json


class Debug(ResponseBase):

    def path(self):
        return 'debug'

    def response(self, path):

        result = 'DEBUG DUMP\n\n\n'

        result += 'NETWORKS:\n\n'
        result += json.dumps(networks)

        result += '\n\n'
        result += 'SUBNETS:\n\n'
        result += json.dumps(subnets)

        result += '\n\n'
        result += 'PORTS:\n\n'
        result += json.dumps(ports)

        return result
