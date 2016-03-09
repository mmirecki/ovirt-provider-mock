from neutron.base import ResponseBase
from neutron_data import networks
import json


class ListNetworks(ResponseBase):

    def path(self):
        return 'networks'

    def response(self, path):

        response_networks = []
        for network in networks.itervalues():
            response_networks.append(network)

        return json.dumps({
            "networks": response_networks
        })
