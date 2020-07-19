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
# Write a function that can take two integral as string
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



# Question 9:
# Write a function called showNumbers that take limit as parameter
# It should print all the numbers between 0 and limit
# it should label printed number with even and odd
# ex if limit is 3
# output:
''' 0 EVEN
    1 ODD
    2 EVEN
    3 ODD'''

print ("Code for Task4 Q9 starts here:")

def showNumbers(limit):
    for i in range(limit):
        if (i%2==0):
            print (i,"EVEN")
        else:
            print (i,"ODD")

showNumbers(4)



# Question 10:
# Write a program which can filter() {A built in pyhthon function}
# to make a list of even numbers between 1 to 20 (Both included)


print ("Code for task4 Q10 starts here:")

number = list(range(1,21))

def even(x):
    if (x%2==0):
        return True
    else:
        return False
    
res = filter (even,number)
l = []
for i in res:
    l.append(i)
print (l)



# Question 11:
# Write a program which can map() and filter() to make a list
# Whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]

print("code for task4 Q11 starts here:")
x = [1,2,3,4,5,6,7,8,9,10]

def even (n1):
    if (n1%2==0):
        return True
    else:
        return False

def square (n2):
    return n2**2

res1 = filter (even, x)
res2 = map (square,res1)
print (list(res2))



# Question 12:
# Write function to compute 5/0
# use try/except block to catch exception.

print ("Code for Task4 Q12 starts here:")

try:
    n1 = int(input("Enter the first number : "))
    n2 = int(input("Enter the second number : "))
    div = n1/n2
    print ("division :",div)
except ZeroDivisionError:
    print ("can not be divided by 0")



# Question 13:
# flattern the list using reduce()
# input : [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8]
# goal [1,2,3,4,5,6,7,8] turn to 1234567 

print("Code for Task4 Q13 starts here:")
import functools

list_in = [[1,2,3],[4,5],[6,7,8]]
list_out = functools.reduce(lambda x,y:x+y,list_in)
print (list_out)

str1 = ""
for i in list_out:
    str1 += str(i)
print(str1)



# Question 14:
# Write the output of given blocks

'''def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)'''

# Output 1: 2

'''def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
a()'''

# Output : NameError: name 'f' is not defined
