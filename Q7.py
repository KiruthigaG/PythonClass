# 7.	Convert First Letter of Each Word to Uppercase
# Write a program that takes a sentence as input and prints the initials of each word in uppercase.

str = input("Enter the text here:")
strsplit = str.split(" ")
newstr =' '
for value in strsplit:
    newvalue = value.capitalize()
    newstr = newstr+ " " +newvalue
print("Result after Capitalization:")
print(newstr)