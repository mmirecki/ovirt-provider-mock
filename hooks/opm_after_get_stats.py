#!/usr/bin/env python
import hooking
import json
import time

# If the interface is an existing device, the statistics will be present in the hook input data
# An example for a device called "public"
stats = hooking.read_json()

# If the statistics for the device are to be appended manually
# An example for device "test"
custom_stats = {
    "ens17": {
        "sampleTime": time.time(),
        "rxDropped": "0",
        "tx": "0",
        "rxErrors": "0",
        "rx": "0",
        "txDropped": "0",
        "txRate": "0.0",
        "rxRate": "0.0",
        "txErrors": "0",
        "state": "down",
        "speed": "100",
        "name": "ens17"
    }}

stats['network'].update(custom_stats)

hooking.write_json(stats)
