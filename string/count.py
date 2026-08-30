#Input a string and count how many times a particular character occurs.
string = input("Enter a string: ")
char = input("Enter a character to count: ")

count = string.count(char)

print("Character occurs", count, "times")