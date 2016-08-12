from neutron.base import ResponseBase
from neutron_data import subnets
import json
import utils


class DeleteSubnets(ResponseBase):

    def path(self):
        return 'subnets'

    def response(self, path, content=None):
        subnet_id = utils.get_id_from_path(path)
        if subnet_id in subnets:
            del(subnets[subnet_id])
