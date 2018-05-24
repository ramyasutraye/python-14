a=int(input("enter the lower limit:"))
b=int(input("enter the upper limit:"))
c=int(input("enter the num to be found in the range:"))
if c in range(a,b):
    print("yes it is in the given range")
else:
    print("the num is not in the range")
