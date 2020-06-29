# Ask user to enter mode of operation : 1 - Addition, 2 - Subtraction
# 3 - Division, 4 - Multiplication, 5 - Average
# Ask user to enter two values for operation 1 to 4.
# Ask user to enter two more values for operartion 5.
# In the end if solution to any operation is negative , Print "Zsa"
# at a time user can perform only one operation.

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
