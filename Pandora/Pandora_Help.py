#Made by GlobalPandemic
#This script is intended to be the main front of Pandora.
#Subject to change.

#This method is used for \Help.
#Contains details on each program.
#Please update regularly.
def Help(progChoice):
	#PR_Alpha Description
	if("1" in progChoice):
		print('''
________________     _____________       ______         
___  __ \__  __ \    ___    |__  /__________  /_______ _
__  /_/ /_  /_/ /    __  /| |_  /___  __ \_  __ \  __ `/
_  ____/_  _, _/     _  ___ |  / __  /_/ /  / / / /_/ / 
/_/     /_/ |_|______/_/  |_/_/  _  .___//_/ /_/\__,_/  
			_/_____/           /_/                    
======================USER GUIDE======================

=====DESCRIPTION=====
PR_Alpha is a Python command line port scanner and IP sweeper program.
By scanning ports, PR_Alpha can determine if the said port is closed or open.
By scanning IP addresses, PR_Alpha can determine what hosts are online.

=====USEAGE=====
When prompted with "Which mode would you like to select", you must input the number on the same line as the action.
Currently, there are three modes:
1 - Port Specific
2 - Port Range
3 - Ping Sweep

=====PORT SPECIFIC=====
Port specific will prompt you to enter the IP address of the device you wish to scan.
Enter a port number and press enter to add your port. Add another port on the new line provided after entering the
previous port.
Use a number below 1 or above 65535 to start scanning.

=====PORT RANGE=====
Port range will prompt you for an IP address.
Once you've enter the IP, it will prompt you for your first port. This is where the scan begins at.
After you've entered the first port, it will ask you for the port it will end at.
Everything between (including the start and end ports) will be scanned.

=====IP SWEEP=====
When asked for the three IP numbers, insert the first three numbers such as 194.55.32 in 194.55.32.45
The program will start at ###.###.###.1 and end at ###.###.###.255.
It will display each host it recieved a response back from at the end.
This program uses Window's batch, so this feature currently only works with Windows computers - not compatible with Mac, *NIX and other OSes.
		''')
		wait = input("\nPress enter to exit the help menu.")
		return
	
#Loop for program choice
while True:
	progChoice = input("\nPlease select an option using ONLY the number provided.\n1 - PR_Alpha\n2 - Cerberus\n3 - Gecko\nUse \\help with the number for info and useage on program (i.e. \help 1).\n")
	if(progChoice == 1):
		#Go to PR_Alpha method
		print()
	elif(progChoice == 2):
		#Go to Cerberus method
		print()
	elif(progChoice == 3):
		#Go to Gecko method
		print()
	elif("\help" in progChoice):
		Help(progChoice)
