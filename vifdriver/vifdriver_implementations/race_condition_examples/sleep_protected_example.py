from vif_driver import VIFDriver
from empty_vif_driver import EmptyVifDriver
import os
import shutil
import time
import libvirt
import hooking
from subprocess import call
from vdsm.network.netinfo import DUMMY_BRIDGE

VNIC_ID_KEY = 'vnic_id'
PROVIDER_TYPE_KEY = 'provider_type'
EXTERNAL_NETWORK_PROVIDER_TYPE = 'EXTERNAL_NETWORK'
OPENSTACK_NETWORK_PROVIDER_TYPE = 'OPENSTACK_NETWORK'


class SleepProtectedVifDriver(EmptyVifDriver):

    def after_vm_start(self, environ, domxml):
        # check if the vm was launched in the paused state
        launch_flags = hooking.load_vm_launch_flags_from_file(environ['vmId'])
        if launch_flags == libvirt.VIR_DOMAIN_START_PAUSED:
            # sleep for a minute for each provisioned vm
            time.sleep(60)
            self.resume_paused_vm(environ)
        return domxml

    def before_nic_hotplug(self, environ, domxml):
        return self.attach_nic(environ, domxml)

    def before_device_create(self, environ, domxml):
        if not self.is_external_port(environ):
            return domxml

        domxml = self.attach_nic(environ, domxml)
        self.add_launch_paused_flag(environ)
        return domxml

    def attach_nic(self, environ, domxml):

        source_bridge = DUMMY_BRIDGE

        iface = domxml.getElementsByTagName('interface')[0]
        source = iface.getElementsByTagName('source')[0]
        bridge_name = source.setAttribute('bridge', source_bridge)
        return domxml

    def add_launch_paused_flag(self, environ):
        vm_id = environ['vmId']
        flags = hooking.load_vm_launch_flags_from_file(vm_id)
        flags |= libvirt.VIR_DOMAIN_START_PAUSED
        hooking.dump_vm_launch_flags_to_file(vm_id, flags)

    def resume_paused_vm(self, environ):
        call(['vdsClient', '-s', '0', 'continue', environ['vmId']])

    def is_external_port(self, environ):
        provider_type = environ.get(PROVIDER_TYPE_KEY, None)
        if not provider_type:
            return False
        return provider_type == EXTERNAL_NETWORK_PROVIDER_TYPE or \
            provider_type == OPENSTACK_NETWORK_PROVIDER_TYPE
