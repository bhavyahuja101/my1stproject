a = input("comment ").lower()

if ("make a lot of money" in a or
    "buy now" in a or
    "subscribe this" in a or
    "click this" in a):
    
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")

list = ["mohan" , "sohan" , "rohan"]    
myname = input("enter your name")
if myname in list :
    print("you are selected")
else:
    print("you are not in list sadddd")    