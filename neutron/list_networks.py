from neutron.base import ResponseBase


class ListNetworks(ResponseBase):

    def path(self):
        return 'networks'

    def response(self, path):
        return """
{
    "networks": [
        {
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
        },
        {
            "status": "ACTIVE",
            "subnets": ["6ed90628-5d9c-4eae-8665-0b2420e683d4"],
            "name": "private",
            "provider:physical_network": null,
            "admin_state_up": true,
            "tenant_id": "472beee27f704a5b8a6f3a15fdac7ba5",
            "mtu": 0,
            "router:external": false,
            "shared": false,
            "provider:network_type": "vxlan",
            "id": "59b48a4c-893c-47d2-9df3-84102329bbb9",
            "provider:segmentation_id": 56
        }
    ]
}
"""
