a =  int(input("enter no. 1: "))
b =  int(input("enter no. 2: "))
c =  int(input("enter no. 3: "))
d =  int(input("enter no. 4: "))
if(a>b and a>c and a>d):
    print("a is greatest")
elif(b>a and b>c and b>d):
    print("b is greatest")
elif(c>a and c>b and c>d):
    print("c is greatest")
elif(d>a and d>b and d>c):
    print("d is greatest")
else:    print("all are equal") 