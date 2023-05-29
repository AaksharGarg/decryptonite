# If the hash was cracked!
import hashlib
from itertools import product
import time


def Cracked(): # If the crack was successful!
    if (flag == 1):
        print("Successfully cracked the hash!")
        time.sleep(100000)
        
hash_to_be_cracked = input("Enter the hash to be cracked: ") # The md5 hash is to be cracked
user_input = input("Enter the string which you want to add while cracking hash: ") # The string through which we are going to going the generate the wordlist

min_size = int(input("Enter the minimum size of the encoded string: ")) # Minimum size of the wordlist to be produced
max_size = int(input("Enter the maximum size of the encoded string: ")) # Maximum size of the wordlist to be produced

flag = 0 # False by default!

for length in range(min_size,max_size+1): #Here min_size and max_size - Represents the length of the wordlist that we are going to generate
    to_attempt = product(user_input,repeat = length) # here user_input is the collection of the string from which we are going to make combination of the wordlist
    
    for x in to_attempt:
        key = ''.join(x)
        myhash = hashlib.md5(key.encode()).hexdigest()
        print("The hash = {}, Word = {}".format(myhash,key))    
        
        if (myhash == hash_to_be_cracked):
            flag = 1
            print("Cracked the hash successfully!")
            Cracked()

# If the crack wasn't successful!
if (flag == 0):
    print("Sorry we were not able to crack the hash!")
    print("Please try again!")

time.sleep(10000)