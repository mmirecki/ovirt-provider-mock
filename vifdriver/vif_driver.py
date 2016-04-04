from abc import abstractmethod


class VIFDriver(object):

    @abstractmethod
    def after_get_caps(self, environ, json_content):
        return json_content

    @abstractmethod
    def after_get_stats(self, environ, json_content):
        return json_content

    @abstractmethod
    def before_nic_hotplug(self, environ, domxml):
        return domxml

    @abstractmethod
    def before_nic_unplug(self, environ, domxml):
        return domxml

    @abstractmethod
    def before_device_create(self, environ, domxml):
        return domxml

    @abstractmethod
    def before_device_destroy(self, environ, domxml):
        return domxml

    @abstractmethod
    def before_migration_source(self, environ, domxml):
        return domxml

    @abstractmethod
    def before_migration_destination(self, environ, domxml):
        return domxml

    @abstractmethod
    def before_network_setup(self, environ, json_content):
        return json_content
