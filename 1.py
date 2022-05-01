# Write a Java/C/C++/Python program that contains a string (char pointer) with a value 'Hello World'. The program should AND or and XOR each character in this string with 127 and display the result.
s = "Hello World"
and_output = ""
or_output = ""
xor_output = ""

for c in s:
    and_output += chr(ord(c) & 127)
    or_output += chr(ord(c) | 127)
    xor_output += chr(ord(c) ^ 127)

print("AND Operation Output -> ", and_output)
print("OR Operation Output -> ", or_output)
print("XOR Operation Output -> ", xor_output)

# Expected Output
# AND Operation Output ->  Hello World
# OR Operation Output ->  
# XOR Operation Output ->  7_(