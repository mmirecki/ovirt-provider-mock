from vif_driver_config import vif_driver


def after_get_caps(environ, json_content):
    return vif_driver.after_get_caps(environ, json_content)


def after_get_stats(environ, json_content):
    return vif_driver.after_get_stats(environ, json_content)


def before_device_create(environ, domxml):
    return vif_driver.before_device_create(environ, domxml)


def before_device_destroy(environ, domxml):
    return vif_driver.before_device_destroy(environ, domxml)


def before_nic_hotplug(environ, domxml):
    return vif_driver.before_nic_hotplug(environ, domxml)


def before_nic_unplug(environ, domxml):
    return vif_driver.before_nic_unplug(environ, domxml)


def before_migration_source(environ, domxml):
    return vif_driver.before_migration_source(environ, domxml)


def before_migration_destination(environ, domxml):
    return vif_driver.before_migration_destination(environ, domxml)


def before_network_setup(environ, json_content):
    return vif_driver.before_network_setup(environ, json_content)
