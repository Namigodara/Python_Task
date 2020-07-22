# Question 1:
# Write a program using high order function.
# to find a value which is multiply of 7 but not divisable by 3

print ("Code for task5 Q1 starts here:")

x = list(range(1,71))

y = filter (lambda i:(i%3 != 0)and(i%7==0),x)
print ("List of numbers divisable by 7 but not by 3 :")
print (list(y))



# Question 2:
# Write a program in python using traditional function
# to multiply the list of elements
# pass the function to map it in order to complete program

print ("Code for task5 Q2 starts here:")

x = [1,2,3,4,5,6]


def mul (x1):
    res = 1
    for i in x1:
        res = i * res
    return res

y = mul(x)
print ("product of list:",y)



# Question 3:
# Write a program to find out uppercase in string 
# using list comprehension

print ("Cade for task5 Q3 starts here:")

print ("Enter the string with Upper and Lower Case:")
str1 = input()
out = [i for i in str1 if (i >= 'A' and i<='Z')]
print("list of uppercase in string ;",out)



# Question 4:
# Write a program to construct a dict from two lists
# Student = ['Smit', 'Jaya', 'Rayyan']
# capital = ['CSE', 'Networking', 'Operating System']
# Map student to their respective subject 
# use list student as key and subject as value
# Use for loop, dictionary comprehension, zip function

print ("Code for task5 Q4 starts here:")

student = ['Smit', 'Jaya', 'Rayyan']
subject = ['CSE', 'Networking', 'Operating System']
print ("student:", student)
print ("subject:", subject) 

# Method 1 using for loop
dict1 = {}
for s in range(len(student)):
    dict1[student[s]] =  subject[s] 
    
print (dict1)


# Method 2: Dictionary comprehenstion
dict2 = {student[i]:subject[i] for i in range(len(student))}
print (dict2)

# Method 3: using zip function
dict3 = dict(zip(student,subject))
print(dict3)




# Question 5:
# Learn more about yield, next and generators:

'''Python generators are a simple way of creating iterators.    
Simply speaking, a generator is a function that returns an object (iterator) 
which we can iterate over (one value at a time). 

It is fairly simple to create a generator in Python. 
It is as easy as defining a normal function, 
but with a yield statement instead of a return statement.

If a function contains at least one yield statement 
(it may contain other yield or return statements), it becomes a generator function. 
Both yield and return will return some value from a function.
The difference is that while a return statement terminates a function entirely, 
yield statement pauses the function saving all its states 
and later continues from there on successive calls.'''

''' Example :
def sq(x):
    for i in range(x):
        yield i*i

res = sq(5)'''''
''' we can write for or while loop to print values.
while True:
    try:
        print(next(res))
    except StopIteration:
        break'''



# Question 6:
# Write a program in python using generators to reverse the string
# input string = "Counsultadd Training"

print ("Code for task5 Q6 starts here:")

str_in = "Consultadd Training"

def reverse (x):
    yield (x[::-1])

str_out = reverse (str_in)

while True:
    try:
        print(next(str_out))
    except StopIteration:
        break



# Question 7: 
# Write any example of decorator 

print ("Code for Task5 Q7 starts here:")

def repeat(function):
    print ("this decorator calls function multiple times")
    count = 1
    while (count <= 2):
        function ()
        count +=1
    return function

@repeat
def sum():
    res = 3+4
    print(res)

sum()



# Question 8 :
# Learn about What is FRONT END and its Technologies and Tools
# Make sure to mention at least 5 top notch technologies of Frontend.
# Also mentioned the name of companies using 
# those 5 technologies individually

''' Front End Technology :
    front-end development is the art of creating sites and 
    web applications that render on the client-side.
    While there are many different types of technologies and stacks, 
    most front-end web developers use HTML, CSS and JavaScript, 
    the de facto building blocks of the web, and client-side frameworks 
    such as Angular, React, Stencil and Vue.

    1. react: Airbnb, Dropbox, BBC, Facebook
    2. AngularJS : Netflix , upwork, IBM
    3. Ionic : The National health service, GE transportation 
    4. Bootstrap : twitter, spotify, Udemy 
    5. Flutter : Google ads, Alibaba, Birch finance 
    6. Vue.js : Github, Netguru, nelify
    '''
    