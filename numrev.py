number=int(input("enter the num to reverse"))
reverse=0
while(number>0):
    rem=number%10
    reverse=(reverse*10)+rem
    number=number//10
print("the reversed value is=%d"%reverse)

