# By Steffen Rivedal Eimhjellen for Assignment 1
# Question 7

c = 82          # We know this because of the message bob sends to alice, which is 82. Therefor we know the ciphertext is 82.
n, e = 341, 7   # we know this because, this is what alice chose as RSA keys.
m = 1           # Sets m = 1 at first, then we send m through a loop to see for which m value, m^7 mod(341) = 82 equation will go up.

while m > 0:                # Using a while loop so we don't have to deal with inverse modular.
    if (m**7 % 341) == 82:  # Using an if command to se if, for each number m loops through, the equation goes up and we find our key.
        break               # stops the loop whenever we find the value of m, and we find our key.
    else:
        m += 1              # setting m + 1, so we can check the next number. We are doing this everytime we go through the loop
        continue            # until we find m's proper value. Then continues to continue going through the loop.

print(f" \n The key in digits = {m} \n")        # FInally we print the key in digits.

          
