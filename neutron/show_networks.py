from neutron.base import ResponseBase


class ShowNetworks(ResponseBase):

    def path(self):
        return 'networks/'

    def response(self, path):
        return """
{
    "network": {
            "status": "ACTIVE",
            "subnets": ["dc594048-a9e2-4ec9-9928-4157cea7e530"],
            "name": "public",
            "provider:physical_network": null,
            "admin_state_up": true,
            "tenant_id": "547deac3d7f64e2688de188365a139aa",
            "mtu": 0,
            "router:external": true,
            "shared": false,
            "provider:network_type": "vxlan",
            "id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
            "provider:segmentation_id": 35
        }
}
"""
