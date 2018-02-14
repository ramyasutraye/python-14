while True:
	ch = input("Enter any character: ")
	if ch == '0':
		break
	else:
		if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
			print(ch, "is an alphabet.\n")
		else:
			print(ch, "given num is not an alphabet.\n")
