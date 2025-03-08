#1. Write a dictionary comprehension that creates a dictionary with even numbers from 1 to 20 as keys, and their squares as values.
newdict={}
newdict={i:i**2 for i in range(1,21) if i%2==0}
print(newdict)
# 2. Given a dictionary {1: 'a', 2: 'b', 3: 'c'}, use dictionary comprehension to swap the keys and values.
dict={1:'a',2:'b',3:'c'}
swapdict={val:key for key,val in dict.items()}
print(swapdict)
# 3. Given a string "interview", use dictionary comprehension to create a dictionary where the keys are the characters and the values are their frequencies in the string.
str ="interview"
strdict={i:str.count(i) for i in str}
print(strdict)
# 4. Given a dictionary {1: 10, 2: 15, 3: 20, 4: 25, 5: 30}, use dictionary comprehension to filter only the keys whose values are even.
numdict={1:10,2:15,3:20,4:25,5:30}
evendict={key:val for key,val in numdict.items() if val%2==0 }
print(evendict)




