from neutron.base import ResponseBase
from neutron_data import ports
import json


class ListPorts(ResponseBase):

    def path(self):
        return 'ports'

    """
    identified in ovirt by: device_id
    Check how port is created in update_ports.py
    """

    def response(self, path):

        response_ports = []
        for port in ports.itervalues():
            response_ports.append(port)

        return json.dumps({
            "ports": response_ports
        })
