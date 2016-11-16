''' Simple Cypher Program

Read me for more details, but goal is to take a message and encrypt/decrypt based on a shift from the alphabet
'''


#Add Dependencies

import sys,math, string

#Add akphabet for the Cypher shift
#Will need to add a upper() function to induce case-sensitivity
alphabetList= list(string.ascii_uppercase)
shiftKey= input("Add Key for shift (must be 26 letters):")
message = input("Enter phrase to be encrypted: ")
flag = input("Do you want to set the ENCRYPT (E) or DECRYPT (D)?:")

#Check if shift Key is valid, sort to see if list is the same length
def checkValidShiftKey(shiftKey,alphabetList):
	keySort= list(shiftKey).upper()
	if len(alphabetList) != len(keySort)
	'The key you have provided is invalid. Check length or if a letter not part of the alphabet'
	sys.exit('The key you have provided is invalid. Check length or if a letter not part of the alphabet')

	
