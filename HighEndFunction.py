#1. Write a Python program using map() to square each number in the given list
from functools import reduce

from Feb22.listcomprehension import nested_list
from Learning.Dictionary import mydir

li=[2,5,6,78,9,10,15,20,8,13]
newli=list(map(lambda a:a**2,li))
print(f'List with square:{newli}')
#2. Given a list of lowercase strings, use map() to convert them to uppercase.
strli=['a','g','k','r','t']
strli_upper=list(map(lambda a:a.upper(),strli))
print(f'List with upper case: {strli_upper}')
# 3. Find the length of each word in a list.
wordli=["hello","my","name","kiruthiga","Ganesan","dhruvan"]
word_length=list(map(lambda a:len(a),wordli))
print(f'Length of each word:{word_length}')
#4. extract even numbers from a list.
evenli=list(filter(lambda a:a%2==0,li))
print(f'List of even numbers:{evenli}')
# 5. Find words with length greater than 4.
len4=list(filter(lambda a:len(a)>4,wordli))
print(f'List with length >4 :{len4}')
# 6. Write a function to check if a number is prime and use filter() to extract prime numbers.
def is_prime(num):
    if num%2==0:
        return False
    else:
        return True
prime=list(filter(lambda a:is_prime(a),li))
print(f'Prime numbers:{prime}')
# 7. Sum of all elements in a list.
sumvalue=reduce(lambda a,b:a+b,li)
print(f'Sum of all numbers in the list:{sumvalue}')
#8. Find the maximum number in a list.
maxvalue=reduce(max,li)
print(f'Maxium value from list:{maxvalue}')
#9. Find the product of all elements in a list.
reduceli=[5,6,7,3,2]
product=reduce(lambda a,b:a*b,reduceli)
print(f'Product of all elements:{product}')
#10.Concatenate all strings in a list.
constr=reduce(lambda a,b:a+" "+b,wordli)
print(f'Concate result:{constr}')
# 11. Given a list of numbers, first use map() to square them.
#         Then, use filter() to keep only the even squares.
#         Finally, use reduce() to find the sum of these even squares.
values=[2,3,4,5,6,7,8,9,10,12,13,15]
nestedlist=reduce(lambda x,y:x+y,(list(filter(lambda b:b%2==0,(map(lambda a:a*2,values))))))
print(f'Final value of nested high end function:{nestedlist}')


