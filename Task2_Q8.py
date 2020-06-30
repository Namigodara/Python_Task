# Program for calculating number of albhabet and digit in given string

alphabet = 0
digit = 0
string = str(input("Enter the string : "))
string_length = len(string)
for i in range (string_length):
    if (string[i].isalpha()):
        alphabet = alphabet + 1
    elif (string[i].isdigit()):
        digit = digit + 1
print ("Total Alphabets in string :", alphabet)
print ("Total Digits in string :", digit)