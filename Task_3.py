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
