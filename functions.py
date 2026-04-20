# Functions
# Defn: A function in python is a block of code which we can reuse to perform specific task.
# Functions helps to avoid repetition of code & makes the program easy to read, write & maintain.
# Types of functions
# In-built functions
# User-defined functions
# Types of string data type methods in python

# String methods are in-built methods which are used to perform specific operation on strings.

# String methods are used to perform calculation on string values.

# Q) WAP to print in-built methods of string data type
print(dir(str))
# 7) Capitalize method

# This method in python it is used to convert initial first character of string into upper case & remaining all characters into lower case.

# Syntax:
# variable_name.capitalize()
# Eg:
msg = 'hello'
print(msg.capitalize())   # o/p: Hello
msg2 = 'heLLo'
print(msg2.capitalize())  # o/p: Hello

S1 = 'welcome to python'
print(S1.capitalize())     # o/p: Welcome to python
# 2. Upper method:

# This method in python is used to convert all characters of string into upper case.

# Syntax:
# variable_name.upper()
# Eg:
S1 = 'python'
print(S1.upper())      # o/p: PYTHON
S2 = 'python'
result = S2.upper()
print(result)          # o/p: PYTHON
# 3. Lower method

# This method in python is used to convert all characters of string into lower case.

# Syntax:
# variable_name.lower()
# Eg:
S1 = 'JAVA'
print(S1.lower())      # o/p: java
# 4. Swapcase method

# This method in python is used to convert uppercase characters into lowercase & lowercase characters into uppercase.
# Syntax:
# variable_name.swapcase()
# Eg:
msg = 'PyThON class'
result = msg.swapcase()
print(result)      # o/p: pYtHon CLASS
# 5. Count method

# This method is used to find occurrence of substring based on start index & end index.

# Syntax:
# variable_name.count(substring)
# variable_name.count(substring, start_index, end_index)
# Eg:
msg = 'welcome to python'
result = msg.count('o')
print(result)      # o/p: 3
msg = 'welcome to python'
result = msg.count('o', 6)
print(result)      # o/p: 2

# (from start index 6 how many times 'o' appears)

msg = 'welcome to python'
result = msg.count('o', 6, 15)
print(result)      # o/p: 1

# (from start index 6 & end index 15 how many times 'o' appears)

# 6. Index method

# It is used to find index value of first occurrence of substring.

# Syntax:
# variable_name.index(substring)

msg = 'Basavanagudi'
first = msg.index('a')
print(first)        # o/p: 1

# WAP to find index value of second occurrence substring 'a'

msg = 'Basavanagudi'
first = msg.index('a')
second = msg.index('a', first+1)
print(second)       # o/p: 3

# WAP to find index value of third occurrence substring 'a'
msg = 'Basavanagudi'
first = msg.index('a')
second = msg.index('a', first+1)
third = msg.index('a', second+1)
print(third)        # o/p: 5

# Enumerate function

# This function in python is used to loop over a sequence
# It is used to display index value & element together from an collection

# Example:
string = 'python'
for index, ch in enumerate(string):
    print(index, ch)
# o/p:
# 0 P
# 1 Y
# 2 T
# 3 H
# 4 O
# 5 N

# WAP to find position of third occurrence of character 'a'
msg = 'basavanagudi'
count = 0

for i, ch in enumerate(msg):
    if ch == 'a':
        count = count + 1
        if count == 3:
            print(i)
            break

string = 'python'
for index, ch in enumerate(string, start=1):
    print(index, ch)
# o/p:
# 1 p
# 2 y
# 3 t
# 4 h
# 5 o
# 6 n

msg = 'python'
print(msg.index('j'))   # ValueError (substring not found)

# Find() method

# This method in python used to find position of characters (substring)

# Syntax:
# variablename.find(substring)

# Example:
msg = 'python'
print(msg.find('t'))   # 2
print(msg.find('n'))   # 5
print(msg.find('j'))   # -1


# rindex method

# This method in python is used to find occurrence of last substring

# Syntax:
# variablename.rindex(substring)

# Example:
msg = 'python python python'
print(msg.rindex('h'))   # 17

# Replace method

# It is used to replace occurrence of substring with another substring

# Syntax:
# variablename.replace(oldsubstring, newsubstring, count)

# Example:
msg = 'welcome to python'

