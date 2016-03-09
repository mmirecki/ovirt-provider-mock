from neutron.base import PostResponseBase
from neutron_data import subnets
import json
import utils


class DeleteSubnets(PostResponseBase):

    def path(self):
        return 'subnets'

    def response(self, path, content):
        subnet_id = utils.get_id_from_path(path)
        if subnet_id in subnets:
            del(subnets[subnet_id])
