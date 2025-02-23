# 6.	Check First and Last Character
# Take a string as input and check whether the first and last characters are the same (ignoring case).

strvalue =input("Enter the string value here:")
firstchar = strvalue[0::]
lastchar = strvalue[::-1]
if firstchar==lastchar:
    print("First and Last character are same")
else:
    print("They are not same")