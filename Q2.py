# Question:2.Ask the user to enter a word.
# 	•	If the word has an even number of characters, print “Even length: [word in uppercase]”.
# 	•	If the word has an odd number of characters, print “Odd length: [word reversed]”



value= input("Enter a word:")
count=0
for char in value:
    if char.isalpha():
        count = count+1
print(f'Length of the word entered:{count}')
if(count %2 ==0):
    print(f'Even length: {value.upper()}')
else:
    reverse_value = value[::-1]
    print(f'Odd length: {reverse_value}')

