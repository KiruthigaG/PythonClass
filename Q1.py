# 1.Write a Python program to swap two variables without using a temporary variable.

# With integer
a=5
b=10
print("Before swapping: ")
print(a,b)
# Swapping action
a,b=b,a
print("After swapping: ")
print(a,b)
# With string
a="Hello"
b="Morning"
print("Before swapping the string:")
print(a,b)
a,b=b,a
print("After swapping the string:")
print(a,b)