print(msg.replace('o', '*'))
print(msg.replace('o', '*', 1))
print(msg.replace('o', '*', 2))
print(msg.replace('o', '*', 10))

# startswith

# It is used to check the given string is starts with specified substring, this method will display output in boolean format

# Syntax:
# variablename.startswith(substring)

# Example:
msg = 'python'
print(msg.startswith('p'))   # True
print(msg.startswith('P'))   # False
print(msg.startswith('j'))   # False

# endswith

# It is used to check the given string is endswith specified substring or not. It will display output in boolean format

# Syntax:
# variablename.endswith(substring)

# Example:
msg = 'python'
print(msg.endswith('n'))   # True

msg = 'python'
print(msg.endswith('a'))   # False

# split()

# It is used to divide a string into list

# Syntax:
# variablename.split(substring)

# Example:
msg = 'welcome to python class'
print(msg.split())
print(msg.split('o'))

# WAP program to display extension of file
filename = 'python.txt'
extension = filename.split('.')
print(extension[-1])   # txt

# WAP to display only filename
filename = 'python.txt'
extension = filename.split('.')
print(extension[0])   # python

# WAP to print domain name of a URL
link = 'https://pyspiders.com'
result = link.split('://')
print(result[-1])   # pyspiders.com

# WAP to print protocol of given URL
link = 'https://pyspiders.com'
result = link.split('://')
print(result[0])   # https

# join method

# It is used to concatenate the elements of iterable

# Syntax:
# separator.join(iterable)

# Example:
msg = 'hello python'
result = '*'.join(msg)
print(result)   # h*e*l*l*o* *p*y*t*h*o*n

words = ['hello', 'python']
result = '*'.join(words)
print(result)   # hello*python

# isalpha

# It is used to check all the characters in a string are alphabets or not. It will display output in boolean format

# Syntax:
# variablename.isalpha()

# Example:
msg = 'python'
print(msg.isalpha())   # True

msg = 'python123'
print(msg.isalpha())   # False

# isalnum

# It is used to check characters of string are alphanumeric or not

# Syntax:
# variablename.isalnum()

# Example:
msg = 'python123'
print(msg.isalnum())   # True

msg = 'python'
print(msg.isalnum())   # True

msg = 'python@123'
print(msg.isalnum())   # False

# islower

# It is used to check characters of string are lowercase or not

# Syntax:
# variablename.islower()

# Example:
msg = 'python'
print(msg.islower())   # True

msg = 'Python'
print(msg.islower())   # False

# isupper

# It is used to check characters of string are uppercase or not

# Syntax:
# variablename.isupper()

# Example:
msg = 'PYTHON'
print(msg.isupper())   # True

msg = 'python'
print(msg.isupper())   # False

# isdigit

# It is used to check characters of string are digits or not

# Syntax:
# variablename.isdigit()

# Example:
num = '12345'
print(num.isdigit())   # True

# Methods in list

# append method

# It is used to add new element to the existing list
# By using append method we can add only one element at once

# Syntax:
# variablename.append(new_element)

# Example:
my_list = [10, 20, 30]
my_list.append(98)
print(my_list)   # [10, 20, 30, 98]

lst = []
lst.append('hello')
print(lst)   # ['hello']

# extend method

# It is used to add multiple elements to the existing list

# Syntax:
# variablename.extend(elements)

# Example:
lst = [1, 2, 3]
lst.extend([4, 5, 6])
print(lst)   # [1, 2, 3, 4, 5, 6]

# insert method

# It is used to add new element at a specific position in the list

# Syntax:
# variablename.insert(index, new_element)

# Example:
lst = [10, 20, 30, 40, 50]
lst.insert(3, 98)
print(lst)   # [10, 20, 30, 98, 40, 50]

# count method

# It is used to find the occurrence of element

# Syntax:
# variablename.count(element)

# Example:
lst = [10, 20, 20, 30, 20, 20, 50]
print(lst.count(20))   # 4

# index method

# It is used to find position of first occurrence of specified element

# Syntax:
# variablename.index(element)

# Example:
lst = [10, 20, 30, 20, 20, 50]
first = lst.index(20)
print(first)   # 1

# WAP to find position of second occurrence
lst = [10, 20, 20, 30, 20, 20, 30]

first = lst.index(20)
second = lst.index(20, first + 1)

print(second)   # 2

