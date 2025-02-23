# 1. How can you reverse a Python list?
list1=[34,56,2,7,8,9,'Apple']
print(f'Before Reversing: {list1}')
list1.reverse()
print(f'After Reversing: {list1}')

# 2. How do you check if an item exists in a Python list?
print(2 in list1)
#   3. What method would you use to concatenate two lists in Python?
list2 =["new","list",2,4,"extend"]
list1.extend(list2)
print(list1)
# 4. How do you find the length of a list in Python?
print(f'Length of the list:{len(list1)}')
# 5. How do you sort a list in Python, and what are the options for sorting (ascending vs descending)?
list3=[4,5,7,89,100,34,23,12,53]
print("Sort in ascending order:")
list3.sort()
print(list3)
print("Sort in descending order:")
list3.sort(reverse=True)
print(list3)
# 6. How would you remove duplicates from a Python list
list4=[2,2,45,6,7,6,8,90,91,90]
print("Display list with duplicates:")
print(list4)
list5 =set(list4)
print("Display list without duplicates:")
print(list5)