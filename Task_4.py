# Question 1:
# Write a program to reverse a string.
# Sample input :"1234abcd" output:"dcba4321"

print ("Code for Task4 Q1 starts here:")
print ("Enter a string :")
str_in = input()

def reverse(in_str):
    str_reverse = in_str[::-1]
    print ("Reverse string is :", str_reverse)

reverse(str_in)