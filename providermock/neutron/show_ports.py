from neutron.base import ResponseBase
from neutron_data import ports
import json
import utils


class ShowPorts(ResponseBase):

    def path(self):
        return 'ports'

    def response(self, path):
        port_id = utils.get_id_from_path(path)

        port = ports[port_id]
        return json.dumps({'port': port})
