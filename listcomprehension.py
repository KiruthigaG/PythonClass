#'1.Write a Python program using list comprehension to generate a list of all odd numbers between 1 and 20.

value=[i for i in range(1,21) if i%2!=0]
print(value)

#2. Write a Python program using list comprehension to convert a list of temperatures from Celsius to Fahrenheit.
celsius=[0, 10, 20, 30, 40]
fahrenheit=[i*(9/5)+32 for i in celsius]
print(fahrenheit)

# 3. Write a Python program using list comprehension to flatten a nested list.
nested_list =[[1, 2, 3], [4, 5], [6, 7]]
newlist=[]
newlist.extend(i for lists in nested_list for i in lists)
print(newlist)


