#!/usr/bin/env python
import pprint
from napalm import get_network_driver

# Load driver and connection parameters
driver = get_network_driver('ios')
device = driver('198.18.1.55', 'cisco', 'cisco')
device.open()
print('Napalm Is Running........\n')

# Rollback the previous config changes
device.rollback()

# Collect facts and print the device details
pp = pprint.PrettyPrinter(indent=4)
facts = device.get_facts()
pp.pprint(facts['interface_list'])

device.close()