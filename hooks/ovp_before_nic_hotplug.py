#!/usr/bin/python
import os
from xml.dom import minidom
import hooking
from vdsm.netinfo import DUMMY_BRIDGE
from vdsm.network.configurators import libvirt
from vdsm import netinfo

VNIC_ID_KEY = 'vnic_id'
PROVIDER_TYPE_KEY = 'provider_type'
OPENSTACK_NET_PROVIDER_TYPE = 'OPENSTACK_NETWORK'


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

    add_bridge(bridge_name)
    add_libvirt_network(bridge_name)


def add_libvirt_network(bridge_name):
    net = libvirt.getNetworkDef("public")
    if not net:
        net_xml = "<network><name>" + netinfo.LIBVIRT_NET_PREFIX + \
            bridge_name + \
            "</name><forward mode='bridge' /><bridge name='" + bridge_name +\
            "' /></network>"
        libvirt.createNetwork(net_xml)


def add_bridge(bridge_name):
    if not does_bridge_exist(bridge_name):
        create_bridge(bridge_name)


"""
Not persistant
Requires modyfing the following in /etc/sudoers.d/50_vdsm on host
Cmnd_Alias VDSM_NET = \
    /sbin/brctl
vdsm  ALL=(ALL) NOPASSWD: VDSM_LIFECYCLE, VDSM_STORAGE, VDSM_NET
"""


def run(cmd):
    rc, out, err = hooking.execCmd(cmd, sudo=True)
    return out


def create_bridge(bridge_name):
    run(['/sbin/brctl', 'addbr', bridge_name])
    run(['/sbin/brctl', 'addif', bridge_name, "ens11"])


def does_bridge_exist(bridge_name):
    return bridge_name in get_all_bridges()


def get_all_bridges():
    process_output = run(['brctl', 'show'])
    output_lines = process_output[1:]
    tokenized_lines = map(str.split, output_lines)
    bridge_lines = filter(lambda bridge_tokens: len(bridge_tokens) > 1,
                          tokenized_lines)
    bridge_names = map(lambda tokens: tokens[0], bridge_lines)
    return bridge_names


def connect_to_existing_network(domxml):
    source_bridge = DUMMY_BRIDGE

    iface = domxml.getElementsByTagName('interface')[0]
    source = iface.getElementsByTagName('source')[0]
    bridge_name = source.setAttribute('bridge', source_bridge)

main()
