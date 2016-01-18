from neutron.base import ResponseBase


class ListPorts(ResponseBase):

    def path(self):
        return 'ports'

    """
    identified in ovirt by: device_id
    Check how port is created in update_ports.py
    """

    def response(self, path):
        return """
{"ports":
 [
   {
    "status": "DOWN",
    "binding:host_id": "192.168.120.18-1ebb72",
    "allowed_address_pairs": [],
    "extra_dhcp_opts": [],
    "dns_assignment": [
       {
        "hostname": "host-172-24-4-227",
        "ip_address": "172.24.4.227",
        "fqdn": "host-172-24-4-227.openstacklocal."
       }
       ],
    "device_owner": "oVirt",
    "binding:profile": {},
    "fixed_ips": [
       {
        "subnet_id": "dc594048-a9e2-4ec9-9928-4157cea7e530",
        "ip_address": "172.24.4.227"
       }],
    "id": "49ccb785-eadb-469d-8c33-e7bc87d37e4e",
    "security_groups": ["9cca3bc4-416c-4815-b3d7-4ee81ab8bb97"],
    "device_id": "5cc10431-0b25-41bd-941c-3a1aed8edd87",
    "name": "nic5",
    "admin_state_up": true,
    "network_id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
    "dns_name": "",
    "binding:vif_details": {},
    "binding:vnic_type": "normal",
    "binding:vif_type": "binding_failed",
    "tenant_id": "547deac3d7f64e2688de188365a139aa",
    "mac_address": "00:1a:4a:16:01:59"
  }]
}
"""
