from neutron.list_default import ListDefault
from neutron.list_networks import ListNetworks
from neutron.list_ports import ListPorts
from neutron.list_subnets import ListSubnets


from neutron.show_networks import ShowNetworks
from neutron.show_ports import ShowPorts
from neutron.show_subnets import ShowSubnets

from neutron.update_ports import UpdatePorts


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
get_responses[response_subnets.path()] = response_default


ports = ShowPorts()
get_responses[ports.path()] = ports

networks = ShowNetworks()
get_responses[networks.path()] = networks

subnets = ShowSubnets()
get_responses[subnets.path()] = subnets


ports = UpdatePorts()
post_responses[ports.path()] = ports
