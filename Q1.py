# Question:1. Write a Python program that takes two numbers as input and
# asks the user to choose an operation: addition, subtraction, multiplication, or division.
# Perform the operation and display the result


num1 =int(input("Enter the first number:"))
num2 =int(input("Enter the second number:"))

operation = input("Enter the arithmetic operation to be performed:")

match operation:
    case '+':
        result = num1+num2
        print(f'Result for {'+'} operator is {result}')
    case '-':
        result = num1 - num2
        print(f'Result for {'-'} operator is {result}')
    case '*':
        result = num1 * num2
        print(f'Result for {'*'} operator is {result}')
    case '/':
        result = num1 / num2
        print(f'Result for {'/'} operator is {result}')
    case '//':
        result = num1 // num2
        print(f'Result for {'//'} operator is {result}')
    case '**':
        result = num1 ** num2
        print(f'Result for {'**'} operator is {result}')
    case _:
        print("No operations were entered")

