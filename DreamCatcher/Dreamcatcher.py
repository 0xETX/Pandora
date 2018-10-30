import re

#Methods
#Website Search
def WebSearch(fileReadString):
	text = re.findall(r"[w0-9]{0,4}[\.]{0,1}[\w0-9\.]{1,}[\.][A-Za-z0-9]{1,}", fileReadString)
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

filePathRead = input("Enter the path of the SEARCH TO file, including desired filename and extension.\n")
filePathAppend = input("\nEnter the path of the OUTPUT TO file, including desired filename and extension.\n")
try:
	fileRead = open(filePathRead, "r", errors="ignore")
	fileAppend = open(filePathAppend, "a")
except:
	print("An error occured! Make sure you typed your filename correctly the program has sufficient privilleges.")
	exit()

fileReadString = fileRead.read()
 
userInput = input("Options:\n-dot: Find links, files, ips, etc.\nYou can select up to multiple options.\n")
if("dot" in userInput):
	fileAppend.write("===WEBSITES===\n")
	fileAppend.write(WebSearch(fileReadString)+"\n")

fileRead.close()
fileAppend.close()
