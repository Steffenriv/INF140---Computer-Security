# By Steffen Rivedal Eimhjellen for Assignment 1
# Question 6.1.3

p, q, e, m = 7, 17, 29, 7                # Defining our variables p q e and M so we can use them later.

phi_n = (p-1)*(q-1)                     # Calculating phi_n 
n = p*q
d = 0                                   # Defining d as an integer the answer to d is not 0 as it cannot be 0,
                                        # just so it works well in our loop
                                        # Now making a loop so we can go through all values of d and find the correct value of d
for d in range(phi_n):                      # loops it from 0 to phi_n as d has to be lower than phi_n
    if d != 1 and d != 0 and d !=e:     # also sets  values that d cannot be alike, as d has to be higher than 0,1 and cannot be = 5 due to e = 5
        if((d * e) % phi_n == 1):           # using the formula to find d.
            break                       # stop the loop when we find d.
        else:
            continue                    # continues the loop if we don't find it

encrypted = (m**e) % n                 # using the formula to find encrypted C
print(f"encrypted: {encrypted}")

decrypted = (encrypted**d) % n         # using the formula to find decrypted M
print(f"decrypted: {decrypted}")

