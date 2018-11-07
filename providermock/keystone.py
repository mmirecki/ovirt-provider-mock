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

from BaseHTTPServer import BaseHTTPRequestHandler
import logging


# TODO: any token to make engine happy
response_string = """{"access":{"token":{
    "id": "00000000000000000000000000000001"} }}"""


# TODO: authentication to be implemented
# This is just a placeholder
class TokenHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        logging.debug('Request: {} : {}'.format('POST', self.path))
        logging.debug(self.headers)
        content = self._get_content()
        if content:
            logging.debug('Request body:\n{}'.format(content))

        response_code = 200
        logging.debug('Response code: {}'.format(response_code))
        logging.debug('Response body: {}'.format(response_string))

        self.send_response(200)
        self.send_header('Content-Type', 'Application/json')
        self.end_headers()
        self.wfile.write(response_string)

    def _get_content(self):
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length)
        return content
