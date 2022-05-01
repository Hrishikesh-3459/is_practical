# Write a Java/C/C++/Python program to perform encryption and decryption using the method of Transposition technique.

def encrypt(plainText, secretKey):
    secretKeyLength = len(secretKey)
    cipherTextArray = ["" for i in range(secretKeyLength)]
    for i in range(len(plainText)):
        position = i % secretKeyLength

        if plainText[i] == " ":
            cipherTextArray[position] += "_"
        else:
            cipherTextArray[position] += plainText[i]

    for n,i in enumerate(cipherTextArray):
        cur_len = len(i)
        if cur_len != secretKeyLength:
            cipherTextArray[n] += ("_" * (secretKeyLength - cur_len))

    finalCipherText = ""
    for i in sorted(secretKey):
        originalPosition = secretKey.index(i)
        finalCipherText += cipherTextArray[originalPosition]

    return finalCipherText

def decrypt(cipherText, secretKey):
    secretKeyLength = len(secretKey)
    plainTextArray = ["" for i in range(secretKeyLength)]

    position = 0
    for i in sorted(secretKey):
        originalPosition = secretKey.index(i)
        plainTextArray[originalPosition] = cipherText[position:position + secretKeyLength]
        position += secretKeyLength

    finalPlainText = ""
    for i in range(secretKeyLength):
        for s in plainTextArray:
            if s[i] == "_":
                finalPlainText += " "
            else:
                finalPlainText += s[i]

    return finalPlainText

try:
    decision = int(input("Enter 1 to encrypt Plain Text, 2 to decrypt Cipher Text: "))
    if decision == 1:
        plainText = input("Please enter plain text: ")
        secretKey = input("Please enter secret key: ")
        print("Cipher Text = ", encrypt(plainText, secretKey))

        # Expected Output
        # Please enter plain text: Geeks for Geeks
        # Please enter secret key: HACK
        # Cipher Text = e__kefGsGsrekoe_
    elif decision == 2:
        cipherText = input("Please enter cipher text: ")
        secretKey = input("Please enter secret key: ")
        print("Plain Text = ", decrypt(cipherText, secretKey))

        # Expected Output
        # Please enter cipher text: e__kefGsGsrekoe_
        # Please enter secret key: HACK
        # Plain Text = Geeks for Geeks 
    else:
        print("Incorrect input")
except:
    print("Incorrect input")