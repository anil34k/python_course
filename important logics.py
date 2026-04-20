# write a condition to check number is greater than 5 or not

num = int(input("Enter a number: "))
res = num > 5
print(res)

# write a condition to check last digit of a given character is divisible by 3 or not

num = int(input("Enter a number: "))

last_digit = num % 10
res3 = last_digit % 3 == 0
print(res3)

# write a condition to check the given collection is upper case or not

chr = input("Enter a collection: ")
r = chr >= 'A' and chr <= 'Z'
print(r)