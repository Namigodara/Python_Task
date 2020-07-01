# Question 1 :
# create and assign value to three variable in single line.
# All three values should be different data type.
print("Code for Task_1 Question_1 starts here")
x,y,z = 30, 10.5, "apple"
print("x:", x)
print("y:", y)
print("z:", z)



# Question 2 :
# Create a complex variable type and swap it with another variable type Int
print("Code for Task_1 Question_2 starts here")
a,b = 1+2j, 10
print("a= ", a)
print("b= ", b)
 
 # swap the values
a,b = b,a
print("Values after swapping")
print("a= ", a)
print("b= ", b)


# Question 3 :
# Swap two variable using third variable 
print("Code for Task_1 Question_3 starts here")
x = 10
y = 20
print("Values before swapping") 
print("x= ", x)
print("y= ", y)

# Perform Swapping using third variable 
result = x
x = y
y = result 
print ("Values after first swapping using third variable")
print("x= ", x)
print("y= ", y)

# Perform Swapping without using third variable
x,y = y,x
print ("Values after second swapping without third variable")
print("x= ", x)
print("y= ", y)



# Question 4 :
# Example of print command in python3.x and pyhon2.x
'''>>> x = "try print command with python2"
>>> print x
try print command with python2'''

'''>>> x = "try print command with python3"
>>> print(x)
try print command with python3'''



# Question 5 :
# Ask user to input two numbers from 1-10.
# Add Both of them to another variable z = 30. 
print("Code for Task_1 Question_5 starts here")
print("Please enter first number between 1-10" )
x = int(input())
print("Please enter second number between 1 -10")
y = int(input())
z = 30
Result = x+y+z 
print("sum of all three variable is = ", Result)



# Question 6 :
# write code for finding out the data type of entered value.
print("Code for Task_1 Question_6 starts here")
print ("Enter an input value from keyboard ")
x = eval(input())
print("The input value datatype is : ", type(x))


# Question 7 :
'''If one data type value is assigned to ‘a’ variable and then a 
different data type value is assigned to ‘a’ again. Will it change 
the value. If Yes then Why?'''

'''Ans:  Yes, In Python data type of variable need not to be specified. 
According to Value assigned to the variable, python determines the data 
type and alocate the memory. So as soon as we re- assign the different 
data type value given, variable will store the new value.'''



