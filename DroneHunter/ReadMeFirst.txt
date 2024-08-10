how to use it ? 
sudo python3 dronehunter.py          

       
         _____                       _    _             _            
 |  __ \                     | |  | |           | |           
 | |  | |_ __ ___  _ __   ___| |__| |_   _ _ __ | |_ ___ _ __ 
 | |  | | '__/ _ \| '_ \ / _ \  __  | | | | '_ \| __/ _ \ '__|
 | |__| | | | (_) | | | |  __/ |  | | |_| | | | | ||  __/ |   
 |_____/|_|  \___/|_| |_|\___|_|  |_|\__,_|_| |_|\__\___|_|   
                                                              
                                                              
        
        
DroneHunter Framework - Drone Exploitation Toolkit

DroneHunter > help
Commands: search <query>, use <index|name>, show options, set <option> <value>, exploit
DroneHunter > search att
Matching Modules
================
0  Attitude Spoofing  Attacks drone's attitude control
DroneHunter > use 0
Using module: Attitude Spoofing
DroneHunter > show options
target (Required: True):  - The target IP address
port (Required: True): 14550 - The target port
DroneHunter > set target 192.1.3.4
Set target to 192.1.3.4
DroneHunter > exploit
Debug: Retrieved target IP is '1'
Debug: Retrieved target port is '14550'
Invalid target IP: 1
DroneHunter > set port 8000
Set port to 8000
DroneHunter > exploit
Debug: Retrieved target IP is '1'
Debug: Retrieved target port is '8'
Invalid target IP: 1
# As you you can see the problem is with how target_ip and target_port are being retrieved and processed
