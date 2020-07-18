# Question 1: 
# Create a list of 10 element with different type of data

print ("code for Q1 starts here: ")
A = [1,2,"mango","banana",6+5j, 8+9j,18.5, 20.2, -20,-15.5]
print (A)



# Question 2:
# Create a list of 5 and execute slicing structure 

print ("Code for Q2 starts here : ")

fruits = ["mango","orange", "banana", "cherry", "pear"]
print ("slicing the list from o to i :", fruits[:2])
print ("Slicing the list from i to end :", fruits[3:])
print ("slicing the list within a range :", fruits[2:4])
print ("slicing using negative index :", fruits[-5:-1])



# Question 3:
# create a list of given structure and run
# x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# 1 : Access list [1, 2, 3, 4]
# 2 : Access list [600,  700]
# 3 : Access list [100, 300, 500, 600, 800]
# 4 : Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# 5 : Access list [10]
# 6 : Access list [ ]

print ("Code for Q3 starts here : ")

x = [100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print ("Main list : ", x)

print ("list for the task 1 :", x[5][0:4])
print ("list for task 2 :", x[6:8])
print ("list for task 3 :", x[::1])

x.reverse()
print ("list for task 4 :", x)

print ("list for task 5 :", x[3][5][0])
print("list for task 6 :", x[99:100])



# Question 4:
# print range(1,1000) and xrange(1,1000) and see difference
''' Question was done using python 2
    x = range(1,1000) returns a list
    y = xrange(1,1000) returns a xrange object'''



# Question 5:
# How tuple is considered beneficial as compared to list
''' tuples are imutable while lsits are mutable, so you
    can change the content in the list. 
    so tuples are safer to store information which need 
    not to be altered.
    tuples are faster than lists
    Tuples are imutable so can be used as dictionary keys'''



# Question 6:
# Create a list in range 1,100
# print the numbers which are divisable by 3 and multiple of 2.

print ("Code for Q6 starts here :")

A = list(range(1,100))
print (A)

B = []
for i in A:
    if ((i%3==0) and (i%2==0)):
        B.append(i)
print(B)



# Question 7:
# Write a program to reverse a string
# print only the vowel alphabet with their index.

print ("Code for Q7 start here:")

A = "banana and orange"
print(A)
B = A[::-1]
print(B)
vowel_list = ["a","e","i","o","u"]

for i in range(len(A)):
    if A[i] in vowel_list:
        print ("index :", i, "vowel :", A[i])



# Question 8:
# Iterate through a string "hello my name is abcde"
# Print the string which has even length

print ("Code for Q8 starts here:")
string = "Hello my name is abcde"
A = []
A = string.split()
print (A)

def even_len(S):
    for i in S:
        txt = i
        if(len(txt)%2==0):
            print(txt)

even_len(A)



# Question 9:
# Write a program to print the pair of numbers.
# whose sum is equal to some number i.e  8
# x = [1,2,3,4,5,6,7,8,9,-1]

print ("Code for Q9 starts here:")

x = [1,2,3,4,5,6,7,8,9,-1]
A = []
for i in x:
    j = i+1
    for j in x:
        if(i != j):
            sum = i+j
            if (sum==8):
                print(i,j)



# Question 10:
# Write a program in python to complete following task:
# create two list even_list and odd_list
# Ask user to enter a number in range of (1,50)
# if number is even add in even_list, if odd add in odd_list
# Make sure there are not numbers more than 5 in any list
# In the add , find sum of all elements in the list
# print out the Maximum of two lists

print ("Code for Q10 starts here:")

even_list = []
odd_list  = []

while True:
    print ("please enter a number between (1,50):")
    num = int(input())

    if ((num > 50) or (num < 1)):
        print ("please enter another number")
 
    elif ((num % 2 == 0) and (len(even_list)<5)):
        even_list.append (num)
        
    elif ((num % 2 != 0) and (len(odd_list)<5)):
        odd_list.append (num) 
    
    elif ((len(even_list)==5) and (len(odd_list)==5)):
        print ("Both Lists are full")
        print ("Even_list :", even_list)
        print ("Odd_list :", odd_list )
        break
        
def sum_list(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum

even = sum_list (even_list)
odd  = sum_list (odd_list)
print ("Sum of even list :", even)
print ("sum of odd list :", odd)

if (even >= odd):
    print ("Max of sum is :", even)
else:
    print ("Max of sum is :", odd)



# Question 11:
# write a program to find occurance of alphabets in alphanumeric string
# Make sure you avoid counting numeric value
# example input :  12abcbacbaba344ab  
# output :  a=5 b=5 c=2 

print ("Code for Q11 starts here:")

str_in = "12abcbacbaba344ab"
print ("input string is:", str_in)
dict_out = {}

for i in str_in:
    if (i.isalpha()):
        if (i in dict_out): 
            dict_out[i] +=1
        else:
            dict_out[i] = 1
    else:
        continue

print (dict_out)



# Question 12:
# Generate another tupple whose values are even values from input tuple
# input tuple (1,2,3,4,5,6,7,8,9,10)

print ("Code for Q12 starts here:")

tuple_in = (1,2,3,4,5,6,7,8,9,10)
list_out = []

for i in tuple_in:
    if (i % 2 ==0):
        list_out.append(i)
    else:
        continue

tuple_out = tuple(list_out) 
print (tuple_out)