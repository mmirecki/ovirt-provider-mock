from neutron.base import ResponseBase


class UpdatePorts(ResponseBase):

    def path(self):
        return 'ports'

    def response(self, path):
        return """
{
    "port":
    {
        "status": "DOWN",
        "binding:host_id": "192.168.120.18-1ebb72",
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "device_owner": "oVirt",
        "binding:profile": {},
        "fixed_ips": [{
            "subnet_id": "dc594048-a9e2-4ec9-9928-4157cea7e530",
            "ip_address": "172.24.4.232"
        }],
        "id": "3c10bb5a-3d73-43a2-9c5a-9349d449e2a6",
        "security_groups": ["9cca3bc4-416c-4815-b3d7-4ee81ab8bb97"],
        "device_id": "7b2fa61c-2a88-424a-93b5-adc63328efe4",
        "name": "nic2",
        "admin_state_up": true,
        "network_id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
        "dns_name": "",
        "binding:vif_details": {},
        "binding:vnic_type": "normal",
        "binding:vif_type": "binding_failed",
        "tenant_id": "547deac3d7f64e2688de188365a139aa",
        "mac_address": "00:1a:4a:16:01:53"
    }
}
"""

"""
Input:

{
  "port" : {
    "name" : "nic2",
    "binding:host_id" : "192.168.120.18-1ebb72",
    "admin_state_up" : true,
    "device_id" : "7b2fa61c-2a88-424a-93b5-adc63328efe4",
    "device_owner" : "oVirt",
    "mac_address" : "00:1a:4a:16:01:53",
    "network_id" : "bf864bf3-81d8-438d-bf68-4b0c357309b3",
    "tenant_id" : "547deac3d7f64e2688de188365a139aa"
  }
}
"""
