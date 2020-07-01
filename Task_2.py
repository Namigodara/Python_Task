# Question 1 :
# Write a program in python to perform the following
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “c” as a string
# If a number is divisible by both 3 and 5 its should print “Consultadd 
# Python Training” as a string.

print("Code for Task_2 Question_1 starts")

Value = eval(input("Enter a number: "))
print ("Input value is: ", Value)

if ((Value % 3 == 0) and (Value % 5 == 0)):
    print ("Consultadd Ptyhon Training")
elif (Value % 3 == 0):
    print ("consultadd")
elif (Value % 5 == 0):
    print ("c")
else:
    print ("do nothing")



# Question 2 :
# Ask user to enter mode of operation : 1 - Addition, 2 - Subtraction
# 3 - Division, 4 - Multiplication, 5 - Average
# Ask user to enter two values for operation 1 to 4.
# Ask user to enter two more values for operartion 5.
# In the end if solution to any operation is negative , Print "Zsa"
# at a time user can perform only one operation.

print("Code for Task_2 Question_2 starts")

print ("Enter the mode of operation from following")
print ("1 : Addition")
print ("2 : Subtraction")
print ("3 : Division")
print ("4 : Multiply")
print ("5 : Average") 
Operator = int(input())

print("Now enter two input Values")
Val1 = eval(input("Val1 : "))
Val2 = eval(input("Val2 : "))

if (Operator not in range(1,6)):
    print ("Invalid mode of operation")
elif (Operator == 1):
    Result = Val1 + Val2
    print ("Addition of two values is :", Result)
elif (Operator == 2):
    Result = Val1 - Val2
    print ("Difference of two values is:", Result)
elif (Operator == 3):
    Result = Val1 / Val2
    print ("Division of two values is :", Result)
elif (Operator == 4):
    Result = Val1 * Val2 
    print ("Multiplication of two values is :", Result)
elif (Operator == 5):
    print ("For average enter two more values")
    first1 = eval(input("enter first1 : "))
    second2 = eval(input("enter second2 : "))
    Result = (Val1 + Val2 + first1 + second2) / 4
    print ("Average of all four values is :", Result)

if (Result < 0):
    print("Zsa")



# Question 3 :
# write a program which takes Age as input to buy football match ticket
# if Age is less than or equal to 11 : Not elligible to see the match
# if Age is more than 11 you can watch the match
# ticket price for kids (age <= 20) & seniors (Age >= 60) is $12
# Tickets price for others is $20

print("Code for Task_2 Question_3 starts")

Age = int(input("Please enter your Age : "))

if (Age >= 11):
    print ("you are eligible to see the Football match")
    if ((Age <= 20) or (Age >= 60)):
        print ("Ticket price is $12")
    else:
        print ("Ticket price is $20")
else:
    print ("You are not eligible to buy ticket")




# Question 4 :
# program takes a number from user
# if a negative number Break the program
# If a positive number just continue in the loop and  print"Good Going"

print("Code for Task_2 Question_4 starts")

Number = int(input("Enter a number : "))

while True:
    if (Number < 0):
        break
    print("Good Going")
    Number = int(input("Enter a number : "))

print ("It's Over")



# Question 5 :
# write a program to find numbers in range 2000 to 3200
# number should be divisable by 7 but shouldn't be multiple of 5.

print("Code for Task_2 Question_5 starts")

print("Find number between 2000 to 3200, divisable by 7 but not by 5")

for number in range(2000, 3200):
    if (number % 7 == 0):
        if(number % 5 != 0):
            print(number)

print ("End of the program")


# Question 6 :
# What will be output of three examples.
# Example 1:
'''x=123 
for i in x:
   	print(i)
'''

'''Output : TypeError: 'int' object is not iterable'''

# Example 2:
'''i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("error")'''

'''Output :
0
1
2'''

# Example 3 :
'''count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break'''

'''Output :
NameError: name 'Break' is not defined'''



# Question 7 :
# Program for print the number from 0 to 6 except 3 and 6.

print("Code for Task_2 Question_7 starts")

print("Start printing the numbers")
for number in range(0,6):
    if(number == 3 or number == 6):
        continue
    print(number)

print("End of the program")



# Question 8 :
# Program for calculating number of albhabet and digit in given string

print("Code for Task_2 Question_7 starts")

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



# Question 9 : (Only Part 2 , Part 1 is in separate file)
# Write a program that asks user to "guess the 
# lucky number"
# If guess is correct program stops, else runs forever
# Part2 : modify the program to take two inputs "Number"
# and if they want to continue guessing "Answer"
# if guess is correct or Answer is No exit the program.

print("Code for Task_2 Question_9 starts")

lucky_number = 20
number = int(input("Guess the lucky Number : "))

while (number != lucky_number):
    answer = str(input("Do you want to guess again : "))
    if (answer == "no"):
        print ("Player doesn't want to continue, Game ends")
        break
    number = int(input("Guess the lucky Number : "))

if(number == lucky_number):
    print("YES!! lucky number is : ",number)



# Question 10 :
# Write a program to guess the lucky number
# use a while loop counter such as counter = 1
# in while(counter <= 5) loop continues
# Program asks for 5 guesses even if answer is correct
# if number is correct output is ("Good Guess!")
# if number is wrong output is ("Try again!") 
# after the fifth iteration it stops ("Game Over!")

print("Code for Task_2 Question_10 starts")

lucky_number = 20
counter = 1

while (counter <= 5):
    number = int(input("Guess the number : "))
    print("count :", counter, "Number :", number )
    counter = counter + 1
    
    if (number == lucky_number):
        print("Good Guess")
    else:
        print("Try Again") 

print("Game Over!")



# Question 11 :
# Write a program to guess the lucky number
# use a while loop counter such as counter = 1
# in while(counter <= 5) loop continues
# if number is correct  program breaks
# if number is wrong output is ("Try again!") 
# if none of the guess was correct print
# "Sorry but that was not very successful"

print("Code for Task_2 Question_10 starts")

lucky_number = 20
counter = 1

while (counter <= 5):
    number = int(input("Guess the number : "))
    print("count :", counter, "Number :", number )
    counter = counter + 1
    
    if (number == lucky_number):
        print("Good Guess")
        break
    else:
        print("Try Again")    

if (number != lucky_number):        
    print("Sorry but that wasn't very successful")
