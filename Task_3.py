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
