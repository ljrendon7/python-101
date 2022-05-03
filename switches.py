import netmiko
import getpass
from netmiko import ConnectHandler
import os



switch = {
    'device_type': 'cisco_ios',
    'ip': '',
    'username': '',
    'password': '',
    'secret': '4yourswitch',
}

ip = input("\nPlease enter the IP of the switch (X.X.X.X) or domain name (XXXSW01): ")
ping = input("\nPlease select a destination IP to test your ping: ")
traceroute = input("\nPlease enter IP to Traceroute: ")
username = input("\nPlease enter your username admin.xxxx:")
password = getpass.getpass(prompt="\nPlease enter your password:")
switch['ip'] = ip
switch['username'] = username
switch['password'] = password


#connecting to switch
net_connect =ConnectHandler(**switch)
#going to enable mode
net_connect.enable()
#sending a command and getting the output

#commands()

file = open('output.txt', 'w')
    
file.write('***SHOW INTERFACE STATUS***\n')
output =net_connect.send_command('show interface status')
file.write(output)
    
file.write("\n\n***SHOW SPANNING-TREE SUMMARY***\n")
output1 =net_connect.send_command('show spanning-tree summary')
file.write(output1)
    
file.write("\n\n***SHOW ENVIRONMENT STACK***\n")
output2 =net_connect.send_command('show environment status')
file.write(output2)
    
file.write("\n\n***SHOW ENVIRONMENT ALL***\n")
output3 =net_connect.send_command('show environment all')
file.write(output3)
    
file.write("\n\n***SHOW VERSION***\n")
output4 =net_connect.send_command('show version')
file.write(output4)
    
file.write("\n\n***SHOW  SWITCH***\n")
output5 =net_connect.send_command('show switch')
file.write(output5)
    
file.write("\n\n***SHOW PROCESS CPU HISTORY***\n")
output6 =net_connect.send_command('show process cpu history')
file.write(output6)
    
file.write("\n\n***PING SOURCE VLAN 100***\n")
output7 =net_connect.send_command(f"ping {ping} source vlan 100")
file.write(output7)
    
file.write("\n\n***PING SOURCE VLAN 200***\n")
output8 =net_connect.send_command(f"ping {ping} source vlan 200")
file.write(output8)
    
file.write("\n\n***PING SOURCE VLAN 300***\n")
output9 =net_connect.send_command(f"ping {ping} source vlan 300")
file.write(output9)
    
file.write("\n\n***PING SOURCE VLAN 400***\n")
output10 =net_connect.send_command(f"ping {ping} source vlan 400")
file.write(output10)
    
file.write("\n\n***PING SOURCE VLAN 500***\n")
output11 =net_connect.send_command(f"ping {ping} source vlan 500")
file.write(output11)

'''
file.write("\n\n***TRACEROUTE***\n")
output12 =net_connect.send_command(f"traceroute {traceroute}")
file.write(output12)
'''
os.startfile('C:\\Users\\luis.rendon\\Documents\\Python\\Networking Tools\\output.txt')
























































