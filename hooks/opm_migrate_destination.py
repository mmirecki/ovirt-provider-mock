#!/usr/bin/python
import hooking
from vdsm.network.configurators import libvirt
from vdsm import netinfo
import opm_common

VNIC_ID_KEY = 'vnic_id'
PROVIDER_TYPE_KEY = 'provider_type'
OPENSTACK_NET_PROVIDER_TYPE = 'OPENSTACK_NETWORK'


def main():
    domxml = hooking.read_domxml()
    interfaces = domxml.getElementsByTagName('interface')
    for iface in interfaces:
        source = iface.getElementsByTagName('source')[0]
        bridge_name = source.getAttribute('bridge')
        opm_common.add_bridge(bridge_name)
        opm_common.add_libvirt_network(bridge_name)

main()
