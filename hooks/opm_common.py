from vdsm.network.configurators import libvirt
from vdsm import netinfo
import hooking


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
        #
        try:
            create_bridge(bridge_name)
        except:
            pass

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
