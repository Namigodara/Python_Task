# Write a program to guess the lucky number
# use a while loop counter such as counter = 1
# in while(counter <= 5) loop continues
# if number is correct  program breaks
# if number is wrong output is ("Try again!") 
# if none of the guess was correct print
# "Sorry but that was not very successful"

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