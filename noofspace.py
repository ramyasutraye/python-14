string = input("enter the data:")
counter = 0
for i in string:
    if i == ' ' or i == '\n':
        counter += 1
print(counter)
