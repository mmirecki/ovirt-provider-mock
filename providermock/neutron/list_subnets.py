from neutron.base import ResponseBase
from neutron_data import subnets
import json


class ListSubnets(ResponseBase):

    def path(self):
        return 'subnets'

    def response(self, path):

        response_subnets = []
        for subnet in subnets.itervalues():
            response_subnets.append(subnet)

        return json.dumps({
            "subnets": response_subnets
        })
