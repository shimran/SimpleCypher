/* Simple Cypher Program

Read me for more details, but goal is to take a message and encrypt/decrypt based on a shift from the alphabet

*/


#Add Dependencies

import sys, math

#Add akphabet for the Cypher shift
#Will need to add a lower() function to induce case-sensitivity
Alphabet_Key= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = input("Enter phrase to be encrypted: ")
flag = input("Do you want to set the ENCRYPT (E) or DECRYPT (D)?")

