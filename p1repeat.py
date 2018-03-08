chars = "abcdefghijklmnopqrstuvwxyz"
string = str(input("enter the sentance or word:"))

for char in chars:
  count = string.count(char)
  if (count > 1):
    print (char,("is repeated") ,count ,("times"))
