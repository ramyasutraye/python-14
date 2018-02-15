def add(n1,n2):
   return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def power(n1,n2):
    return n1**n2
print("select any option:" "\n1.Add" "\n2.subtract""\n3.multiply" "\n4.divide" "\n5.power")
num = int(input("Enter choice(1/2/3/4/5):"))
n1=(input("enter the first value"))
if (n1== int):
    print(n1)
if (n1 == float):
    print(n1)
n2=(input("enter the second value"))
if (n2== int):
    print(n2)
if (n2 == float):
    print(n2)
if (num==1):
    print(add(n1,n2))
elif (num==2):
    print(subtract(n1,n2))
elif (num==3):
    print(multiple(n1,n2))
elif (num==4):
    if (n2==0):
        print("infinity")
    else:
        print(divide(n1,n2))
elif (num==5):
    if (n1 or n2<=0):
        print("enter a positive num")
    else:
        print(power(n1,n2))
else:
    print("enter a valid choice")
   
    
   
   #func defined and func called
