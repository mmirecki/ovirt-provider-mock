#!/usr/bin/env python

import hooking
import json

network_name = "public"
nic_name = "ens17"

caps = hooking.read_json()
networks = caps['networks']
bridges = caps['bridges']
nics = caps['nics']

if networks.get(network_name, None):
    hooking.exit_hook("", return_code=0)

"""
Update networks with the provider managed network
An example off adding network <network_name> to the caps info (if the network
does not exist)
"""

networks[network_name] = {
    "iface": network_name
}

bridges[network_name] = {
    "ports": [nic_name]
}

nic = nics.get(nic_name, None)
if nic:  # if the nic exists, do nothing
    nics[nic_name]["ports"] = [nic_name]
else:  # if the nic does not exist, add it to the results
    nics[nic_name] = {}

hooking.write_json(caps)
hooking.exit_hook("", return_code=0)


"""
In case you need to pass more information about the above configuration items,
below is a more complete configuration:
"""


networks[network_name] = {
    "iface": network_name,
    "addr": "",
    "cfg":
    {
        "IPV6INIT": "no",
        "DEFROUTE": "no",
        "HOTPLUG": "no",
        "MTU": "1500",
        "DELAY": "0",
        "NM_CONTROLLED": "no",
        "BOOTPROTO": "none",
        "STP": "off",
        "DEVICE": "public",
        "TYPE": "Bridge",
        "ONBOOT": "yes"
    },
    "bridged": True,
    "ipv6addrs": [],
    "gateway": "",
    "dhcpv4": False,
    "netmask": "",
    "dhcpv6": False,
    "stp": "off",
    "ipv4addrs": [],
    "mtu": "1500",
    "ipv6gateway": "::",
    "ports": [nic_name]
}

bridges[network_name] = {
    "addr": "",
    "cfg": {"BOOTPROTO": "none"},
    "ipv6addrs": [],
    "mtu": "1500",
    "dhcpv4": False,
    "netmask": "",
    "dhcpv6": False,
    "stp": "off",
    "ipv4addrs": [],
    "ipv6gateway": "::",
    "gateway": "",
    "opts": {
        "multicast_last_member_count": "2",
        "vlan_protocol": "0x8100",
        "hash_elasticity": "4",
        "multicast_query_response_interval": "1000",
        "group_fwd_mask": "0x0",
        "multicast_snooping": "1",
        "multicast_startup_query_interval": "3125",
        "hello_timer": "0",
        "multicast_querier_interval": "25500",
        "max_age": "2000",
        "hash_max": "512",
        "stp_state": "0",
        "topology_change_detected": "0",
        "priority": "32768",
        "multicast_membership_interval": "26000",
        "root_path_cost": "0",
        "root_port": "0",
        "multicast_querier": "0",
        "multicast_startup_query_count": "2",
        "nf_call_iptables": "0",
        "hello_time": "200",
        "topology_change": "0",
        "bridge_id": "8000.fe1a4a160153",
        "topology_change_timer": "0",
        "ageing_time": "30000",
        "nf_call_ip6tables": "0",
        "gc_timer": "0",
        "root_id": "8000.fe1a4a160153",
        "nf_call_arptables": "0",
        "group_addr": "1:80:c2:0:0:0",
        "multicast_last_member_interval": "100",
        "default_pvid": "1",
        "multicast_query_interval": "12500",
        "multicast_query_use_ifaddr": "0",
        "tcn_timer": "0",
        "multicast_router": "1",
        "vlan_filtering": "0",
        "forward_delay": "1500"
    },
    "ports": [nic_name]
}

nics[nic_name] = {
    "addr": "",
    "cfg": {
        "BRIDGE": network_name,
        "IPV6INIT": "no",
        "MTU": "1500",
        "NM_CONTROLLED": "no",
        "BOOTPROTO": "none",
        "DEVICE": nic_name,
        "ONBOOT": "yes"
    },
    "ipv6addrs": ["fe80::5054:ff:fec8:3205/64"],
    "mtu": "1500",
    "dhcpv4": False,
    "netmask": "",
    "dhcpv6": False,
    "ipv4addrs": [],
    "hwaddr": "52:54:00:c8:32:05",
    "ipv6gateway": "::",
    "gateway": "",
    "speed": 0
}
