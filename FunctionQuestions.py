# 1. Write a Python function called greet that takes a name as a parameter and prints out "Hello, <name>!" (e.g., greet("Shruti") should output "Hello, Shruti!").
def greet(name):
    name=name.capitalize()
    print(f'Hello,{name}!')
greet("kiruthiga")
# 2. Write a Python function sum_of_numbers that takes two numbers as arguments and returns their sum
def sumnum(n1,n2):
    return n1+n2
print(f'Sum the values given:{sumnum(3,4)}')
# 3. Write a function calculate_area that calculates the area of a rectangle. It should take two arguments, length and width, with default values of 5 and 10, respectively. If no arguments are passed, it should use these default values.
def calculate_area(l=5,w=10):
    return l*w
print(f'Calculate area with parameters:{calculate_area(2,5)}')
print(f'calculate area with default value:{calculate_area()}')
# 4. Write a function introduce that accepts keyword arguments first_name and last_name and prints out a sentence "My name is Harsh Anand.
def key_eg(fname,lname):
    print(f'My name is {fname} {lname}')
key_eg(fname="Kiruthiga",lname="Ganesan")
# 5. Write a function average that accepts any number of numeric arguments and returns their average. Use the *args syntax.
def getavg(*args):
    return sum(args)/len(args)
print(f'Average of the given numbers:{getavg(4,5,5,6,3,7)}')
# 6. Write a lambda function that takes two arguments and returns their product. Use this lambda function to calculate the product of 4 and 5
res=(lambda a,b:a*b)
print(f'Product calc using lambda:{res(4,5)}')
# 7. Write a recursive Python function to calculate the factorial of a number n (i.e., n! = n * (n-1) * ... * 1)
def factorial(n):
    res=1
    for i in range(n):
        res =res*(i+1)
    print(f'The factorial value is :{res}')
n=int(input("Enter the value to be factored:"))
factorial(n)
# 8. Write a function even_numbers that takes a list of integers and returns a new list containing only the even numbers from the original list, using list comprehension.
li=[4,3,5,6,7,8,9]
newlist=[i for i in li if i%2==0]
print(newlist)
# 9. Write a function that takes a string and returns the string reversed.
def stringreverse(str):
    str1 = " "
    for i in range(len(str)):
        str1+=str[-(i+1)]
    return str1
str = input("Enter the string need to be reversed:")
print(f'The string after reversed:{stringreverse(str)}')
# 10.Create a function that takes a list of numbers and returns a new list with only the odd numbers.
def oddnumbers(numli):
    oddli=[]
    for i in numli:
        if i%2!=0:
            oddli.append(i)
    return oddli
numli=[4,3,5,6,7,8,9]
print(f'The list with odd numbers:{oddnumbers(numli)}')
