# escape squence and string formating

# escape sequence
# An escape sequence is a combination of characters that represents a special character or a non-printable character in a string.
# It is used to include characters in a string that would otherwise be difficult or impossible to include directly.
# The most common escape sequences are:
# \n - represents a new line
# \t - represents a tab
# \\ - represents a backslash
# \' - represents a single quote
# \" - represents a double quote

print('hello\nworld')
print("Hello\nstudents\nwelcome to python class")

# String formatting
# String formatting is a way to create a new string by inserting values into a template string.
# The most common way to format strings in Python is using f-strings, which are denoted by an 'f' before the opening quote of the string.
# The values to be inserted into the string are enclosed in curly braces {}.

name1 = 'smith'
print(f"hello {name1}")
salary = 10000
print(f"hello {name1} your salary is {salary}")

