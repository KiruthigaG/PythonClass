# 1. Write a Python program to merge two dictionaries. If there are any common keys, their values should be summed.
DictA = {"a": 10, "b": 20}
DictB = {"b": 30, "c": 40}
DictC=DictA.copy()
DictC.update(DictB)
for key in DictA:
    if key in DictB:
        DictC[key]=DictA[key] + DictB[key]
print(DictC)
#  2. Write a Python program to find the key with the highest value in a dictionary.
newdir ={'a': 5, 'b': 10, 'c': 3, 'd': 7}
valuelist=newdir.values()
setvalue = list(valuelist)
setvalue.sort()
newval = setvalue[-1]
largestkey={}
for key in newdir:
    if newdir[key] == newval:
        largestkey[key]=newdir[key]
        print(largestkey)

#3. Write a Python program to remove a key from a dictionary. If the key does not exist, handle it gracefully.
dict1= {'a': 1, 'b': 2, 'c': 3}

dict1.pop('b')
print(dict1)
#Write a Python program to check if a key exists in a dictionary.
dictcheck={'a': 100, 'b': 200}
print('a' in dictcheck)



