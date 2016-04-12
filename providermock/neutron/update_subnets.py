from neutron.base import PostResponseBase
from neutron_data import subnets
import json
from utils import update_field_if_present


# REST:
# POST: http://localhost:9696/v2.0/subnets
# {"subnet" :{"name": "subnet_name","network_id" : "network_id","ip_version" : "ip_version","cidr" : "cidr","gateway_ip" : "gateway_ip","dns_nameservers" : "dns_nameservers"}}

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
        subnet['cidr'] = received_subnet['cidr']

        update_field_if_present(subnet, received_subnet, 'ip_version')
        update_field_if_present(subnet, received_subnet, 'gateway_ip')
        update_field_if_present(subnet, received_subnet, 'dns_nameservers')

        print "UPDATE SUBNET:" + str(subnet)

        subnets[subnet_id] = subnet

        return json.dumps({'subnet': subnet})
