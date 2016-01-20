#!/usr/bin/env python

import hooking
import json

caps = hooking.read_json()
networks = caps['networks']

# Update networks with the provider managed network
# An example off adding network "public" to the caps info

networks['public'] = {
    "iface": "public",
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
    "ports": ["ens11"]
}

hooking.write_json(caps)
