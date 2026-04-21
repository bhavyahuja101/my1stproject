sub1 = int(input("enter marks of physics: "))
sub2 = int(input("enter marks of chemistry: "))
sub3 = int(input("enter marks of maths: "))

if(sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and (sub1+sub2+sub3)/3 >= 40):
    print("you are pass")
else:
    print("you are fail baby")