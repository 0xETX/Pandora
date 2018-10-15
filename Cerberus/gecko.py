#								CAESER CIPHER ENCRYPTING
#The code below takes a string and uses the Caeser Cipher to encrypt it
def caeser_encrypt (crypto):
	letter_unicode = [ord(single_letter) for single_letter in user_input]
	converted_letter = [e + 1 for e in letter_unicode]
	number_back_letter = [chr(c) for c in converted_letter]
	for number_back_letter in number_back_letter:
		print(number_back_letter, end = ' ', flush = True)
	return;
#
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#								CAESER CIPHER DECRYPTING
#The code below takes an encrypted string and uses the reverse Caeser Cipher to reverse
def caeser_decrypt (crypto):
	letter_unicode = [ord(single_letter) for single_letter in user_input]
	converted_letter = [ e - 1 for e in letter_unicode]
	number_back_letter = [chr(c) for c in converted_letter]
	for number_back_letter in number_back_letter:
		print(number_back_letter, end = ' ', flush = True)
	return;
#
#--------------------------------------------------------------------------------------
#EXTRA TIME FOR CAESER?
#remove spaces, check for both upper and lower case and adjust, adjust for ends with z
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#								HASHING USING SHA-256
#
def secure_hash (crypto):
	hash_object = hashlib.sha256(user_input.encode('utf-8'))
	#hex_dig = hash_object.hexidigest()
	print(hash_object.hexdigest())
	#hex_dig is supposed to be in print
#does it need to be put into a for loop to be able going through each letter and then convert?
	
	
print("							WELCOME TO CERBERUS")

#!!!SLIDE NUMBER 27 IN MODULE 5 CAN SOLVE THE ISSUE BELOW!!!

user_selection = eval(input("Please select if you would like to encrypt [0] decrypt [1] or hashed with SHA-256 [2]:"))

if user_selection == 0:
	user_input = str(input("Please enter a phrase you would like to have encrypted:"))
	caeser_encrypt(user_input)
elif user_selection == 1:
	user_input = str(input("Please enter a phrase you would like to have decrypted:"))
	caeser_decrypt(user_input)
elif user_selection == 2:
	user_input = str(input("Please enter a phrase you would like to have hashed with SHA-256:"))
	secure_hash(user_input)
else:
	print("")
print("Please select a number off the menu")
#need to have restart

#--------------------------------------------------------------------------------------
#								TESTING AREA DOWN HERE
