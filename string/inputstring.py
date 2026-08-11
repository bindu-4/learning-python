#input string and display its first character,last character and middle character using index
a = (input("Enter a string"))
ch = a[0]
last = a[-1]
middle = a[len(a) // 2]
print("first character" , ch)
print("last character" , last)
print("middle character" , middle)