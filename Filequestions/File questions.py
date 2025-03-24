#1. Write a Python program to create a new text file called sample.txt and write "Hello, World!" into it.
filename = "sample.txt"
file=open(filename,'w')
file.write("Hello, World!")
file.close()
# 2. Write a Python program to read the contents of sample.txt and print them to the console.
result=open(filename,'r')
print(result.read())
result.close()
#3. Modify your program to append the text "Welcome to Python file handling!" to sample.txt.
with open(filename,'a') as modifyfile:
    modifyfile.write("\nWelcome to Python file handling!")
# 4. Write a program to read a file line by line and print each line.
with open(filename,'r') as readlinebyline:
    for line in readlinebyline:
        print(line)
#5. Modify the above program to store all lines in a list and print them.
filelist=[]
with open(filename,'r') as readlinebyline:
    filelist = readlinebyline.readlines()
    print(filelist)
# 6. Write a function that reads a file and counts the number of lines in it.
def filecount(filename):
    count = 0
    file=open(filename,'r')
    for line in file:
        count+=1
    print(f'Total number of lines in the file are:{count}')
filecount(filename)
# 7. Write a Python program to read only the first 5 lines of a file.
newfile="sample1.txt"
files=open(newfile,'r')
fileread=files.readlines()
print(fileread[:5])
# 8. Write a Python program that reads a CSV file called employees.csv and prints all employee names.
import csv
file=open("E:\Study\Python\employee.csv",'r')
csvreader=csv.reader(file)
for rows in csvreader:
    print(rows)
# 9. Write a Python program that writes a dictionary of student marks into a JSON file named marks.json.
import json
marks={'English':90,'Tamil':99,'Maths':90,'Physics':98}
with open('newfile.json','w') as newfilejson:
    json.dump(marks,newfilejson)
# 10. Read a JSON file called config.json and print its contents as a dictionary
import json
with open('config.json','r') as readfile:
    data =json.load(readfile)
print(data)
# 11. Write a Python program to count the number of words in a given text file.
with open('sample1.txt','r') as countfile:
    data=countfile.read()
    print(len(data.split()))
# 12. Write a function that searches for a specific word in a file and prints the line numbers where it appears.
word="kiruthiga"
with open('sample1.txt','r') as readfile:
    i=0
    data=readfile.readlines()
    linenumber=len(data)
    for i in range(linenumber):
        line=data[i]
        if word in line:
            print(f'The linenumber of the word is:{i+1}')
#13. Write a Python script that reads a large text file line by line using a generator function.
def generatoreg(genfile):
    with open(genfile,'r') as fileread:
        readfile=fileread.readlines()
        yield readfile
genfile="sample1.txt"
results=generatoreg(genfile)
for result in results:
    print(result)

# 14. Write a program to find and replace a word in a text file.
find_word="uk"
replace_word="coventry"
with open("sample1.txt",'r') as fileread:
    readfiles=fileread.readlines()
    for readline in readfiles:
        if find_word in readline:
            replacedline=readline.replace(find_word,replace_word)
            print(replacedline)
# 15. Write a Python script that copies contents from one file to another.
with open("sample1.txt",'r') as input,open("copiedfile.txt",'w') as output:
    for line in input:
        output.write(line)

# 17. Modify the script to count the frequency of each word in the file.
filedict={}
with open("sample1.txt",'r') as input:
    file=input.read()
    data =file.split()
    for words in data:
        if words in filedict:
            filedict[words]=filedict[words]+1
        else:
            filedict[words]=1
    print(filedict)
# 19. Write a Python program to merge two text files into a third file.
with open("sample.txt",'r') as first, open("sample1.txt",'r') as second, open("thirdsample.txt",'w+') as third:
    firstfile=first.read()
    secondfile=second.read()
    thirdfile=third.write(firstfile+secondfile)















