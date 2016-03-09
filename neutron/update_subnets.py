from neutron.base import PostResponseBase
from neutron_data import subnets
import json


class UpdateSubnets(PostResponseBase):

    def path(self):
        return 'subnets'

    def response(self, path, content):

        content_json = json.loads(content)
        received_subnet = content_json['subnet']
        subnet = dict()

        # generate some new id for the subnet
        subnet_id = 'subnet_id_' + str(len(subnets) + 1)

        # only copy the relevant keys, fail if any of them is missing
        subnet['id'] = subnet_id
        subnet['name'] = received_subnet['name']
        subnet['network_id'] = received_subnet['network_id']
        subnet['ip_version'] = received_subnet['ip_version']
        subnet['cidr'] = received_subnet['cidr']
        subnet['gateway_ip'] = received_subnet['gateway_ip']
        subnet['dns_nameservers'] = received_subnet['dns_nameservers']

        print "UPDATE SUBNET:" + str(subnet)

        subnets[subnet_id] = subnet

        return json.dumps({'subnet': subnet})
