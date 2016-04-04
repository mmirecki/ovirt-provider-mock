from vif_driver import VIFDriver
import shutil


class InputDumpDriver(object):

    def after_get_caps(self, environ, json_content):
        shutil.copyfile(environ['_hook_json'], '/tmp/after_get_caps')

    def after_get_stats(self, environ, json_content):
        shutil.copyfile(environ['_hook_json'], '/tmp/after_get_stats')

    def before_nic_hotplug(self, environ, domxml):
        shutil.copyfile(environ['_hook_domxml'], '/tmp/before_nic_hotplug')

    def before_nic_unplug(self, environ, domxml):
        shutil.copyfile(environ['_hook_domxml'], '/tmp/before_nic_unplug')

    def before_migration_source(self, environ, domxml):
        shutil.copyfile(environ['_hook_domxml'], '/tmp/before_migration_source')

    def before_migration_destination(self, environ, domxml):
        shutil.copyfile(environ['_hook_domxml'], '/tmp/before_migration_destination')

    def before_network_setup(self, environ, json_content):
        shutil.copyfile(environ['_hook_json'], '/tmp/before_network_setup')
