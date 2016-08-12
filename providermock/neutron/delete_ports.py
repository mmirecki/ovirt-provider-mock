from neutron.base import ResponseBase
from neutron_data import ports
import json
import utils


class DeletePorts(ResponseBase):

    def path(self):
        return 'ports'

    def response(self, path, content=None):
        port_id = utils.get_id_from_path(path)
        if port_id in ports:
            del(ports[port_id])
