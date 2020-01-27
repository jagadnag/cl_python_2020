#!/usr/bin/env python
import pprint
from napalm import get_network_driver

# Load driver and connection parameters
driver = get_network_driver('ios')
device = driver('198.18.1.55', 'cisco', 'cisco')

# Open connection to the end device and load config
device.open()
print('Napalm Is Running........\n')
device.load_merge_candidate(filename='new_loopback.cfg')
diffs = device.compare_config()

# Comapare configs to check whether any changes required
# If changes are required commit configs, if not do nothing
if len(diffs) > 0:
    print(diffs)
    print('Commiting changes...')
    device.commit_config()
    print('Done')
else:
    print('No changes needed')

device.close()