# reverse method

# It is used to reverse the list elements

# Syntax:
# variablename.reverse()

# Example:
lst = [45, 20, 98]
lst.reverse()
print(lst)   # [98, 20, 45]

# sort method

# It is used to rearrange list elements either in ascending order or descending order

# Ascending:
a = [50, 40, 90, 20]
a.sort()
print(a)   # [20, 40, 50, 90]

# Descending:
a = [50, 40, 90, 20]
a.sort(reverse=True)
print(a)   # [90, 50, 40, 20]

# Based on string length (low to high):
a = ['sql', 'python', 'java']
a.sort(key=len)
print(a)   # ['sql', 'java', 'python']

# Based on string length (high to low):
a = ['sql', 'python', 'java']
a.sort(key=len, reverse=True)
print(a)   # ['python', 'java', 'sql']

# pop method

# It is used to remove last element from list collection
# but we can remove particular element based on index value

# Syntax:
# variablename.pop(index)

# Example:
a = [10, 20, 30, 40]

a.pop()
print(a)

a.pop(2)
print(a)

# remove method

# It is used to remove first occurrence of specified element from given list

# Syntax:
# variablename.remove(element)

# Example:
a = [10, 20, 30, 20, 40]
a.remove(20)
print(a)   # [10, 30, 20, 40]

# clear method

# This method in python it is used to remove all the elements from existing list

# Syntax:
# variablename.clear()

# Example:
a = [10, 20, 30, 40]
a.clear()
print(a)   # []

# WAP to find fourth occurrence position using enumerate
a = [10, 20, 30, 20, 40, 20, 50, 20, 98]

element = 20
count = 0

for index, value in enumerate(a):
    if value == element:
        count = count + 1
        if count == 4:
            print(index)
            break

# WAP to find 3rd highest element
data = [10, 20, 30, 20, 40, 20, 50, 20, 98]

numbers = list(set(data))
numbers.sort(reverse=True)

for index, value in enumerate(numbers, start=1):
    if index == 3:
        print(value)
        break

# WAP to find second lowest element
data = [10, 20, 30, 20, 40, 20, 50, 20, 98]

numbers = list(set(data))
numbers.sort()

for index, value in enumerate(numbers, start=1):
    if index == 2:
        print(value)
        break

# WAP to separate even & odd numbers
data = [10, 15, 20, 25, 30, 40, 45]

even = []
odd = []

for num in data:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)

# WAP to remove all occurrences of element
nums = [10, 15, 20, 25, 30, 40, 45, 20]

while 20 in nums:
    nums.remove(20)

print(nums)

# WAP to find frequency of each element
nums = [10, 20, 10, 20, 30, 30, 20, 20]

unique = list(set(nums))

for i in unique:
    print(i, nums.count(i))

# Tuple methods in Python

# 1) count method

# This method in python it is use to find occurrence of specified element

# Syntax:
variable_name.count(element)

# Example:
t1 = (10, 20, 30, 20, 30, 20, 90)
print(t1.count(20))   # o/p: 3

# 2) index method

# This method it is use to find position of first occurrence of specified value

# If the element is not present it will give ValueError

# Syntax:
variable_name.index(element)

# Example:
t1 = (10, 20, 30, 20, 30, 20, 90)
print(t1.index(20))   # o/p: 1
t2 = (10, 20, 30, 40)
print(t2.index(700))   # o/p: ValueError

# WAP to find position of 3rd occurrence of specified element

# (using enumerate function)

t1 = (10, 20, 30, 20, 30, 20, 40)

count = 0
num = 20

for i, value in enumerate(t1):
    if value == num:
        count = count + 1
        if count == 3:
            print(i)
            break

# o/p: 5

# Methods in Set Data Type

# 1) add method

# This method it is use to add new element to the existing set collection

# Syntax:
variable_name.add(element)

# Example:
s1 = {'balaji', 'jeevan'}
s1.add('chethan')
print(s1)   # o/p: {'balaji', 'chethan', 'jeevan'}

# 2) remove method

# This method it is use to remove specified element from an existing set collection

# Syntax:
variable_name.remove(element)

# Example:
s1 = {'balaji', 'jeevan'}
s1.remove('balaji')
print(s1)   # o/p: {'jeevan'}

# 3) update method

# This method it is use to add elements of one collection into another collection

