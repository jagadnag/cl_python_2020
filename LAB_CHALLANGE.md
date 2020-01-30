## User Lab Tasks

Note: Don't save the scripts with the filename 'netmiko.py' or 'napalm.py', Use a diffrent name. These are module names that will be used to write the script. If the script name and module name are the same, the scripts will not excute correctly.

### Task 1: Create a simple Netmiko script

#### Import the Netmiko module

```py
from xxxxx import xxxxxx
```

#### Create a dictionary representing the device connection parameters

```py
cisco_router = {
    'device_type': 'xxxxxx', # provide the device type
    'host': 'x.x.x.x',       # fill the ip address of the device
    'username': 'xxxxx',     # provide the username
    'password': 'xxxxx',     # prodide the password
}
```

#### Establish an SSH connection to the device by passing in the device dictionary.

```py
net_connect = ConnectHandler(**xxxxxx) # reference the dictionary connected above
```

#### Execute a show command.

```py
output = net_connect.send_command('xxxxxx')
```
#### Print the output
```py
print(xxxxx)
```

### Task 2: Write a python script to make a config change

#### Copy paste the previosuly written script and rename it

#### Edit the .send_command() to .send_config_set()

```py
output = net_connect.send_config_set('xxxxxxx)
```
#### Print the output
```py
print(xxxxx)
```
