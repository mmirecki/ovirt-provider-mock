from vif_driver import VIFDriver
import shutil
from vdsm.network.netinfo import DUMMY_BRIDGE

VNIC_ID_KEY = 'vnic_id'
PROVIDER_TYPE_KEY = 'provider_type'
EXTERNAL_NETWORK_PROVIDER_TYPE = 'EXTERNAL_NETWORK'


class VdsmDummyVidDriver(VIFDriver):

    def after_device_destroy(self, environ, domxml):
        return domxml

    def after_device_create(self, environ, domxml):
        return domxml

    def after_network_setup(self, environ, json_content):
        return json_content

    def after_nic_hotplug(self, environ, domxml):
        return domxml

    def after_nic_unplug(self, environ, domxml):
        return domxml

    def after_get_caps(self, environ, json_content):
        return json_content

    def after_get_stats(self, environ, json_content):
        return json_content

    def after_vm_start(self, environ, domxml):
        return domxml

    def before_get_caps(self, environ, json_content):
        return json_content

    def before_get_stats(self, environ, json_content):
        return json_content

    def before_nic_hotplug(self, environ, domxml):
        return self.attach_nic(environ, domxml)

    def before_nic_unplug(self, environ, domxml):
        return domxml

    def before_device_create(self, environ, domxml):
        return self.attach_nic(environ, domxml)

    def before_device_destroy(self, environ, domxml):
        return domxml

    def before_migration_source(self, environ, domxml):
        return domxml

    def before_migration_destination(self, environ, domxml):
        return domxml

    def before_network_setup(self, environ, json_content):
        return json_content

    def before_vm_start(self, environ, domxml):
        return domxml

    def attach_nic(self, environ, domxml):
        provider_type = environ.get(PROVIDER_TYPE_KEY, None)
        if not provider_type or provider_type != EXTERNAL_NETWORK_PROVIDER_TYPE:
            return
        source_bridge = DUMMY_BRIDGE

        iface = domxml.getElementsByTagName('interface')[0]
        source = iface.getElementsByTagName('source')[0]
        bridge_name = source.setAttribute('bridge', source_bridge)
        return domxml
