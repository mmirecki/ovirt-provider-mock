from neutron.list_default import ListDefault
from neutron.list_networks import ListNetworks
from neutron.list_ports import ListPorts
from neutron.list_subnets import ListSubnets


from neutron.show_networks import ShowNetworks
from neutron.show_ports import ShowPorts
from neutron.show_subnets import ShowSubnets

from neutron.update_ports import UpdatePorts
from neutron.update_subnets import UpdateSubnets

from neutron.delete_networks import DeleteNetworks
from neutron.delete_ports import DeletePorts
from neutron.delete_subnets import DeleteSubnets


get_responses = dict()
post_responses = dict()
delete_responses = dict()


response_default = ListDefault()
get_responses[response_default.path()] = response_default

response_ports = ListPorts()
get_responses[response_ports.path()] = response_ports

response_networks = ListNetworks()
get_responses[response_networks.path()] = response_networks

response_subnets = ListSubnets()
get_responses[response_subnets.path()] = response_subnets


show_ports = ShowPorts()
get_responses[show_ports.path()] = show_ports

show_networks = ShowNetworks()
get_responses[show_networks.path()] = show_networks

show_subnets = ShowSubnets()
get_responses[show_subnets.path()] = show_subnets


update_ports = UpdatePorts()
post_responses[update_ports.path()] = update_ports

update_subnets = UpdateSubnets()
post_responses[update_subnets.path()] = update_subnets


delete_networks = DeleteNetworks()
delete_responses[delete_networks.path()] = delete_networks

delete_ports = DeletePorts()
delete_responses[delete_ports.path()] = delete_ports

delete_subnets = DeleteSubnets()
delete_responses[delete_subnets.path()] = delete_subnets
