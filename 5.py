# Write a Java/C/C++/Python program to implement RSA algorithm.

def encrypt(plainText, e, n):
    cipherText = (plainText ** e) % n
    return cipherText

def decrypt(cipherText, d, n):
    plainText = (cipherText ** d) % n
    return plainText

def isPrime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def gcd(a, h):
    while(True):
        tmp = a % h
        if tmp == 0:
            return h
        a = h
        h = tmp


print("Generating Public Key....")
p = int(input("Enter first prime number: "))
while(not isPrime(p)):
    print(p, " is not a prime number, please try again")
    p = int(input("Enter first prime number: "))

q = int(input("Enter second prime number: "))
while(not isPrime(q)):
    print(q, " is not a prime number, please try again")
    q = int(input("Enter second prime number: "))

n = p * q
e = 2
phi = (p - 1) * (q - 1)
while(e < phi):
    if (gcd(e, phi) == 1):
        break
    else:
        e += 1

print("Generating Private Key....")
k = int(input("Enter the value for k: "))
d = (1 + (k * phi)) // e

message = int(input("Please enter the plain text message (Only Positive Integers): "))
cipherText = encrypt(message, e, n)
print("Cipher Text = ", cipherText)
plainText = decrypt(cipherText, d, n)
print("Plain Text = ", plainText)

# Expected Output
# Generating Public Key....
# Enter first prime number: 3
# Enter second prime number: 7
# Generating Private Key....
# Enter the value for k: 2
# Please enter the plain text message (Only Positive Integers): 12
# Cipher Text =  3
# Plain Text =  12