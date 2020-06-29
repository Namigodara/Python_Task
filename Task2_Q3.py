# write a program which takes Age as input to buy football match ticket
# if Age is less than or equal to 11 : Not elligible to see the match
# if Age is more than 11 you can watch the match
# ticket price for kids (age <= 20) & seniors (Age >= 60) is $12
# Tickets price for others is $20

Age = int(input("Please enter your Age : "))
if (Age >= 11):
    print ("you are eligible to see the Football match")
    if ((Age <= 20) or (Age >= 60)):
        print ("Ticket price is $12")
    else:
        print ("Ticket price is $20")
else:
    print ("You are not eligible to buy ticket")
    
