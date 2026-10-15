import json

notebook_path = r'C:\Users\anilk\Desktop\Qspiders\python\Python_WAP_All_Questions.ipynb'

all_questions = [
    # 1 to 21
    {
        "num": 1,
        "title": "WAP to check whether a given value is positive or negative or neutral. if positive, display the positive with value.or negative display the negative with value or else display the neutral with value.",
        "code": """# Write your solution here
num = int(input("Enter a number: "))
if num > 0:
    print(f'positive {num}')
elif num < 0:
    print(f'negative {num}')
else:
    print(f'neutral {num}')"""
    },
    {
        "num": 2,
        "title": "WAP to find out the greatest of three numbers.",
        "code": """# Write your solution here
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Greatest number is:", num2)
else:
    print("Greatest number is:", num3)"""
    },
    {
        "num": 3,
        "title": "Write a program to check whether a given number is divisible by 3 and 5. if the number divisible by 3 print fizz, if the number divisible by 5 print buzz if it is divisible by both then print fizzbuzz",
        "code": """# Write your solution here
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print('fizzbuzz')
elif num % 3 == 0:
    print('fizz')
elif num % 5 == 0:
    print('buzz')
else:
    print('invalid')"""
    },
    {
        "num": 4,
        "title": "WAP to find out the relationship between two values and display the relationship.",
        "code": """# Write your solution here
num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)"""
    },
    {
        "num": 5,
        "title": "Write a program to check if a given number is one digit or two digit or three digit for more than 3 digit, if one digit displays the one digit value, if two digit displays the two digit value and so on..",
        "code": """# Write your solution here
num1 = int(input("Enter a number: "))
num = str(abs(num1))
if len(num) == 1:
    print(f'one digit {num1}')
elif len(num) == 2:
    print(f'two digit {num1}')
elif len(num) == 3:
    print(f'three digit {num1}')
else:
    print(f'more than 3 digit {num1}')"""
    },
    {
        "num": 6,
        "title": "WAP to check whether a given character is an alphabet or ascii number or special character or invalid. if alphabet, display the alphabet with character.or elif ascii number display the ascii number with character,or else display the special character with character.",
        "code": """# Write your solution here
ch = input("Enter a character: ")
if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print(f"alphabet {ch}")
elif '0' <= ch <= '9':
    print(f"ascii number {ch}")
else:
    print(f"special character {ch}")"""
    },
    {
        "num": 7,
        "title": "WAP to accept any number from 1-5 and display that number in word form.",
        "code": """# Write your solution here
num = int(input("Enter a number (1-5): "))
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
else:
    print("Invalid number")"""
    },
    {
        "num": 8,
        "title": "WAP to check whether the given input character is uppercase, lowercase, number or special symbol.",
        "code": """# Write your solution here
ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print(f"{ch} is an Uppercase alphabet")
elif 'a' <= ch <= 'z':
    print(f"{ch} is a Lowercase alphabet")
elif '0' <= ch <= '9':
    print(f"{ch} is a Number")
else:
    print(f"{ch} is a Special symbol")"""
    },
    {
        "num": 9,
        "title": "WAP to check whether a given character is uppercase or lowercase or special character.",
        "code": """# Write your solution here
ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print(f"{ch} is an Uppercase alphabet")
elif 'a' <= ch <= 'z':
    print(f"{ch} is a Lowercase alphabet")
else:
    print(f"{ch} is a Special character")"""
    },
    {
        "num": 10,
        "title": "WAP to check whether the given character is lowercase or uppercase, numeric or special characters.",
        "code": """# Write your solution here
ch = input("Enter a character: ")
if 'a' <= ch <= 'z':
    print(f"{ch} is Lowercase")
elif 'A' <= ch <= 'Z':
    print(f"{ch} is Uppercase")
elif '0' <= ch <= '9':
    print(f"{ch} is Numeric")
else:
    print(f"{ch} is a Special character")"""
    },
    {
        "num": 11,
        "title": "WAP to check whether a given percentage is which grade.",
        "code": """# Write your solution here
percentage = float(input("Enter percentage: "))
if percentage >= 90 and percentage <= 100:
    print("Grade A+ (Distinction)")
elif percentage >= 75 and percentage < 90:
    print("Grade A (First Class)")
elif percentage >= 60 and percentage < 75:
    print("Grade B (Second Class)")
elif percentage >= 35 and percentage < 60:
    print("Grade C (Pass)")
elif percentage >= 0 and percentage < 35:
    print("Fail")
else:
    print("Invalid percentage")"""
    },
    {
        "num": 12,
        "title": "WAP to perform arithmetic operations depending on user choice.",
        "code": """# Write your solution here
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
choice = input("Enter operation (+, -, *, /, //, %, **): ")

if choice == '+':
    print(f"Result: {num1} + {num2} = {num1 + num2}")
elif choice == '-':
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif choice == '*':
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif choice == '/':
    if num2 != 0:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero")
elif choice == '//':
    if num2 != 0:
        print(f"Result: {num1} // {num2} = {num1 // num2}")
    else:
        print("Error: Floor division by zero")
elif choice == '%':
    if num2 != 0:
        print(f"Result: {num1} % {num2} = {num1 % num2}")
    else:
        print("Error: Modulo by zero")
elif choice == '**':
    print(f"Result: {num1} ** {num2} = {num1 ** num2}")
else:
    print("Invalid operation choice")"""
    },
    {
        "num": 13,
        "title": "WAP to check a given number is one digit or two digit or three digits.",
        "code": """# Write your solution here
num = int(input("Enter a number: "))
val = abs(num)
if 0 <= val <= 9:
    print(f"{num} is a One-digit number")
elif 10 <= val <= 99:
    print(f"{num} is a Two-digit number")
elif 100 <= val <= 999:
    print(f"{num} is a Three-digit number")
else:
    print(f"{num} has more than three digits")"""
    },
    {
        "num": 14,
        "title": "WAP to check whether a given collection is list, tuple, set or string.",
        "code": """# Write your solution here
coll = eval(input("Enter a collection: "))
if type(coll) == list:
    print(f"{coll} is a List")
elif type(coll) == tuple:
    print(f"{coll} is a Tuple")
elif type(coll) == set:
    print(f"{coll} is a Set")
elif type(coll) == str:
    print(f"{coll} is a String")
else:
    print(f"{coll} is of other type: {type(coll).__name__}")"""
    },
    {
        "num": 15,
        "title": "WAP to check whether a given value is int, float, string or other.",
        "code": """# Write your solution here
val = eval(input("Enter a value: "))
if type(val) == int:
    print(f"{val} is an Integer")
elif type(val) == float:
    print(f"{val} is a Float")
elif type(val) == str:
    print(f"{val} is a String")
else:
    print(f"{val} is of other type: {type(val).__name__}")"""
    },
    {
        "num": 16,
        "title": "WAP to check whether the given character is uppercase or ascii number.",
        "code": """# Write your solution here
ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print(f"{ch} is an Uppercase alphabet (ASCII: {ord(ch)})")
elif '0' <= ch <= '9':
    print(f"{ch} is an ASCII number (ASCII: {ord(ch)})")
else:
    print(f"{ch} is neither uppercase nor an ASCII number")"""
    },
    {
        "num": 17,
        "title": "Nested IF: even/odd with extra conditions.",
        "code": """# Write your solution here
# Nested IF: Check if number is even or odd, then perform nested checks
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
    if num % 4 == 0:
        print(f"{num} is divisible by 4, Cube: {num ** 3}")
    else:
        print(f"{num} is not divisible by 4, Square: {num ** 2}")
else:
    print(f"{num} is Odd")
    if num % 3 == 0:
        print(f"{num} is divisible by 3, Cube: {num ** 3}")
    else:
        print(f"{num} is not divisible by 3, Square: {num ** 2}")"""
    },
    {
        "num": 18,
        "title": "WAP to check alphabet present in collection and case conversion.",
        "code": """# Write your solution here
# WAP to check alphabet present in collection and case conversion
ch = input("Enter an alphabet: ")
coll = input("Enter a collection (string): ")

if (('A' <= ch <= 'Z') or ('a' <= ch <= 'z')) and ch in coll:
    print(f"'{ch}' is present in '{coll}'")
    if 'A' <= ch <= 'Z':
        converted = ch.lower()
        print(f"Converted uppercase '{ch}' to lowercase: '{converted}'")
    elif 'a' <= ch <= 'z':
        converted = ch.upper()
        print(f"Converted lowercase '{ch}' to uppercase: '{converted}'")
else:
    print(f"'{ch}' is either not an alphabet or not present in the collection")"""
    },
    {
        "num": 19,
        "title": "WAP to check character present in string and even/odd index slicing.",
        "code": """# Write your solution here
# WAP to check character present in string and perform slicing
st = input("Enter a string: ")
ch = input("Enter a character: ")

if ch in st:
    idx = st.index(ch)
    print(f"'{ch}' found at index {idx}")
    if idx % 2 == 0:
        print(f"Index is even. Even-indexed elements: {st[::2]}")
    else:
        print(f"Index is odd. Odd-indexed elements: {st[1::2]}")
else:
    print(f"'{ch}' is not present in the string '{st}'")"""
    },
    {
        "num": 20,
        "title": "WAP to check whether a character is alphabet and nested conditions.",
        "code": """# Write your solution here
# WAP to check whether a character is alphabet and apply nested conditions
ch = input("Enter a character: ")

if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print(f"'{ch}' is an Alphabet")
    if 'A' <= ch <= 'Z':
        print(f"'{ch}' is Uppercase")
        if ch in 'AEIOU':
            print(f"'{ch}' is an Uppercase Vowel, ASCII: {ord(ch)}")
        else:
            print(f"'{ch}' is an Uppercase Consonant, Lowercase: {ch.lower()}")
    else:
        print(f"'{ch}' is Lowercase")
        if ch in 'aeiou':
            print(f"'{ch}' is a Lowercase Vowel, ASCII: {ord(ch)}")
        else:
            print(f"'{ch}' is a Lowercase Consonant, Uppercase: {ch.upper()}")
else:
    print(f"'{ch}' is Not an alphabet")
    if '0' <= ch <= '9':
        print(f"'{ch}' is a Number/Digit, ASCII: {ord(ch)}")
    else:
        print(f"'{ch}' is a Special character, ASCII: {ord(ch)}")"""
    },
    {
        "num": 21,
        "title": "WAP to check whether given value is primitive or non primitive.",
        "code": """# Write your solution here
# WAP to check whether given value is primitive or non primitive
val = eval(input("Enter a value: "))

primitive_types = (int, float, complex, bool, type(None))
non_primitive_types = (str, list, tuple, set, dict, bytes, bytearray, frozenset)

if type(val) in primitive_types:
    print(f"{val} ({type(val).__name__}) is a Primitive (Single-value) Data Type")
elif type(val) in non_primitive_types:
    print(f"{val} ({type(val).__name__}) is a Non-Primitive (Collection/Multi-value) Data Type")
else:
    print(f"{val} is of type {type(val).__name__}")"""
    },
    # 22 to 28 (from difficult question.ipynb)
    {
        "num": 22,
        "title": "WAP to check whether a given value is less than 125 and in between 47 to 125 or not. if condition is True, to perform store the given value as key and value as a character into the dict.or else to append the value in list and display it.",
        "code": """# Write your solution here
num = int(input("Enter a number: "))
char_dict = {}
char_list = []

if 47 <= num < 125:
    char_dict[num] = chr(num)
    print("Dictionary:", char_dict)
else:
    char_list.append(num)
    print("List:", char_list)"""
    },
    {
        "num": 23,
        "title": "WAP to take the input from the user as a number and check whether it is a number or not. if yes. take the number and add some value and print it.",
        "code": """# Write your solution here
val = input("Please type in a number: ")
if '0' <= val <= '9' or val.isdigit():
    num = int(val)
    print("Result after adding 3:", num + 3)
else:
    print(f"'{val}' is not a number")"""
    },
    {
        "num": 24,
        "title": "WAP to check whether the given value's last digit is greater than 5 or not.if greater, to perform the bitwise right shift operator (skipping value is 2)",
        "code": """# Write your solution here
num = int(input('Enter a number: '))
if (abs(num) % 10) > 5:
    result = num >> 2
    print("Result after bitwise right shift by 2:", result)
else:
    print("Last digit is not greater than 5")"""
    },
    {
        "num": 25,
        "title": "WAP to check whether a given value is less than 125 and greater than 60 or not. If the condition is satisfied, take the name and extract the middle character and display it.",
        "code": """# Write your solution here
num = int(input('Enter a number: '))
if 60 < num < 125:
    name = input('Enter a name: ')
    middle_char = name[len(name) // 2]
    print("Middle character:", middle_char)
else:
    print(f"{num} is not between 60 and 125")"""
    },
    {
        "num": 26,
        "title": "WAP to check whether a character is in the alphabet or not. If the alphabet, store the value inside the dict(key as a character and value as an ascii value).",
        "code": """# Write your solution here
ch = input("Enter a character: ")
if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    res_dict = {ch: ord(ch)}
    print(res_dict)
else:
    print(f"'{ch}' is not an alphabet")"""
    },
    {
        "num": 27,
        "title": "WAP to check whether a character is in the uppercase or not. If the uppercase, convert to lowercase and store the value inside the dict(character as a key and ascii value as a value).",
        "code": """# Write your solution here
ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    ch_low = ch.lower()
    ch_dict = {ch_low: ord(ch_low)}
    print(ch_dict)
else:
    print(f"'{ch}' is not an uppercase character")"""
    },
    {
        "num": 28,
        "title": "WAP to check whether a character is in the vowel or not. If the vowel,print the next character.",
        "code": """# Write your solution here
char = input("Enter a character: ")
if char in 'aeiouAEIOU':
    next_char = chr(ord(char) + 1)
    print("Next character:", next_char)
else:
    print(f"'{char}' is not a vowel")"""
    },
    # 29 to 46 (OOP & Extra logic questions)
    {
        "num": 29,
        "title": "WAP to print numbers which are divisible by 5 and 7 from 1 to 20.",
        "code": """# Write your solution here
# Using while loop
print("--- Using While Loop ---")
num = 1
while num <= 20:
    if num % 5 == 0 and num % 7 == 0:
        print(num)
    num += 1

print()

# Using for loop
print("--- Using For Loop ---")
for i in range(1, 21):
    if i % 5 == 0 and i % 7 == 0:
        print(i)"""
    },
    {
        "num": 30,
        "title": "WAP to find second greatest number among 3 numbers.",
        "code": """# Write your solution here
# Input three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Method 1: Using conditional statements
if (a >= b and a <= c) or (a <= b and a >= c):
    second_greatest = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    second_greatest = b
else:
    second_greatest = c

print(f"The second greatest number is: {second_greatest}")

# Method 2: Using list sort
numbers = [a, b, c]
numbers.sort()
print(f"The second greatest number (using sort) is: {numbers[1]}")"""
    },
    {
        "num": 31,
        "title": "WAP to print multiplication table of a given number (num = 5).",
        "code": """# Write your solution here
# Using while loop
num = 5
i = 1
print(f"--- Multiplication Table of {num} (While Loop) ---")
while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1

print()

# Using for loop
print(f"--- Multiplication Table of {num} (For Loop) ---")
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")"""
    },
    {
        "num": 32,
        "title": "Example for encapsulation with private variable and private method.",
        "code": """# Write your solution here
# Example for Private Access modifier

class Bank:
    def __init__(self, name, balance):
        self.__name = name        # Private variable
        self.__balance = balance  # Private variable

    def __showdetails(self):       # Private method
        print(f"Name: {self.__name}, Balance: {self.__balance}")

class Customer(Bank):
    def display(self):
        # Trying to access private method from subclass
        try:
            self.__showdetails()
        except AttributeError as e:
            print("Error:", e)

# Creating object
obj = Customer('smith', 98000)
obj.display()

# Accessing private variable outside the class
try:
    print(obj.__balance)
except AttributeError as e:
    print("Error:", e)

# Accessing private variable outside the class using name mangling
print("Accessed via name mangling:", obj._Bank__balance)   # Output: 98000"""
    },
    {
        "num": 33,
        "title": "Example for encapsulation with getters and setters.",
        "code": """# Write your solution here
class Employee:
    def __init__(self, empno, ename, salary):
        self.empno = empno        # Public variable
        self.ename = ename        # Public variable
        self.__salary = salary    # Private variable (data hiding)

    # Getter method
    def get_salary(self):
        return self.__salary

    # Setter method
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary must be greater than zero")

# Example usage
e = Employee(7839, "Smith", 800)

print(f"Employee No: {e.empno}")
print(f"Employee Name: {e.ename}")

# Accessing private variable using getter
print(f"Employee Salary: {e.get_salary()}")

# Updating private variable using setter
e.set_salary(98000)
print(f"Updated Salary: {e.get_salary()}")

# Trying to set invalid salary
e.set_salary(-500)   # Will print error message"""
    },
    {
        "num": 34,
        "title": "Example for runtime polymorphism (Method Overriding).",
        "code": """# Write your solution here
class Parent:
    def display(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

# Runtime polymorphism
obj1 = Parent()
obj2 = Child()

obj1.display()   # Output: This is Parent class
obj2.display()   # Output: This is Child class"""
    },
    {
        "num": 35,
        "title": "Example for method overriding using super() keyword.",
        "code": """# Write your solution here
class Parent:
    def display(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        super().display()   # Call parent method
        print("This is Child class")

obj = Child()
obj.display()

# Output:
# This is Parent class
# This is Child class"""
    },
    {
        "num": 36,
        "title": "Example for class and instance variables.",
        "code": """# Write your solution here
class Employee:
    # Class Variable (Static)
    company_name = "Techcorp" 

    def __init__(self, ename, job):
        # Instance Variables
        self.ename = ename 
        self.job = job

    def display(self):
        print(f"Name: {self.ename}, Job: {self.job}, Company: {Employee.company_name}")

# Creating separate objects with unique instance data
emp1 = Employee("Smith", "Manager")
emp2 = Employee("Martin", "Salesman")

emp1.display() # Output: Name: Smith, Job: Manager, Company: Techcorp
emp2.display() # Output: Name: Martin, Job: Salesman, Company: Techcorp"""
    },
    {
        "num": 37,
        "title": "Example for multiple inheritance using MRO (Method Resolution Order).",
        "code": """# Write your solution here
# WAP to create same method name in multiple classes

class A:
    def display(self):
        print("class A")

class B:
    def display(self):
        print("class B")

class C(B, A):   # Multiple inheritance
    def display(self):
        print("class C")

# Object of C
obj = C()
obj.display()   # Output: class C

# Method Resolution Order (MRO)
print("MRO:", C.__mro__)
# Output: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)"""
    },
    {
        "num": 38,
        "title": "Example for method overloading using *args and **kwargs.",
        "code": """# Write your solution here
class Calculator:
    # Method that can handle addition with variable positional arguments
    def add(self, *args):
        return sum(args)
    
    # Method that can handle operations with keyword arguments
    def calculate(self, operation, **kwargs):
        if operation == 'add':
            return sum(kwargs.values())
        elif operation == 'multiply':
            result = 1
            for value in kwargs.values():
                result *= value
            return result
        else:
            return "Unsupported operation"

# Usage
calc = Calculator()

# Using *args for positional arguments
print("Sum of 2 args:", calc.add(10, 20))          # Output: 30
print("Sum of 5 args:", calc.add(1, 2, 3, 4, 5))   # Output: 15

# Using **kwargs for keyword arguments
print("Calculate add:", calc.calculate('add', a=10, b=20, c=30))      # Output: 60
print("Calculate multiply:", calc.calculate('multiply', x=2, y=3, z=4))    # Output: 24"""
    },
    {
        "num": 39,
        "title": "What is static method? Explain with an example.",
        "code": """# Write your solution here
# Static Method: A static method is a method that belongs to the class rather than an instance of the class. 
# It does not require an instance to be called and does not have access to instance variables (self) or class variables (cls). 
# Static methods are defined using the @staticmethod decorator.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Usage
print("Static add:", MathUtils.add(10, 20))            # Output: 30 
print("Static multiply:", MathUtils.multiply(10, 20))  # Output: 200"""
    },
    {
        "num": 40,
        "title": "WAP to check if first char is special symbol: display the mid char, else reverse the string.",
        "code": """# Write your solution here
# If first char is special symbol display the mid char else reverse and show

st = input("Enter a string: ")

if st:
    first_char = st[0]
    # Check if first character is a special symbol (not alphanumeric)
    if not (('A' <= first_char <= 'Z') or ('a' <= first_char <= 'z') or ('0' <= first_char <= '9')):
        mid_idx = len(st) // 2
        print(f"First character '{first_char}' is a special symbol. Middle character: '{st[mid_idx]}'")
    else:
        print(f"First character '{first_char}' is alphanumeric. Reversed string: '{st[::-1]}'")
else:
    print("String is empty")"""
    },
    {
        "num": 41,
        "title": "Explain class method with an example.",
        "code": """# Write your solution here
# Class Method: A class method is a method that is bound to the class and not the instance. 
# It can access and modify class variables but not instance variables. 
# Class methods are defined using the @classmethod decorator and take 'cls' as the first parameter.

class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

# Usage
emp = Employee("John")
print("Before change:", emp.company)  # Output: TechCorp

Employee.change_company("NewCorp")
print("After change:", emp.company)   # Output: NewCorp"""
    },
    {
        "num": 42,
        "title": "Example for multi-level inheritance using constructor chaining and method chaining.",
        "code": """# Write your solution here
class A:
    def __init__(self):
        print("Constructor of A")

    def method_a(self):
        print("Method of A")
        return self  # Return self for method chaining

class B(A):
    def __init__(self):
        super().__init__()  # Constructor chaining
        print("Constructor of B")

    def method_b(self):
        print("Method of B")
        return self  # Return self for method chaining

class C(B):
    def __init__(self):
        super().__init__()  # Constructor chaining
        print("Constructor of C")

    def method_c(self):
        print("Method of C")
        return self  # Return self for method chaining

# Creating object of class C
print("--- Constructor Chaining ---")
obj = C()

print()
print("--- Method Chaining ---")
obj.method_a().method_b().method_c()"""
    },
    {
        "num": 43,
        "title": "Example for constructor overloading (simulated using default arguments).",
        "code": """# Write your solution here
# Python doesn't support constructor overloading directly like other languages.
# Instead, use default arguments to simulate overloading.

class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

# Usage
p1 = Person("John")        # Uses default age 18
p2 = Person("Jane", 25)    # Overrides age

print(f"{p1.name} is {p1.age} years old")  # Output: John is 18 years old
print(f"{p2.name} is {p2.age} years old")  # Output: Jane is 25 years old

class Employee:
    def __init__(self, name, salary=50000):
        self.name = name
        self.salary = salary

# Usage
e1 = Employee("Smith")           # Default salary
e2 = Employee("Martin", 60000)   # Custom salary

print(f"{e1.name} earns ${e1.salary}")  # Output: Smith earns $50000
print(f"{e2.name} earns ${e2.salary}")  # Output: Martin earns $60000"""
    },
    {
        "num": 44,
        "title": "Example for abstract class with multiple methods.",
        "code": """# Write your solution here
from abc import ABC, abstractmethod

# Abstract Class with multiple abstract methods
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

# Concrete Class implementing all abstract methods
class Car(Vehicle):
    def start(self):
        print('Car starts with key')

    def stop(self):
        print('Car stops with brake')

    def fuel_type(self):
        print('Car uses petrol')

# Usage
obj = Car()
obj.start()     # Output: Car starts with key
obj.stop()      # Output: Car stops with brake
obj.fuel_type() # Output: Car uses petrol"""
    },
    {
        "num": 45,
        "title": "WAP to create online shopping cart using encapsulation.",
        "code": """# Write your solution here
class ShoppingCart:
    def __init__(self):
        self.__items = []  # Private list of items
        self.__total = 0.0  # Private total price

    # Getter for items
    def get_items(self):
        return self.__items.copy()  # Return a copy to prevent external modification

    # Getter for total
    def get_total(self):
        return self.__total

    # Method to add item (encapsulated)
    def add_item(self, item_name, price):
        if price > 0:
            self.__items.append({"name": item_name, "price": price})
            self.__total += price
            print(f"Added {item_name} for ${price}")
        else:
            print("Invalid price")

    # Method to remove item (encapsulated)
    def remove_item(self, item_name):
        for item in self.__items:
            if item["name"] == item_name:
                self.__items.remove(item)
                self.__total -= item["price"]
                print(f"Removed {item_name}")
                return
        print(f"Item {item_name} not found")

    # Method to display cart (encapsulated)
    def display_cart(self):
        if not self.__items:
            print("Cart is empty")
        else:
            print("Items in cart:")
            for item in self.__items:
                print(f"- {item['name']}: ${item['price']}")
            print(f"Total: ${self.__total}")

# Usage
cart = ShoppingCart()
cart.add_item("Laptop", 1000)
cart.add_item("Mouse", 50)
cart.display_cart()
cart.remove_item("Mouse")
cart.display_cart()"""
    },
    {
        "num": 46,
        "title": "Example for bank system with transaction using encapsulation and file handling.",
        "code": """# Write your solution here
class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0.0
        self.__transactions = []
        self.load_data()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(f"Deposited ${amount}")
            self.save_data()
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Withdrew ${amount}")
            self.save_data()
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount")

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions.copy()

    def save_data(self):
        with open(f"{self.__account_number}_balance.txt", "w") as f:
            f.write(str(self.__balance))
        with open(f"{self.__account_number}_transactions.txt", "w") as f:
            for t in self.__transactions:
                f.write(t + "\\n")

    def load_data(self):
        try:
            with open(f"{self.__account_number}_balance.txt", "r") as f:
                self.__balance = float(f.read().strip())
            with open(f"{self.__account_number}_transactions.txt", "r") as f:
                self.__transactions = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            pass  # No data yet

# Usage
account = BankAccount("12345")
account.deposit(1000)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")
print("Transactions:", account.get_transactions())"""
    }
]

cells = []
for q in all_questions:
    idx = len(cells)
    
    # Markdown cell
    md_text = f"## Question {q['num']}\n{q['title']}"
    md_lines = [l + '\n' for l in md_text.split('\n')]
    if md_lines:
        md_lines[-1] = md_lines[-1].rstrip('\n')
        
    md_cell = {
        "cell_type": "markdown",
        "id": f"cell_{idx:03d}_markdown",
        "metadata": {},
        "source": md_lines
    }
    
    # Code cell
    code_lines = [l + '\n' for l in q['code'].split('\n')]
    if code_lines:
        code_lines[-1] = code_lines[-1].rstrip('\n')
        
    code_cell = {
        "cell_type": "code",
        "execution_count": None,
        "id": f"cell_{idx+1:03d}_code",
        "metadata": {},
        "outputs": [],
        "source": code_lines
    }
    
    cells.append(md_cell)
    cells.append(code_cell)

nb_data = {
    "cells": cells,
    "metadata": {
        "language_info": {
            "name": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb_data, f, indent=1, ensure_ascii=False)

print(f"Successfully generated all {len(all_questions)} questions ({len(cells)} total cells) in {notebook_path}!")
