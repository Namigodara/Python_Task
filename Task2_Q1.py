# Write a program in python to perform the following
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “c” as a string
# If a number is divisible by both 3 and 5 its should print “Consultadd 
# Python Training” as a string.


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




