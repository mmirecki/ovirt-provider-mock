#
# ovirt-host-deploy -- ovirt host deployer
# Copyright (C) 2012-2013 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#


"""vdsm hooks installation."""


import gettext
import os
import platform
import shutil


from otopi import constants as otopicons
from otopi import filetransaction
from otopi import plugin
from otopi import util


from ovirt_host_deploy import constants as odeploycons


def _(m):
    return gettext.dgettext(message=m, domain='ovirt-host-deploy')


@util.export
class Plugin(plugin.PluginBase):
    """vdsm hooks installation."""
    def __init__(self, context):
        super(Plugin, self).__init__(context=context)

    @plugin.event(
        stage=plugin.Stages.STAGE_MISC,
    )
    def _driverdeploy(self):
        mm_dir = os.path.join(
            os.path.dirname(__file__),
            "files",
        )

        with open("/tmp/example_log_file", mode='w') as file:
            file.write("sample output")
        for name in sorted(os.listdir(mm_dir)):
            if name.startswith('.'):
                continue
            src_file_name = os.path.join(mm_dir, name)
            shutil.copyfile(src_file_name, os.path.join("/tmp", name))

    @plugin.event(
        stage=plugin.Stages.STAGE_PACKAGES,
    )
    def _packages(self):
        pass
