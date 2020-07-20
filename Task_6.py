# Question 1:
#  Write a program to go the syntax error to exception.

print ("code for task6 Q1 starts here:")

# try:
#     while True
#     x = "Hello"
#     print(x)
# except SyntaxError:
#     print ("check program for syntax error")



# Question 2 :
# Write a program in python to allow user to open file using argv
# if entered a wrong name throw an exception
# and ask them to enter the name again

from sys import argv
print ("code for task6 Q2 starts here:")
file_name = argv

while True:
    try:
        file_name = input("enter the filename : ")
        fh = open(file_name, 'r')
        content = fh.read()
        print (content)
        break
    except FileNotFoundError:
        print ("wrong file name is entered")



# Question 3:
# Write a program to handle error 
# if user entered a number more than 4 digit
# it should say number is too long/short please enter only four digit

print ("Code for task6 Q3 starts here :")

while True:
    try:
        num = int(input("Enter a 4 digit number : "))
        if (num > 999 and num <= 9999):
            print ("Given number is :", num)
            break
        else:
            raise Exception
    except:
        print ("number is too long/short, please enter only four digit")



# Question 4:
# create a login page backend to ask user to enter Useremail and password
# make sure to give three chance to re-enter if password is wrong
# username used : ngodara
# password : Pass123

print ("Code for task6 Q4 starts here")
count = 1

while True:
    try:
        username = input ("Username : ")
        password = input ("Password : ")
        if (username == "ngodara" and password == "Pass123"):
            print ("login is successful")
            break
        else:
            raise Exception
    except:
        if (count <= 3 ):
            print ("incorrect username or passwrod, enter again ")
            count +=1
            continue
        else:
            print ("maximum number of attempt reached")
            break



# Question 6:
# read a file using python file handling concept
# print the line only with even length string from doc.txt

print ("code for task6 Q6 starts here ")

fh = open("doc.txt", 'r')

for x in fh:
    if (len(x)%2==0):
        print(x)
