from neutron.base import ResponseBase
from neutron_data import networks
import json
import utils


class DeleteNetworks(ResponseBase):

    def path(self):
        return 'networks'

    def response(self, path, content=None):
        network_id = utils.get_id_from_path(path)
        if network_id in networks:
            del(networks[network_id])
