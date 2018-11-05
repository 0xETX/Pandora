#Made by GlobalPandemic

import re

#Methods
#Website Search
def DotSearch(fileReadString):
	text = re.findall(r"[w0-9]{0,4}[\.]{0,1}[\w0-9\.]{1,}[\.][A-Za-z0-9]{1,}", fileReadString)
	text = "\n".join(text)
	return text
	
def RegSearch(fileReadString):
	text = re.findall(r"HKEY[A-Za-z0-9_\\]*", fileReadString)
	text = "\n".join(text)
	return text

#patorjk.com - 'sweet' font
print('''
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
     ___                                                               
    (   )                                                              
  .-.| |   ___ .-.      .--.     .---.   ___ .-. .-.                   
 /   \ |  (   )   \    /    \   / .-, \ (   )   '   \                  
|  .-. |   | ' .-. ;  |  .-. ; (__) ; |  |  .-.  .-. ;                 
| |  | |   |  / (___) |  | | |   .'`  |  | |  | |  | |                 
| |  | |   | |        |  |/  |  / .'| |  | |  | |  | |                 
| |  | |   | |        |  ' _.' | /  | |  | |  | |  | |                 
| '  | |   | |        |  .'.-. ; |  ; |  | |  | |  | |                 
' `-'  /   | |        '  `-' / ' `-'  |  | |  | |  | |                 
 `.__,'   (___)        `.__.'  `.__.'_. (___)(___)(___)                
                                                                       
                                                                       
                    ___                 ___                            
                   (   )               (   )                           
  .--.      .---.   | |_       .--.     | | .-.     .--.    ___ .-.    
 /    \    / .-, \ (   __)    /    \    | |/   \   /    \  (   )   \   
|  .-. ;  (__) ; |  | |      |  .-. ;   |  .-. .  |  .-. ;  | ' .-. ;  
|  |(___)   .'`  |  | | ___  |  |(___)  | |  | |  |  | | |  |  / (___) 
|  |       / .'| |  | |(   ) |  |       | |  | |  |  |/  |  | |        
|  | ___  | /  | |  | | | |  |  | ___   | |  | |  |  ' _.'  | |        
|  '(   ) ; |  ; |  | ' | |  |  '(   )  | |  | |  |  .'.-.  | |        
'  `-' |  ' `-'  |  ' `-' ;  '  `-' |   | |  | |  '  `-' /  | |        
 `.__,'   `.__.'_.   `.__.    `.__,'   (___)(___)  `.__.'  (___)   
 
~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
 ''')

#Taking in the input for file directories
filePathRead = input("Enter the path of the SEARCH TO file, including desired filename and extension.\n")
filePathAppend = input("\nEnter the path of the OUTPUT TO file, including desired filename and extension.\n")

#Excepts errors when opening files
try:
	fileRead = open(filePathRead, "r", errors="ignore")
	fileAppend = open(filePathAppend, "a")
except:
	print("An error occured! Make sure you typed your filename/directory correctly the program has sufficient privilleges.")
	exit()

fileReadString = fileRead.read()

#Method finder - takes user's input and activates each method
userInput = input("Options:\n-dot: Find links, files, ips, etc.\n-reg: Find registry keys\nYou can select up to multiple options.\n")
if("dot" in userInput):
	print("\nSearching 'dot'...")
	fileAppend.write("===DOT===\n")
	fileAppend.write(DotSearch(fileReadString)+"\n")
if("reg" in userInput):
	print("\nSearching 'reg'...")
	fileAppend.write("\n===REG===\n")
	fileAppend.write(RegSearch(fileReadString)+"\n")

print("\nSearches completed! Exiting program...")
fileRead.close()
fileAppend.close()
