# Question:Take the user’s name and age as input.
# 	•	If the age is below 18, print: “Hello, [name]. You are a minor.”
# 	•	If the age is between 18 and 60, print: “Hello, [name]. You are an adult.”
# 	•	If the age is above 60, print: “Hello, [name]. You are a senior citizen


Name = input("Enter user's name:")
Age = int(input("Enter user's Age:"))

if (Age <18):
    print(f'Hello,{Name}.You are a minor')
elif(Age>=18) and (Age<=60):
    print(f'Hello,{Name}.You are an adult')
else:
    print(f'Hello,{Name}.You are a senior citizen')