from neutron.base import ResponseBase
from neutron_data import networks
import json
import utils


class ShowNetworks(ResponseBase):

    def path(self):
        return 'networks/'

    def response(self, path):
        network_id = utils.get_id_from_path(path)

        network = networks[network_id]
        return json.dumps({'network': network})
