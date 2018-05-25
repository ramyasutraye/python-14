a=[int(x) for x in input("enter the elements in  list1:").split()]
b=[int(x) for x in input("enter the elements in list2:").split()]
if (set(a) & set(b)):
    print("common element exists")
else:
    print("no")
