#    1. Write a Python program to find the union of two sets.
#     Input:
#         Set A: {1, 2, 3, 4}
#         Set B: {3, 4, 5, 6}
SetA= {1, 2, 3, 4}
SetB= {3, 4, 5, 6}
print("Union of SetA and SetB:")
print(SetA.union(SetB))
# 2. Write a Python program to find the intersection of two sets.
print("Intersection of SetA and SetB:")
print(SetA.intersection(SetB))
#3. Write a Python program to find the difference between two sets, i.e., elements that are in Set A but not in Set B.
print("Difference of SetA and SetB:")
print(SetA.difference(SetB))
# 4. Write a Python program to check if one set is a subset of another.
print("Subset of SetA in SetB:")
print(SetA.issubset(SetB))
SetC={4,5}
print("Subset of SetC in SetB:")
print(SetC.issubset(SetB))
