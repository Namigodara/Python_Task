# Write a program to guess the lucky number
# use a while loop counter such as counter = 1
# in while(counter <= 5) loop continues
# Program asks for 5 guesses even if answer is correct
# if number is correct output is ("Good Guess!")
# if number is wrong output is ("Try again!") 
# after the fifth iteration it stops ("Game Over!")

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

    