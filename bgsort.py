from statistics import median
n = [int(x) for x in input("enter the elements to be sorted:").split()]
print(n,"-the unsorted list")
n.sort()
print(n, "-the sorted list")
print(median(n))
