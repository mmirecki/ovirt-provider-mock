from vif_driver import VIFDriver
import os
import shutil
import time
import libvirt
import hooking
from subprocess import call
from vdsm.network.netinfo import DUMMY_BRIDGE
from neutronclient.v2_0 import client

VNIC_ID_KEY = 'vnic_id'
PROVIDER_TYPE_KEY = 'provider_type'
EXTERNAL_NETWORK_PROVIDER_TYPE = 'EXTERNAL_NETWORK'


class ProtectedVdsmDummyVidDriver(VIFDriver):

    def after_device_destroy(self, environ, domxml):
        return domxml

    def after_device_create(self, environ, domxml):
        self.resume_paused_vm(environ)

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
        vm_id = environ['vmId']
        launch_flags = hooking.load_vm_launch_flags_from_file(vm_id)
        if launch_flags == libvirt.VIR_DOMAIN_START_PAUSED:
            self.resume_paused_vm(environ)
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
        result = self.attach_nic(environ, domxml)
        self.add_launch_paused_flag(environ)
        return result

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

    def add_launch_paused_flag(self, environ):
        vm_id = environ['vmId']

        flag_file_dir = "/var/run/vdsm/hook/" + vm_id
        flag_file_name = flag_file_dir + "/launchflags"

        try:
            os.stat(flag_file_dir)
        except:
            os.makedirs(flag_file_dir)

        with open(flag_file_name, mode='w') as file:
            file.write(str(libvirt.VIR_DOMAIN_START_PAUSED))

    def resume_paused_vm(self, environ):
        provider_type = environ.get(PROVIDER_TYPE_KEY, None)
        if not provider_type or provider_type != EXTERNAL_NETWORK_PROVIDER_TYPE:
            return
        # Wait for some time until the nic is connected.
        # This can be replaced by an implicit check if the nic is UP
        time.sleep(15)
        call(['vdsClient', '-s', '0', 'continue',
              environ['vmId']])

    def is_openstack_port_down(self, environ):

        vnic_id = environ['vnic_id']
        credentials = self.get_openstack_credentials()
        neutron = client.Client(**credentials)
        try:
            port = neutron.show_port(vnic_id)
            port_status = port['port']['status']
            return port_status == "DOWN"
        except:
            return False

    def get_openstack_credentials(self):
        credentials = {}
        credentials['username'] = 'admin'
        credentials['password'] = 'f0d910204e194de7'
        credentials['auth_url'] = 'http://192.168.120.151:5000/v2.0'
        credentials['tenant_name'] = 'admin'
        return credentials
