from neutron.base import PostResponseBase
from neutron_data import networks
import json
import utils


class DeleteNetworks(PostResponseBase):

    def path(self):
        return 'networks'

    def response(self, path, content):
        network_id = utils.get_id_from_path(path)
        if network_id in networks:
            del(networks[network_id])
