# 1.What is a tuple in Python, and how is it different from a list?
    #Tuple is similar to list in creating objects separated by comma using () but it is immutable,
    #once created, the tuple can not be updated with values, removed and extended
#  2. How do you create a tuple in Python?
temp =(2,5,6,7)
print(temp)

# 3. Can you modify the elements of a tuple once it is created? Why or why not?
    # no we can not modify as it is immutable
# 4. How do you access elements in a tuple?
for i in range(0,len(temp)):
    print(temp[i])
#5. How can you convert a tuple into a list and vice versa?

temp1=list(temp)
print(f'Tuple-List: {temp1} and the dataype is {type(temp1)}')
temp=tuple(temp1)
print(f'List-Tuple: {temp} and the dataype is {type(temp)}')

