# Copyright 2016 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
#
from __future__ import absolute_import

from BaseHTTPServer import HTTPServer
from threading import Thread
import logging
import signal

from keystone import TokenHandler
from neutron import NeutronHandler


def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info('Starting server')

    server_keystone = HTTPServer(('', 35357), TokenHandler)
    Thread(target=server_keystone.serve_forever).start()

    server_neutron = HTTPServer(('', 9696), NeutronHandler)
    Thread(target=server_neutron.serve_forever).start()

    print 'Press ctrl-c to exit'

    try:
        signal.pause()
    except KeyboardInterrupt:
        pass

    print 'Shutting down'

    server_keystone.shutdown()
    server_neutron.shutdown()



if __name__ == '__main__':
    main()
