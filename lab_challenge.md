## User Lab Tasks

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
print(output)
```
