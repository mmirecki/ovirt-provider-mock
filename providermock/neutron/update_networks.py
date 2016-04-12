from neutron.base import PostResponseBase
from neutron_data import networks
import json

# REST:
# POST: http://localhost:9696/v2.0/networks
# { "network" :{"name": "net1"}}
# { "network" :{"name": "net1","admin_state_up" : true,"tenant_id" : "oVirt",
# "provider:physical_network" : "physical_network",
# "provider:network_type" : "vlan", "provider:segmentation_id" : 7}}



class UpdateNetworks(PostResponseBase):

    def path(self):
        return 'networks'

    def response(self, path, content):

        content_json = json.loads(content)

        received_network = content_json['network']
        network = dict()

        #  The port id 'id' will be passed to the VIF driver as "vnic_id"
        if getattr(received_network, 'id', None):  # existing port is updated
            network_id = received_network['id']
        else:  # if port has no id, create a new one
            network_id = 'network_id_' + self.generate_id()

        # only copy the relevant keys, fail if any of them is missing
        network['id'] = network_id
        network['name'] = received_network['name']

        if 'admin_state_up' in received_network:
            network['admin_state_up'] = received_network['admin_state_up']

        if 'tenant_id' in received_network:
            network['tenant_id'] = received_network['tenant_id']
        if 'provider:physical_network' in received_network:
            network['provider:physical_network'] = received_network['provider:physical_network']
        # 'vlan' if a vlan network
        if 'provider:network_type' in received_network:
            network['provider:network_type'] = received_network['provider:network_type']
        # vlan segment
        if 'provider:segmentation_id' in received_network:
            network['provider:segmentation_id'] = received_network['provider:segmentation_id']

        print "UPDATE NETWORK:" + str(network)
        networks[network_id] = network
        return json.dumps({'network': network})
