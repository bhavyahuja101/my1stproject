a = input("comment ").lower()

if ("make a lot of money" in a or
    "buy now" in a or
    "subscribe this" in a or
    "click this" in a):
    
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")

list = ["mohan" , "sohan" , "rohan"]    
myname = input("enter your name ")
if myname in list :
    print("you are selected")
else:
    print("you are not in list sadddd")    

username = input("Enter username: ")

if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("Your username contains more than or equal to 10 characters")