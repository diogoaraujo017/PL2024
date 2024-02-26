import re
import os

# Open the file and read the text
file = open("TPC3/input.txt", "r")
info = file.read()  

# Putting the text in lower case
info = info.lower()

# Tokenize the input
tokenList = re.findall(r'(on|off|-?[0-9]+|=)', info)

# List to store the numbers to sum
sum = 0

# Flag to check if the sum is on or off
flag = False

# Iterate through the tokens to sum the numbers
for i in range(len(tokenList)):
    if tokenList[i] == 'on':
        flag = True
    elif tokenList[i] == 'off':
        flag = False
    elif tokenList[i] == '=':
        print(f"Soma no token numero {i}: {sum}")   
    elif flag:
        sum += int(tokenList[i])        
        

        