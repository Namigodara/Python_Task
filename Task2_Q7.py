# Program for print the number from 0 to 6 except 3 and 6.

print("Start printing the numbers")
for number in range(0,6):
    if(number == 3 or number == 6):
        continue
    print(number)
print("End of the program")
