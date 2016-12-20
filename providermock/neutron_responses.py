# Copyright 2016 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
from __future__ import absolute_import

import json
import time

from neutron_data import networks
from neutron_data import ports
from neutron_data import subnets

GET = 'GET'  # list of entities
SHOW = 'SHOW'  # concrete entity
DELETE = 'DELETE'
POST = 'POST'
PUT = 'PUT'

NETWORKS = 'networks'
PORTS = 'ports'
SUBNETS = 'subnets'


_responses = {}


def rest(method, path):
    """
    Decorator for adding rest request handling methods.
    method -- rest method of the arriving request: GET/POST/DELETE/PUT
    path -- the path of the arriving request
    For example the function handling the following request:
    GET: http://<host>/../networks
    would have to be decorated with:
    rest('GET', 'networks')
    """
    def assign_response(funct):
        if method not in _responses:
            _responses[method] = {}
        _responses[method][path] = funct
        return funct
    return assign_response


def generate_id():
    return str(int(time.time()))


@rest(SHOW, NETWORKS)
def show_network(content, id=None):
        network = networks[id]
        return json.dumps({'network': network})


@rest(SHOW, PORTS)
def show_port(content, id=None):
        port = ports[id]
        return json.dumps({'port': port})


@rest(SHOW, SUBNETS)
def show_subnet(content, id):
        subnet = subnets[id]
        return json.dumps({'subnet': subnet})


@rest(GET, '')
def get_default(content, id):
    return json.dumps({})


@rest(GET, NETWORKS)
def get_networks(conten, id):
    response_networks = []
    for network in networks.itervalues():
        response_networks.append(network)

    return json.dumps({
        "networks": response_networks
    })



@rest(GET, PORTS)
def get_ports(content, id):
    response_ports = []
    for port in ports.itervalues():
        response_ports.append(port)

    return json.dumps({
        "ports": response_ports
    })


@rest(GET, SUBNETS)
def get_subnets(content, id):
    response_subnets = []
    for subnet in subnets.itervalues():
        response_subnets.append(subnet)

    return json.dumps({
        "subnets": response_subnets
    })


@rest(DELETE, NETWORKS)
def delete_network(content=None, id=None):
    if id is not None:
        if id in networks:
            del(networks[id])


@rest(DELETE, PORTS)
def delete_port(content=None, id=None):
    if id is not None:
        if id in ports:
            del(ports[id])


@rest(DELETE, SUBNETS)
def delete_subnet(content, id):
    if id is not None:
        if id in subnets:
            del(subnets[id])


@rest(POST, NETWORKS)
def post_networks(content, id):
    content_json = json.loads(content)

    received_network = content_json['network']
    network = dict()

    #  The port id 'id' will be passed to the VIF driver as "vnic_id"
    if getattr(received_network, 'id', None):  # existing port is updated
        network_id = received_network['id']
    else:  # if port has no id, create a new one
        network_id = 'network_id_' + generate_id()

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


@rest(POST, PORTS)
def post_ports(content, id):
    content_json = json.loads(content)

    received_port = content_json['port']
    port = dict()

    #  The port id 'id' will be passed to the VIF driver as "vnic_id"
    if getattr(received_port, 'id', None):  # existing port is updated
        port_id = received_port['id']
    else:  # if port has no id, create a new one
        port_id = 'port_id_' + generate_id()

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


@rest(POST, SUBNETS)
def post_subnets(content, id):
    content_json = json.loads(content)
    received_subnet = content_json['subnet']
    subnet = dict()

    # generate some new id for the subnet
    subnet_id = 'subnet_id_' + generate_id()

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


@rest(PUT, PORTS)
def put_ports(content, id):
    if not id:
        raise Exception('No port id in POST request')

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


@rest(GET, 'tech')
def get_debug(content, id):
    result = 'DEBUG DUMP\n\n\n'

    result += 'NETWORKS:\n\n'
    result += json.dumps(networks)

    result += '\n\n'
    result += 'SUBNETS:\n\n'
    result += json.dumps(subnets)

    result += '\n\n'
    result += 'PORTS:\n\n'
    result += json.dumps(ports)

    return result


def responses():
    return _responses
