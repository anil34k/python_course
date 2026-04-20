print('100'+'200')
# Output: 100200
# print(98+'hello')
# Error: TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(98+True)
# Output: 99 

# assignment operators(=, +=, -=, *=, /=, //=, %=, **=)
a=10
print(a)
# Output: 10

a+=5
print(a)
# Output: 15

a-=3
print(a)
# Output: 12

a*=2
print(a)
# Output: 24

a/=4
print(a)
# Output: 6.0

a//=2
print(a)
# Output: 3

a%=3
print(a)
# Output: 0

a**=2
print(a)
# Output: 0

# logical operators(and, or, not)
x = True
y = False
print(x and y)
# Output: False
print(x or y)
# Output: True
print(not x)
# Output: False

a=98
b=10
print(a > b and b < a)
# Output: True
print(a > b or b > a)
# Output: True
print(a > b or a == b)
# Output: True
print(not a > b)
# Output: False
print(not(a!=b))
# Output: False

x = 100
y = 90
z = 60
print(x > y and y > z and z < x)
# Output: True
print(x > y or y > z or z > x)
# Output: True
print(not x > y and not y > z and z < x)
# Output: False

# membership operators(in, not in)

s1 = "python"
print('p' in s1)
# Output: True

s2 = "education"
print('j' in s2)
# Output: False
print('j' not in s2)
# Output: True

s3 = "python programming in qspiders"
print('python' in s3)
# Output: True
print('PYTHON' in s3)
# Output: False

s4 = 'python'
s5 = 'n'
print(s5 in s4)
# Output: True

list1 = [1, 2, 3, 4, 5]
print(3 in list1)
# Output: True
print(6 in list1)
# Output: False
print(6 not in list1)
# Output: True

# identity operators(is, is not)

a = 98
b = 98
print(id(a))
# Output: <memory address of a>
print(id(b))
# Output: <memory address of b>
print(a is b)
# Output: True
print(a is not b)
# Output: False

s1 = "python"
s2 = "java"
print(s1 is s2)
# Output: False
print(s1 is not s2)
# Output: True

s3 = "python"
s4 = "python"
print(s3 is s4)
# Output: True
print(s3 is not s4)
# Output: False

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1))
# Output: <memory address of list1>
print(id(list2))
# Output: <memory address of list2>
print(list1 is list2)
# Output: False
print(list1 is not list2)
# Output: True

