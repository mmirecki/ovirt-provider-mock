from neutron.base import ResponseBase
from neutron_data import subnets
import json
import utils


class ShowSubnets(ResponseBase):

    def path(self):
        return 'subnets'

    def response(self, path):
        subnet_id = utils.get_id_from_path(path)

        subnet = subnets[subnet_id]
        return json.dumps({'subnet': subnet})
