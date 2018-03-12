num = int(input("Enter a number:"))
def finding(x):
	for i in range(1, x+1):
		if x % i == 0:
			print(i);
print("Factors of given number are:")
finding(num)
