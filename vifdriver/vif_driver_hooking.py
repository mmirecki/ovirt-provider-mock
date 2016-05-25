from vif_driver_config import vif_driver


def after_get_caps(environ, json_content):
    return vif_driver.after_get_caps(environ, json_content)


def after_get_stats(environ, json_content):
    return vif_driver.after_get_stats(environ, json_content)


def after_device_create(environ, domxml):
    return vif_driver.after_device_create(environ, domxml)


def after_device_destroy(environ, domxml):
    return vif_driver.after_device_destroy(environ, domxml)


def after_nic_hotplug(environ, domxml):
    return vif_driver.after_nic_hotplug(environ, domxml)


def after_nic_unplug(environ, domxml):
    return vif_driver.after_nic_unplug(environ, domxml)


def after_migration_source(environ, domxml):
    return vif_driver.after_migration_source(environ, domxml)


def after_migration_destination(environ, domxml):
    return vif_driver.after_migration_destination(environ, domxml)


def after_network_setup(environ, json_content):
    return vif_driver.after_network_setup(environ, json_content)


def after_vm_start(environ, json_content):
    return vif_driver.after_vm_start(environ, json_content)


def before_get_caps(environ, json_content):
    return vif_driver.before_get_caps(environ, json_content)


def before_get_stats(environ, json_content):
    return vif_driver.before_get_stats(environ, json_content)


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


def before_vm_start(environ, json_content):
    return vif_driver.before_vm_start(environ, json_content)
