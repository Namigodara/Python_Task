# Write a program that asks user to "guess the 
# lucky number"
# If guess is correct program stops, else runs forever
# Part2 : modify the program to take two inputs "Number"
# and if they want to continue guessing "Answer"
# if guess is correct or Answer is No exit the program.

lucky_number = 20
number = int(input("Guess the lucky Number : "))
while (number != lucky_number):
     number = int(input("Guess the lucky Number : "))
print("YES!! lucky number is : ",number)
