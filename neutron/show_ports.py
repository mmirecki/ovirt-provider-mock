from neutron.base import ResponseBase


class ShowPorts(ResponseBase):

    def path(self):
        return 'ports/'

    def response(self, path):
        return """
{"port":
    {
        "status": "DOWN",
        "binding:host_id": "localhost.localdomain",
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "dns_assignment": [
            {
                "hostname": "host-172-24-4-226",
                "ip_address": "172.24.4.226",
                "fqdn": "host-172-24-4-226.openstacklocal."
            }
        ],
        "device_owner": "network:router_gateway",
        "binding:profile": {},
        "fixed_ips": [
            {
                "subnet_id": "dc594048-a9e2-4ec9-9928-4157cea7e530",
                "ip_address": "172.24.4.226"
            }
        ],
        "id": "2aec1577-8777-4b66-b6fc-c88109d28135",
        "security_groups": [],
        "device_id": "c80019b4-e478-4f62-8817-7ee79bca285c",
        "name": "",
        "admin_state_up": true,
        "network_id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
        "dns_name": "",
        "binding:vif_details":
        {
            "port_filter": true,
            "ovs_hybrid_plug": true
        },
        "binding:vnic_type": "normal",
        "binding:vif_type": "ovs",
        "tenant_id": "",
        "mac_address": "fa:16:3e:28:73:93"
    }
}
"""
