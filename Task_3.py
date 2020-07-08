# Question 1 :
# Create a list of 10 element.
# it should contain four data type : int,float, complex and float.

print ("Code for Task_3 Q_1 starts here")

mix_list = [1,2,3,4,"Nami","made","this", 18.5, -1.6, 2+4j, -1+5j]
print(mix_list)



# Question 2 :
# Create a list of size 5. Perform Slicing.

print ("Code for Task_3 Q_2 starts here")

A = ["This","is","example","of","slicing"]

print ("Slicing a full list : ")
print (A[:])

print ("Slicing the list from an index i to last value")
print (A[3:])

print ("Slicing the list from index 0 to index i")
print (A[:3])

print ("Slicing the list in the range")
print (A[1:3])

print ("slicing the list in steps")
print (A[::2])

print ("slicing with negative indexing")
print (A[-3:])
print (A[:-2])
print (A[-3:-1])



# Question 3:
# Write program to find sum of element of a List
# Write a program to find multiplication of a given list.

print ("Code for Task_3 Q3 starts here :")

# Function for calculating sum of list element
def list_sum(x):
    sum = 0
    for i in range(len(x)):
        sum = sum + x[i]
    return sum

# function for calculating the product of a list
def list_prod(x):
    mult = 1
    for i in range(len(x)):
        mult = mult * x[i]
    return mult
    
# Main program
numbers = [1,2,3,4,5,6,]
print ("Given list is :", numbers)
print ("Sum of the elements :", list_sum(numbers))
print ("product of element :", list_prod(numbers))



# Question 4:
# Find a Largest and Smallest number in a List

print ("Code for Task3 Q4 starts here:")

x = [20,10,5,30,8,9,2,14]
print ("List is :", x)


for i in range(len(x)):
    if (i == 0):
        largest = x[i]
        smallest = x[i]
        continue
    
    if (largest < x[i]):
        largest = x[i]
    
    if (smallest > x[i]):
        smallest = x[i]

print ("largest number in list :", largest)
print ("Smallest number in list :", smallest)



# Question 5:
# Create a new list after removing even numbers from a list

print ("Code for Task_3 Q5 starts here:")

List_A = [2,4,5,7,8,9,11,18,15,21]
print ("List_A is :", List_A)
List_B = []

for i in range(len(List_A)):
    if (List_A[i]%2 != 0):
        List_B.append(List_A[i])

print("List_B :", List_B)



#Question 6:
# Create a list of first five and last five values.
# Values are square of numbers in range 1 to 30 both included.

print ("Code for Task3 Q6 starts here:")

list_A = []
for i in range(1,31):
    list_A.append(i**2)

list_B = []
list_B.extend(list_A[:5])
list_B.extend(list_A[-5:])
print(list_B)



# Question 7:
# Write a program to replace the last element in list with another list.
# Smaple Data [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output [1,3,5,7,9,2,4,6,8]

print ("Code for Task3 Q7 starts here:")

# Method 1 :
list_A =  [1,3,5,7,9,10]
list_B =  [2,4,6,8]
list_A.pop()
list_A.extend(list_B)
print(list_A)



# Question 8:
# Create new dictionary by concatening two.

print ("Code for Task3 Q8 starts here :")

fruit1 = {1:"apple", 2:"banana"}
fruit2 = {3:"orange", 4:"mango"}
fruit3 = {**fruit1,**fruit2}
print (fruit3)
