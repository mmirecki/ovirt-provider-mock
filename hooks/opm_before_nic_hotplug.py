#!/usr/bin/python
import os
import hooking
from vdsm.netinfo import DUMMY_BRIDGE
import opm_common

VNIC_ID_KEY = 'vnic_id'
PROVIDER_TYPE_KEY = 'provider_type'
OPENSTACK_NET_PROVIDER_TYPE = 'OPENSTACK_NETWORK'

"""
This script

"""

def main():
    provider_type = os.environ.get(PROVIDER_TYPE_KEY, None)
    if not provider_type or provider_type != OPENSTACK_NET_PROVIDER_TYPE:
        return

    vnic_id = os.environ.get(VNIC_ID_KEY, None)
    if not vnic_id:
        return

    domxml = hooking.read_domxml()

    connect_to_new_network(domxml, vnic_id, provider_type)
    #connect_to_existing_network(domxml)

    hooking.write_domxml(domxml)


def connect_to_new_network(domxml, vnic_id, provider_type):

    iface = domxml.getElementsByTagName('interface')[0]
    source = iface.getElementsByTagName('source')[0]
    bridge_name = source.getAttribute('bridge')

    opm_common.add_bridge(bridge_name)
    opm_common.add_libvirt_network(bridge_name)


def connect_to_existing_network(domxml):
    source_bridge = DUMMY_BRIDGE

    iface = domxml.getElementsByTagName('interface')[0]
    source = iface.getElementsByTagName('source')[0]
    bridge_name = source.setAttribute('bridge', source_bridge)

main()

