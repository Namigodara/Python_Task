# Swap two variable using third variable 
x = 10
y = 20
print("Values before swapping") 
print("x= ", x)
print("y= ", y)

# Perform Swapping using third variable 
result = x
x = y
y = result 
print ("Values after first swapping using third variable")
print("x= ", x)
print("y= ", y)

# Perform Swapping without using third variable
x,y = y,x
print ("Values after second swapping without third variable")
print("x= ", x)
print("y= ", y)



