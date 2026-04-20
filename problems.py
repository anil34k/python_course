# wap condition to check number is greater than 5
num1 = int(input())
res1 = num1 > 5
print(res1)

# write a condition to check whether the given number is greater than 10 and less than 20
num1 = int(input())
res = num1 > 10 and num1 < 20
print(res)

# write a condition to check the given number is divisible by 3
num1 = int(input())
res = num1 % 3 == 0
print(res)

# write a condition to check the given number is divisible by 3 and 5
num1 = int(input())
res = num1 % 3 == 0 and num1 % 5 == 0
print(res)

# to check the given condition is uppercase or not
char1 = input()
res = char1>='A' and char1<='Z'
print(res)

# to check the given condition is lowercase or not
char1 = input()
res = char1>='a' and char1<='z'
print(res)

# write a condition to check last digit of the given character is divisible by 3
# char = input()
# res = (ord(char) % 10) % 3 == 0
# print(res)

word = input("Enter a word: ")
print((ord(word[-1]) % 10) % 3 == 0)

# check greatest number
a,b=98,45
if(a>b):
    print(f"{a} is greater than {b}")

# check no. is +ve
if(a>b):
    print(f"{a} is greater than {b}")
print("Program completed")

# TO CHECK the gievn number is even
num1 = int(input())
if num1 % 2 == 0:
    print(f"{num1} is even")
print("Program completed")

# TO CHECK the gievn number is odd
num1 = int(input()) 
if num1 % 2 != 0:
    print(f"{num1} is odd")
print("Program completed")

# given number is divisible by 3
num1 = int(input())
if num1 % 3 == 0:
    print(f"{num1} is divisible by 3")

# given number is divisible 5
num1 = int(input())
if num1 % 5 == 0:
    print(f"{num1} is divisible by 5")

# given number is divisible by 3 and 5
num1 = int(input())
if num1 % 3 == 0 and num1 % 5 == 0:
    print(f"{num1} is divisible by 3 and 5")

# to check the given string is starts with vowel
string1 = input()
if string1[0] in 'AEIOUaeiou':
    print(f"{string1} starts with vowel")

# to check the given string is starts with consonant
string1 = input()
if string1[0] not in 'AEIOUaeiou':
    print(f"{string1} starts with consonant")

# to check the given string is ends with vowel
string1 = input()
if string1[-1] in 'AEIOUaeiou':
    print(f"{string1} ends with vowel")

# to check the given string is ends with consonant
string1 = input()
if string1[-1] not in 'AEIOUaeiou':
    print(f"{string1} ends with consonant")

# to check the given string starts with uppercase
string1 = input()
if 'A' <= string1[0] <= 'Z':
    print(f"{string1} starts with uppercase")

# to check the given string starts with lowercase
string1 = input()
if 'a' <= string1[0] <= 'z':
    print(f"{string1} starts with lowercase")

# to check the given character is digit
char1 = input()
if '0' <= char1 <= '9':
    print(f"{char1} is a digit")

# wap to check the given character is special character
char1 = input()
if not (('A' <= char1 <= 'Z') or ('a' <= char1 <= 'z') or ('0' <= char1 <= '9')):
    print(f"{char1} is a special character")