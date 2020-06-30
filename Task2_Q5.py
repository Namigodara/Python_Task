# write a program to find numbers in range 2000 to 3200
# number should be divisable by 7 but shouldn't be multiple of 5.

print("Find number between 2000 to 3200, divisable by 7 but not by 5")
for number in range(2000, 3200):
    if (number % 7 == 0):
        if(number % 5 != 0):
            print(number)
print ("End of the program")
