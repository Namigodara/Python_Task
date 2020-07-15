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



# Question 2:
# Write a program that accepts a string
# Calculate the upper case and lower case in string.

print ("Code for Task4 Q2 starts here:")

print("Enter the input string:")
str_in = input()

def count(in_str):
    upper = 0
    lower = 0
    for i in in_str:
        if (i >="A" and i <="Z"):
            upper +=1
        if (i >= "a" and i <="z"):
            lower +=1
    return (upper,lower)

upper,lower = count(str_in)
print ("Upper case count in string :", upper)
print ("lower case count in string :", lower)



# Question 3:
# Create a function which takes a list
# and generate new list with unique values

print ("Code for Task4 Q3 starts here:")

A = [1,2,3,4,5,1,2,3,"Hello", "mango", "Hello"]
print ("input list is :", A)

def unique(list_in):
    list_out = []
    for i in A:
        if i not in list_out:
            list_out.append(i)
    return list_out

B = unique(A)
print ("output list with unique values :", B)



# Question 4:
# Write a program that accepts - (hyphen) separated seq of word as input
# and print the ouput in hyphen seperated seq after sorting it out.

print ("Code for Task4 Q4 starts here:")

print("Enter a hyphen separated seq")
str_in = input()

def sort (x_str):
    x_list = x_str.rsplit("-")
    sort_list = sorted(x_list)
    str_out = "-".join(sort_list)
    return str_out

res = sort(str_in)
print("sorted output :", res)




# Question 5:
# Write a program that accepts sequence of lines as input
# print the line after making all character capitalization. 
# Sample input :
''' Hello World
    Practice makes it perfect'''
# Expected Output:
''' HELLO WORLD
    PRACTICE MAKES IT PERFECT'''

print("Code for task4 Q5 starts here:")

print ("Enter the count of line you want to enter: ")
count = int(input())

l =[]
print ("Enter the input lines one by one:")
for i in range(count):   
    str_in = input()
    x = str_in.upper()
    l.append(x)
    
print ("Output seq is: ")
print (*l, sep = "\n")



# Question 6:
#  Write a function that can take two integral as string
# compute their sum and print in console

print ("code for task4 Q6 starts here:")

print("Enter the first string of number:")
str1 = input()
print("Enter the second string of number:")
str2 = input()

def sum_str(x1,x2):
    int1 = int(x1)
    int2 = int(x2)
    sum = int1 +int2
    return sum

res = sum_str(str1,str2)
print ("Sum of two numbers is :", res)



# Question 7:
# Write a function which accepts two strings as input
# prints the string with maximum length
# if both are same length then it prints both of them

print("code for task4 Q7 starts here:")

print ("enter the firts string:")
str1 = input()
print ("enter the second string:")
str2 = input()

def max_len(s1,s2):
    if (len(s1)==len(s2)):
        print (s1)
        print (s2)
    elif (len(s1) > len(s2)):
        print (s1)
    else:
        print (s2)

print ("output:")
max_len(str1,str2)



# Question 8:
# Define a function to generate a tuple
# values of tuple are square of number 1 to 20

print ("Code for task4 Q8 starts here:")

def square(n):
    l = []
    for i in range(1,n):
        l.append(i**2)
   
    x_tuple = tuple(l)
    return (x_tuple)

x_out = square(20)
print(x_out)
