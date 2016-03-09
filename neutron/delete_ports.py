from neutron.base import PostResponseBase
from neutron_data import ports
import json
import utils


class DeletePorts(PostResponseBase):

    def path(self):
        return 'ports'

    def response(self, path, content):
        port_id = utils.get_id_from_path(path)
        if port_id in ports:
            del(ports[port_id])
