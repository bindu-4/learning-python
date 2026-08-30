#Input a string and check whether it is uppercase, lowercase or mixed case.
string = input("Enter a string")
if(string.isupper()):
    print("string is uppercase")
elif(string.islower()):
    print("string is lowercase")
else:
    print("String is mixed")