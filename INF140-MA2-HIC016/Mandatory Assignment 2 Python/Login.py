# By Steffen Rivedal Eimhjellen for Assignment 2
# Question 1

import hashlib                                      # using hashlib so that we can hash the password

inputusername = input("Please provide your username: ")
inputpassword = input("Please provide your password: ").encode() # so that we can give the text a hash value

inputpassword = (hashlib.sha512(inputpassword).hexdigest()) # hashing the text with sha512, if the hashed password later is equal to shadow.txt password then we have that our password is correct.

f = open("shadow.txt", "r")         #opening shadow.txt file
access = ""

for line in f:                      # making a for loop that goes through every line in the shadow.txt file.
    if inputusername in line:                       #if the username is in the line then we go further
        if inputpassword in line:                              # if the password is also in the line then access = our text and finish the loop
            access = ("You're Successfully logged in!")
            break
        else:                                                   #if the password is not correct access = this
            access = ("Obs! The provided username and password do not match.")
    else:                                                        # if the username is not correct access = this
        access = ("Obs! The provided username and password do not match.")

print(access)                                                   # printing access
f.close()


