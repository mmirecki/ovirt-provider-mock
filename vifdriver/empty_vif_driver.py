from vif_driver import VIFDriver


class EmptyVifDriver(VIFDriver):

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

    def after_migration_source(self, environ, domxml):
        return domxml

    def after_migration_destination(self, environ, domxml):
        return domxml

    def before_get_caps(self, environ, json_content):
        return json_content

    def before_get_stats(self, environ, json_content):
        return json_content

    def before_nic_hotplug(self, environ, domxml):
        return domxml

    def before_nic_unplug(self, environ, domxml):
        return domxml

    def before_device_create(self, environ, domxml):
        return domxml

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
