from neutron.base import PostResponseBase
from neutron_data import ports
import json
from utils import get_id_from_path
from utils import update_field_if_present
# REST:
# PUT: http://localhost:9696/v2.0/ports
# { "port" : {"name" : "name","network_id" : "network_id","device_id" : "device_id","mac_address" : "mac_address","device_owner" : "device_owner","admin_state_up" : "admin_state_up","binding:host_id" : "binding:host_id"}}


class PutPorts(PostResponseBase):

    def path(self):
        return 'ports'

    def response(self, path, content):

        content_json = json.loads(content)

        received_port = content_json['port']

        port_id = get_id_from_path(path)
        port = ports[port_id]

        # only copy the relevant keys, fail if any of them is missing
        update_field_if_present(port, received_port, 'name')
        update_field_if_present(port, received_port, 'network_id')
        update_field_if_present(port, received_port, 'device_id')
        update_field_if_present(port, received_port, 'mac_address')
        update_field_if_present(port, received_port, 'device_owner')
        update_field_if_present(port, received_port, 'admin_state_up')
        update_field_if_present(port, received_port, 'binding:host_id')

        print "PUT PORT:" + str(port)
        # ports[port_id] = port
        return json.dumps({'port': port})