# Syntax:
variable_name.update(iterable)

# Example:
s1 = {1, 2, 3}
s2 = {3, 4, 5, 6, 7}

s1.update(s2)
print(s1)   # o/p: {1, 2, 3, 4, 5, 6, 7}

# 4) pop method

# This method in python it is use to remove random element from set collection

# Set is unordered collection so we can't predict which element will be removed

# Syntax:
variable_name.pop()

# Example:
s1 = {10, 20, 30, 40}
s1.pop()
print(s1)   # o/p: random element removed

# 5) clear method

# This method it is use to remove all the elements from set collection

# Syntax:
variable_name.clear()

# Example:
s1 = {10, 20, 30}
s1.clear()
print(s1)   # o/p: set()

# 6) union method

# This function in python it is use to display matched & unmatched elements from both iterables

# Syntax:
variable_name.union(iterable)

# Example:
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6, 7}

res = s1.union(s2)
print(res)   # o/p: {1, 2, 3, 4, 5, 6, 7}

# 7) intersection method

# This function in python it is used to display matched elements from both iterable

# Syntax:
variable_name.intersection(iterable)

# Example:
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6, 7}

res = s1.intersection(s2)
print(res)   # o/p: {3, 4}

# 8) difference method

# This function in python it will display un-matched elements only from first iterable

# Syntax:
variable_name.difference(iterable)

# Example:
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6, 7}

print(s1.difference(s2))   # o/p: {1, 2}

# 9) symmetric difference method

# This function in python it is used to display unmatched elements from both set collection

# Syntax:
variable_name.symmetric_difference(iterable)

# Example:
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6, 7}

print(s1.symmetric_difference(s2))   # o/p: {1, 2, 5, 6, 7}

# Dictionary Data Type Methods

# 1) get method

# This method in python it is use to get the value of specified key

# Syntax:
variable_name.get(key)

# Example:
d1 = {'ename': 'smith', 'sal': 9000}
print(d1.get('ename'))   # o/p: smith


# Dictionary data type methods

# 1) get method

# This method is used to get the value of specified key

# Syntax:

variable_name.get(key)

# Example:

data = {'ename': 'smith', 'salary': 98000}
print(data.get('ename'))

# o/p:
smith

print(data.get('job'))

# o/p: None

# 2) update method

# This method is used to add new key-value pair & it is used to update values of existing keys

# Syntax:

variable_name.update({'key': value})

# Example:

data = {'ename': 'smith', 'salary': 98000}

data.update({'job': 'analyst'})
print(data)

# o/p:
{'ename': 'smith', 'salary': 98000, 'job': 'analyst'}

data.update({'salary': 99500})
print(data)

# o/p:
{'ename': 'smith', 'salary': 99500}

data.update({'salary': 98600})

# o/p:
{'ename': 'smith', 'salary': 98600}

# 3) items method

# This method is used to display key-value pairs as tuple

# Syntax:

variable_name.items()

# Example:

data = {'ename': 'smith', 'salary': 98000}
print(data.items())

# o/p:
dict_items([('ename', 'smith'), ('salary', 98000)])

# 4) keys method

# This method is used to display all the keys from dictionary collection

# Syntax:

variable_name.keys()

# Example:

data = {'ename': 'smith', 'salary': 98000}
print(data.keys())

# o/p:
dict_keys(['ename', 'salary'])

# 5) values method

# This method is used to display only values from dictionary collection

# Syntax:

variable_name.values()

# Example:

data = {'ename': 'smith', 'salary': 98000}
print(data.values())

# o/p:
dict_values(['smith', 98000])

# 6) pop method

# This method is used to remove specified key from dictionary collection

# Syntax:

variable_name.pop(key)

# Example:

data = {'ename': 'smith', 'salary': 98000}
data.pop('salary')
print(data)

# o/p:
{'ename': 'smith'}

# 7) popitem method

# This method is used to remove last inserted key value pairs

# Syntax:

variable_name.popitem()

# Example:

data = {'ename': 'smith', 'salary': 98000}
data.popitem()
print(data)

# o/p:
{'ename': 'smith'}

# 8) clear method

# This is used to remove all key value pairs from dictionary collection

# Syntax:

variable_name.clear()

# Example:

data = {'ename': 'smith', 'salary': 98000}
data.clear()
print(data)

# o/p:
# {}