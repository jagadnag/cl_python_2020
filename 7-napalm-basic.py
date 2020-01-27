#!/usr/bin/env python
from napalm import get_network_driver

# Load driver and connection parameters
driver = get_network_driver('ios')
device = driver('198.18.1.55', 'cisco', 'cisco')

# Open connection to the end device and print facts
device.open()
print('NAPALM is running........\n')
facts = device.get_facts()
print(facts)
device.close()