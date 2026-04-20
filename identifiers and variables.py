# identifiers are the names given to variables, functions, classes, etc. in Python. They must follow certain rules:
# 1. An identifier can only contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# 2. An identifier cannot start with a digit.
name = 'martin'
print(name)
# Output: martin

age = 25
print(age)
# Output: 25

name_8976 = 'king'
print(name_8976)
# Output: king

#wap to check identifier is valid
name='scott'
print(name.isidentifier())
# Output: True

age=25
print(age.isidentifier())
# Error: AttributeError: 'int' object has no attribute 'isidentifier'

place='bangalore'
print(place.isidentifier())
# Output: True

color='red'
print(color.isidentifier())
# Output: True

# variables

# variables are used to store data in Python. 
# They can hold different types of data, such as numbers, strings, lists, etc. 
# Variables are created by assigning a value to a name using the assignment operator (=).
# Variables can be of different types, such as integers, floats, strings, lists, etc.
# The type of a variable can be determined using the built-in type() function.
# Variables can be reassigned to different values, and they can also be deleted using the del statement.
# Variables can be used in expressions and can be printed to the console using the print() function.
# Variables can also be used to store the result of a calculation or a function call, and they can be used to pass data between different parts of a program.
# Variables are an essential part of programming and are used to store and manipulate data in a program.
# Variables can also be used to store the result of a calculation or a function call, and they can be used to pass data between different parts of a program.
# Variables are an essential part of programming and are used to store and manipulate data in a program.

# single value variable
name = 'martin'
print(name)
# Output: martin
print(type(name))
# Output: <class 'str'>

age = 25
print(age)
# Output: 25
print(type(age))
# Output: <class 'int'>

# double value variable

a,b = 100, 200
print(a,b)
# Output: 100 200
print(a)
# Output: 100
print(b)
# Output: 200
print(c) # this will raise an error because c is not defined
# Error: NameError: name 'c' is not defined

ename, salary = 'smith', 10000
print(ename, salary)
# Output: smith 10000
print(ename)
# Output: smith
print(salary)
# Output: 10000
print(job) # this will raise an error because job is not defined
# Error: NameError: name 'job' is not defined
