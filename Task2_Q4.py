# program takes a number from user
# if a negative number Break the program
# If a positive number just continue in the loop and  print"Good Going"

Number = int(input("Enter a number : "))
while True:
    if (Number < 0):
        break
    print("Good Going")
    Number = int(input("Enter a number : "))
print ("It's Over")

    



