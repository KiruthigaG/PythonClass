# 4.	Find and Replace a Word
# Take a sentence and a word as input. If the word exists in the sentence, replace it with "Python", otherwise print "Word not found".

sentence =input("Enter here:")
findword="C#"
replaceword ="Python"
result =sentence.find(findword)
if result!=-1:
    newsentence = sentence.replace(findword,replaceword)
    print("Before replacing: " +sentence)
    print("After replacing: " +newsentence)
else:
    print("Word not found")