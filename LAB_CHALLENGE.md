## User Lab Tasks

In the following lab challenge tasks, you are requested to create few python scripts to get yourself familiar with writing and executing the scripts.

In the VS Code, Click on File menu and Select 'New File' option. An 'Untitled' page will open on editor window to write new scripts.

### Task 1: Create hello.py script

Open a new file and type in 

```py
print('hello world')
```

Save it as hello.py and run the script from the VS code terminal window.

Note: Ensure you are in the right folder path.

### Task 2: Create a simple Netmiko script

#### Import the Netmiko module

```py
from xxxxx import xxxxxx
```

#### Create a dictionary representing the device connection parameters

```py
cisco_device = {
    'device_type': 'xxxxxx', # provide the device type
    'host': 'x.x.x.x',       # fill the ip address of the device
    'username': 'xxxxx',     # provide the username
    'password': 'xxxxx',     # provide the password
}
```

#### Establish an SSH connection to the device by passing in the device dictionary

```py
net_connect = ConnectHandler(**xxxxxx) # reference the dictionary mentioned above
```

#### Call the netmiko function .send_commnd() that will to execute the show command

```py
output = net_connect.send_command('xxxxxx')
```
#### Print the output
```py
print(xxxxx)
```
#### Now save the script with 'xxxxxx'.py
Note: Don't save the scripts with the filename 'netmiko.py' or 'napalm.py', Use a different name. These are module names that will be inside the scripts. If the script name and module name are the same, the scripts will not execute correctly.

#### Run the script from the VS Code terminal window
```
python xxxxx.py
```
Verifiy the printed output

### Task 3: Write a python script to make a config change

#### Copy paste the previously written script and rename it

#### Call the netmiko .send_config_set() function that will configure the device

```py
output = net_connect.send_config_set('xxxxxxx')
```
#### Print the output
```py
print(xxxxx)
```
#### Now save the script with 'xxxxxx'.py

#### Run the script from the VS Code terminal window
```
python xxxxx.py
```
Verify the printed output
