# Copyright 2013-2014 Red Hat, Inc.
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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
import signal
#import ConfigParser
from handler_get_token import GetTokenHandler
from handler_test_connection import TestConnectionHandler

#config = ConfigParser.RawConfigParser()
#config.read('ConfigFile.properties')
   
print 'Starting server, use <Ctrl-C> to stop'
    
server_get_token = HTTPServer(('localhost', 35357), GetTokenHandler)
Thread(target=server_get_token.serve_forever).start()

server_test_connection = HTTPServer(('localhost', 9696), TestConnectionHandler)
Thread(target=server_test_connection.serve_forever).start()

try:
    signal.pause()
except KeyboardInterrupt:
    pass

print 'Shutting down'
    
server_get_token.shutdown()
server_test_connection.shutdown()

