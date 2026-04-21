a = input("comment ").lower()

if ("make a lot of money" in a or
    "buy now" in a or
    "subscribe this" in a or
    "click this" in a):
    
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")