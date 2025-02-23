# 3.	Check for Palindrome
# Write a program to check whether the given string is a palindrome or not using slicing.
#******Using string reverse
palindromevalues = input('Enter the value:')
reversedstr =""
for value in palindromevalues:
    reversedstr =value+reversedstr
if(palindromevalues == reversedstr):
    print(f'This input string {palindromevalues} is a Palindrome')
else:
    print(f'This input string {palindromevalues} is not a Palindrome')

#*******using reversed()

palindromevalues = input('Enter the value:')
reversedvalue =''.join(reversed(palindromevalues))
if(palindromevalues == reversedvalue):
    print(f'This input string {palindromevalues} is a Palindrome')
else:
    print(f'This input string {palindromevalues} is not a Palindrome')