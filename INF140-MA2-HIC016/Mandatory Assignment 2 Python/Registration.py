# By Steffen Rivedal Eimhjellen for Assignment 2
# Question 1

import hashlib                              # using hashlib so that we can hash the password

username = input("Please provide a username: ") 
password = input("Please choose a password: ").encode()         #encoding the text so that we can hash it

password = (hashlib.sha512(password).hexdigest())                  # hashing the text with sha512
 
f = open("shadow.txt", "a")                                         # opening the file with append access
f.write(username + " : " + password + "\n")                         # writing in the file
f.close()

print("Congratulations! Your registration has been completed!")         # lastly we print the congratulation message
