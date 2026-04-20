# WAP to find the second greatest number among 3 numbers
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# second_greatest = sorted([a, b, c])[1]
# print(f"The second greatest number is: {second_greatest}")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a>b and a>c:
    if b>c:
        print(f"Second greatest number is {b}")
    else:
        print(f"Second greatest number is {c}")
elif b>a and b>c:
    if a>c:
        print(f"Second greatest number is {a}")
    else:
        print(f"Second greatest number is {c}")
else:
    if a>b:
        print(f"Second greatest number is {a}")
    else:
        print(f"Second greatest number is {b}")

