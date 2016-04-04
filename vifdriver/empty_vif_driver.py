from vif_driver import VIFDriver


class DefaultVifDriver(VIFDriver):

    def after_get_caps(self):
        pass

    def after_get_stats(self, path):
        pass

    def before_nic_hotplug(self, path):
        pass

    def before_nic_unplug(self, path):
        pass

    def before_device_create(self, environ, domxml):
        pass

    def before_device_destroy(self, environ, domxml):
        pass

    def before_migration_source(self, path):
        pass

    def before_migration_destination(self, path):
        pass

    def before_network_setup(self, path):
        pass
