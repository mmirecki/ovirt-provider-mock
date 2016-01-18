#!/usr/bin/python
import os
import sys
import traceback
from xml.dom import minidom
import hooking
from vdsm.netinfo import DUMMY_BRIDGE
import subprocess


VNIC_ID_KEY = 'vnic_id'
PROVIDER_TYPE_KEY = 'provider_type'
OPENSTACK_NET_PROVIDER_TYPE = 'OPENSTACK_NETWORK'
BRIDGE_INTERFACE = 'ens11'

XML1 = """
<interface type="bridge">
    <address bus="0x00" domain="0x0000" function="0x0" slot="0x0a" type="pci"/>
    <mac address="00:1a:4a:16:01:56"/>
    <model type="virtio"/>
    <source bridge="public"/>
    <filterref filter="vdsm-no-mac-spoofing"/>
    <link state="up"/>
    <bandwidth/>
</interface>
"""


def main():
    provider_type = os.environ[PROVIDER_TYPE_KEY]
    if not provider_type or provider_type != OPENSTACK_NET_PROVIDER_TYPE:
        return

    vnic_id = os.environ[VNIC_ID_KEY]
    if not vnic_id:
        return

    domxml = hooking.read_domxml()

    result_domxml = connect_nic(domxml, vnic_id, provider_type)

    hooking.write_domxml(result_domxml)


def test():
    result_domxml = connect_nic(minidom.parseString(XML1), '', '')
    print(result_domxml)


def connect_nic(domxml, vnic_id, provider_type):

    add_and_connect_to_new_network(domxml)

    return domxml


def add_and_connect_to_new_network(domxml):
    iface = domxml.getElementsByTagName('interface')[0]
    source = iface.getElementsByTagName('source')[0]
    bridge_name = source.getAttribute('bridge')
    if not does_bridge_exist(bridge_name):
        add_bridge(bridge_name)


def connect_to_existing_network(domxml):
    source_bridge = DUMMY_BRIDGE

    iface = domxml.getElementsByTagName('interface')[0]
    source = iface.getElementsByTagName('source')[0]
    bridge_name = source.setAttribute('bridge', source_bridge)

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


def add_bridge(bridge_name):
    run(['/sbin/brctl', 'addbr', bridge_name])
    run(['/sbin/brctl', 'addif', bridge_name, BRIDGE_INTERFACE])


def does_bridge_exist(bridge_name):
    return bridge_name in get_all_bridges()


def get_all_bridges():
    process_output = run(['brctl', 'show'])
    output_lines = process_output.splitlines()[1:]
    tokenized_lines = map(str.split, output_lines)
    bridge_lines = filter(lambda bridge_tokens: len(bridge_tokens) > 1, tokenized_lines)
    bridge_names = map(lambda tokens: tokens[0], bridge_lines)
    return bridge_names


main()
#test()
