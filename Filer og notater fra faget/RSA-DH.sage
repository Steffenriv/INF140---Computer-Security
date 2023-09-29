# RSA Toy Example

print("================RSA Example=====================")

# Key Generation
p = 17
q = 11

n = p * q
phi_n = (p-1)*(q-1)

e = 7
d = inverse_mod(e, phi_n)

print("Public Key: ", [n, e])
print("Private Key:", [p, q, d])

# Encryption
m = 88
c = mod(m^e, n)
print("ciphertext c = ", c)

#Decryption
m1 = mod(c^d, n)
print("Output of decryption:", m1)
print("Correct Decryption: ", m == m1)




# Diffie-Hellman Example 
print("================DH Example=====================")

p = 187
g = 2

print("Public Parameters:", [p, g])


# Alice

a = 13
a_pub = mod(g^a, p)

print("Alice: ", [a, a_pub])

# Bob

b = 5
b_pub = mod(g^b, p)

print("Bob: ", [b, b_pub])


print("Shared Key for Alice: ", mod(b_pub^a, p))
print("Shared Key for Bob: ", mod(a_pub^b, p))






