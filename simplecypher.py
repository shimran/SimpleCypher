''' Simple Cypher Program

Read me for more details, but goal is to take a message and encrypt/decrypt based on a shift from the alphabet
'''


#Add Dependencies

import sys,math, string

#Define main
def main():

#Add alphabet for the Cypher shift
#Will need to add a upper() function to induce case-sensitivity
alphabetList= list(string.ascii_uppercase)
shiftKey= input("Add Key for shift (must be 26 letters):")
message = input("Enter phrase to be encrypted: ")
flag = input("Do you want to set the ENCRYPT (E) or DECRYPT (D)?:")

if (flag.upper() =='E')
	encryptString(message, shiftKey)
elif (flag.upper() == 'D')
	decryptString(message, shiftKey)
else
	print ("Invalid option selected")
	


#Check if shift Key is valid, sort to see if list is the same length
def checkValidShiftKey(shiftKey,alphabetList):
	keySort= list(shiftKey).upper()
	if len(alphabetList) != len(keySort)
	'The key you have provided is invalid. Check length or if a letter not part of the alphabet'
	sys.exit('The key you have provided is invalid. Check length or if a letter not part of the alphabet')


#Function for encryption

def encryptString():


#Function for decryption

def decryptString():
#Allows function to be imported as module
if __name__ == '__main__':
main()


	
