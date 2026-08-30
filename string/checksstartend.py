#Input a string and check whether it starts and ends with a particular character.

string = input("enetr a string")
char = input("Enetr a character")

if string.startswith(char) and string.endswith(char):
    print("string start and ends with the given character")
else:
    print("string doesnot starts and ends with given character")