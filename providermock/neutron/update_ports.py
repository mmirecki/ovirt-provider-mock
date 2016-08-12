from neutron.base import ResponseBase
from neutron_data import ports
import json

# REST:
# POST: http://localhost:9696/v2.0/ports
# { "port" : {"name" : "name","network_id" : "network_id","device_id" : "device_id","mac_address" : "mac_address","device_owner" : "device_owner","admin_state_up" : "admin_state_up","binding:host_id" : "binding:host_id"}}


class UpdatePorts(ResponseBase):

    def path(self):
        return 'ports'

    def response(self, path, content):

        content_json = json.loads(content)

        received_port = content_json['port']
        port = dict()

        #  The port id 'id' will be passed to the VIF driver as "vnic_id"
        if getattr(received_port, 'id', None):  # existing port is updated
            port_id = received_port['id']
        else:  # if port has no id, create a new one
            port_id = 'port_id_' + str(len(ports) + 1)

        # only copy the relevant keys, fail if any of them is missing
        port['id'] = port_id
        port['name'] = received_port['name']  # vm nic name (eg. ens3)
        port['network_id'] = received_port['network_id']  # external network id
        port['device_id'] = received_port['device_id']  # vm nic id
        port['mac_address'] = received_port['mac_address']  # vm nic mac
        port['device_owner'] = received_port['device_owner']  # always 'oVirt'
        port['admin_state_up'] = received_port['admin_state_up']
        port['binding:host_id'] = received_port['binding:host_id']

        print "UPDATE PORT:" + str(port)
        ports[port_id] = port
        return json.dumps({'port': port})
