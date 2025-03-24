#1. Write a generator function countdown(n) that yields numbers from n to 0
def countdown(n):
    i=0
    for i in range(n):
        while i<=n:
            yield n
            n-=1
for val in countdown(10):
    print(val)
#   2. Create a generator even_numbers(n) that yields the first n even numbers.
def countdown(n):
    i=0
    for i in range(n):
        if i%2==0:
            yield i

for val in countdown(10):
    print(val)
#3. Write a generator function fibonacci(n) that generates the first n Fibonacci numbers.
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        c=a+b
        a=b
        b=c
for val in fibonacci(10):
    print(val)
#4. Create a generator square_numbers(n) that yields the square of numbers from 1 to n.
def square_numbers(n):
    for i in range(n):
        yield i*i

for val in square_numbers(10):
    print(val)
#   5. Write a generator char_generator() that yields each character from a given string one by one.
def char_generator(n):
    for i in n:
        yield i

for val in char_generator("python"):
    print(val)
#    6. Implement a generator prime_numbers(limit) that yields all prime numbers up to limit
def prime_numbers(limit):
    for num in range(2,limit):
        prime = True
        for i in range(2,num):
            if num%i==0:
                prime=False
        if prime:
            yield num

for val in prime_numbers(20):
    print(val)
#7. Modify the Fibonacci generator so that it stops when a number exceeds 1000.
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        c=a+b
        a=b
        b=c
        if(i<=1000):
            continue
        else:
            break
for val in fibonacci(500000):
    print(val)





