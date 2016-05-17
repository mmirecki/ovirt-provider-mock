#!/usr/bin/python

import hooking
import os
import sys
sys.path.append("/usr/libexec/vdsm/hooks/vifdriver")
import vif_driver_hooking

reply = vif_driver_hooking.before_get_caps(os.environ, hooking.read_json())
if reply:
    hooking.write_json(reply)
hooking.exit_hook("", return_code=0)
