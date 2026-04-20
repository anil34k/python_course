# input statement - used to take input from the user
name = input("Enter your name: ")
print("Hello, " + name)
print(type(name)) # <class 'str'>

# example to get input for integer

age = int(input("Enter your age: "))
print("Your age is: " + str(age))
print(type(age)) # <class 'int'>

# example to get input for float

height = float(input("Enter your height in cm: "))
print("Your height is: " + str(height) + " cm") 
print(type(height)) # <class 'float'>

# example to get input for complex number

complex_number = complex(input("Enter a complex number: "))
print("Your complex number is: " + str(complex_number)) 
print(type(complex_number)) # <class 'complex'>


# print statement - used to display output to the user
print("Hello, World!") # Hello, World!
print("Welcome to Python programming") # Welcome to Python programming

# eval statement - its a built-in function and it is used to dynamically calculate the expression from a string or complied code based on given input
# syntax of eval statement
# varname = eval(input("Enter a value: "))

num = eval(input("Enter a number: "))
print(num) # if user enters 10 then output will be 10
print(type(num)) # <class 'int'> or <class 'float'>

result = eval('2'+'3') # 22
print(result) # 22
print(type(result)) # <class 'str'>

result1 = eval('2 + 2') # 4
print(result1) # 4
print(type(result1)) # <class 'int'>
