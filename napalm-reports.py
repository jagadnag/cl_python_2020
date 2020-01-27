#!/usr/bin/env python
import pprint
from napalm import get_network_driver
from prettytable import PrettyTable

# List of devices to collect facts
device_ip = ['198.18.1.55', '198.18.1.56']

# Using prettytable to print a sample report
report = PrettyTable(['Hostname', 'Vendor', 'Model', 'Serial No.'])

# Loop through device_ip list and collect facts
for ip in device_ip:
    driver = get_network_driver('ios')
    device = driver(ip, 'cisco', 'cisco')
    device.open()
    print('NAPALM is running on ' + ip + '........\n')
    facts = device.get_facts()
    report.add_row([facts['hostname'], facts['vendor'], facts['model'], facts['serial_number']])
    device.close()

# Print final report
print (report)