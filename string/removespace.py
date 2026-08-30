# Input a string and remov extra spaces from beginning and end
string = input("Enetr a string")
new_string = string.strip()
print("String after removing spaces:", new_string)
#Input a person's full name and display the name in a formatted form.
full_name = input("Enter a full name")
print("formated name =",full_name.title())
#Count the number of words in a sentence
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Number of words =", len(words))