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
print("select any option:" "\n1.Add" "\n2.subtract""\n3.multiply" "\n4.divide" "\n5.square")
num = int(input("Enter choice(1/2/3/4/5):"))
n1=int(input("enter the first value"))
n2=int(input("enter the second value"))
if (num==1):
    print(add(n1,n2))
elif (num==2):
    print(subtract(n1,n2))
elif (num==3):
    print(multiple(n1,n2))
elif (num==4):
    print(divide(n1,n2))
elif (num==5):
    print(power(n1,n2))
else:
    print("enter a valid choice")
   
   #func defined and func called
