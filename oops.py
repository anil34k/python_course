# # basic syntax for creating class and object
# class classname:
#     # properties
#     # behaviors
#     # sttaing blocks
# obj = classname()

# wap to create class as employee and access emp name , salary and designation using obj(using class variable)

# class employee ():
#     ename = 'smith'
#     salary = 50000
#     designation = 'developer'
# e1 = employee()
# print(e1.ename)
# print(e1.salary)
# print(e1.designation)

# car example using bject variable 

# class car():
#     pass
# c1 = car()
# c1.name = 'swift'
# c1.price = 600000
# c1.color = 'red'
# c2 = car()
# c2.name = 'baleno'
# c2.price = 800000
# c2.color = 'blue'
# print(f'first car name is {c1.name} and price is {c1.price} and color is {c1.color}')
# print(f'second car name is {c2.name} and price is {c2.price} and color is {c2.color}')

# wap to display caompany name location along with employee name sal and their designation using class variable and object variable

# class employee:
#     # class variables
#     company_name = 'TCS'
#     location = 'hyd' 
#     # object varaiable are created inside method 
# e1 = employee()
# # object variable
# e1.name = 'smith'
# e1.salary = 50000
# e1.designation = 'developer'
# print(f'name {e1.name} , salary {e1.salary} , designation {e1.designation} and company name {e1.company_name} and location {e1.location}')


# wap to create class and access class variable without creating object

# class employee:
#     ename = 'smith'
#     salary = 50000
#     designation = 'developer'

#     def display():
#         print(f'employee name {employee.ename} ')
#         print(f'emp salary {employee.salary} ')
#         print(f'emp designation {employee.designation} ')
# employee.display()
            


# wap to create function inside class and to access class variable using objects

# class student:
#     sname = 'john'
#     age = 20

#     def display(self):
#         print(f'student name {student.sname}')
#         print(f'student age {student.age}')

# s1 = student()
# s1.display()

# example using function as object

# class employee:
#     # class variable
#     dname = 'research'
#     # instance methods
#     def details(self , name ,salary ):
#         # object variables
#         self.name = name
#         self.salary = salary
#     # instance method to display the values of object variables and class variables 
#     def display(self):
#         # to access the class variable we use classname or self
#         print(f'employee name {self.name} and emp salary {self.salary} and emp designation {self.dname}')

# e1 = employee()
# e1.details('smith', 50000)
# e1.display()




# wap to perform checkbalance deposite and withdraw operations

# class bank:
#     bankname = 'icici'
#     # function for details
#     def details(self , cname , balance):
#         self.cname = cname
#         self.balance = balance
#     # deposite function 
#     def deposite(self , amount):
#         self.balance = self.balance + amount
#         print(f'deposited ammount {amount} and current balance {self.balance}')
#     # withdraw function 
#     def withdraw(self , amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print(f'withdraw amount {amount} and current balance {self.balance}')
#         else:
#             print('insufficient balance')
#     # checkbalance function 
#     def checkbalance(self):
#         print(f'current balance {self.balance}')

#     def display(self):
#         print(f'customer name {self.cname} and bank name {self.bankname} and current balance {self.balance}')
            

# c1 = bank()
# c1.details('smith', 50000)
# c1.display()
# c1.deposite(10000)
# c1.withdraw(20000)
# c1.checkbalance()

# c2 = bank()
# c2.details('peter',60000)
# c2.display()
# c2.deposite(20000)
# c2.withdraw(30000)
# c2.checkbalance()






# wap to create class to represnt an employee management system
# 1. the company name should be a class variable 
# 2. each emmployee has name and salary (instance variable)
# 3. create method add salary to increment in salary and display employee name, present salary and increase salary

# class company:
#     company_name = 'TCS'

#     def details(self , name , salary ):
#         self.name = name 
#         self.salary = salary 
#         self.increased_sal = salary 

#     def increased(self , amount):
#         if amount > 0:
#             self.increased_sal = self.increased_sal + amount
#         else:
#             print('invalid amount')

#     def display(self):
#         print(f'employee name {self.name}  ')
#         print(f'emp salary {self.salary} ')
#         print(f' emp increased salary {self.increased_sal}')

# e1 = company()
# e1.details('smith', 50000)
# e1.increased(10000)
# e1.display()
# e2 = company()
# e2.details('peter',60000)
# e2.increased(20000)
# e2.display()
        


# syntax for constructor method 
# class classname:
#     def __init__(self, parameter1, parameter2):
#        self.parameter1 = parameter1
#        self.parameter2 = parameter2
#    def method(self):
    #    block of code
# obj = classname(value1, value2)



# wap to display person name and age by creating constructor

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f'name {self.name} and age {self.age}')

p1 = person('smith',25)
p1.display()
print()
p2 = person('peter',30)
p2.display()
print()


# ==============================================================================
# PAGES 14–24: TRANSCRIPTION FROM HANDWRITTEN NOTES
# ==============================================================================

# 12) WAP to display Employee Name, salary & designation along with their company name using constructor method.
class employee:
    company_name = 'Pyspiders'

    def __init__(self, ename, sal, job):
        self.ename = ename
        self.sal = sal
        self.job = job

    def show_details(self):
        print(f'Employee Name: {self.ename}, and salary is: {self.sal}, and designation is: {self.job} and company name is: {employee.company_name}')

e1 = employee('Smith', 98000, 'Analyst')
e1.show_details()
print()

# 13) WAP to perform banking application scanirio (check balance, deposite, withdraw) using constructor method.
class BankAccount:
    bankname = 'SBI'

    def __init__(self, cname, balance):
        self.cname = cname
        self.balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f'{amount} has been deposited')
            print(f'After deposite, updated bank balance is: {self.balance}')
        else:
            print('Amount must be greater than 0')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f'{amount} has been withdrawn')
            print(f'After withdrawn bank balance is: {self.balance}')
        else:
            print('Insufficient balance')

    def checkbalance(self):
        print(f'Initial Bank Balance: {self.balance}')

c1 = BankAccount('Smith', 5000)
c1.checkbalance()
c1.deposite(1000)
c1.withdraw(500)
print()

# WAP to book ticket in Bookmyshow
# Condition:-
# It should ask theatername then it should display
# the movie available and it has to display ticket price
# and it should ask confirmation to book ticket using
# constructor method.
class BookMyshow:
    def __init__(self, theater_name):
        print("Welcome to Book My Show!")
        self.theater_name = theater_name

        if self.theater_name == 'PVR':
            print("In Movie available at PVR")
            self.movie1 = "Avatar: The way of water"
            self.movie2 = "The Batman"
            self.price1 = 850
            self.price2 = 800
        elif self.theater_name == 'INOX':
            print("In Movie available at INOX")
            self.movie1 = "Mission Impossible"
            self.movie2 = "War"
            self.price1 = 900
            self.price2 = 950
        else:
            print("Sorry, theater not available")
            return

        print(f'1. {self.movie1}')
        print(f'2. {self.movie2}')
        # Using preset inputs for execution to avoid blocking
        # self.movie_choice = "1"
        self.movie_choice = input("\nEnter your movie choice (1 or 2): ")
        self.select_movie()

    def select_movie(self):
        if self.movie_choice == "1":
            self.selected_movie = self.movie1
            self.price = self.price1
        elif self.movie_choice == "2":
            self.selected_movie = self.movie2
            self.price = self.price2
        else:
            print("Invalid choice")
            return

        print(f'\nSelected movie: {self.selected_movie}')
        print(f'\nTicket Price is {self.price}')

        # Using preset inputs for execution to avoid blocking
        # self.confirm = "yes"
        self.confirm = input('\nDo you want to book ticket? (yes/no): ')
        self.confirm_booking()

    def confirm_booking(self):
        if self.confirm == "yes":
            print(f'\nTicket for {self.selected_movie} booked successfully')
        else:
            print("\nBooking cancelled")

theater = input("Enter the name of theater (PVR, INOX): ")
booking = BookMyshow(theater)


# Types of Constructor:-
# (1) Default Constructor
# (2) User-defined Constructor
#     -> Parameter constructor
#     -> Non-parameter raised constructor

# (1) Default Constructor:-
# Whenever user does not explicitly define a constructor within a class,
# then python itself create a constructor internally during compilation
# of the program is called as default constructor.
# WAP to create default constructor and to display employee name & salary.
class employee_default:
    def read(self, ename='smith', salary=98000):
        self.ename = ename
        self.salary = salary

emp1 = employee_default()
emp1.read()
print(f'Employee Name is {emp1.ename} and salary is: {emp1.salary}')
print()
emp2 = employee_default()
emp2.read('Allen', 87000)
print(f'Employee Name is {emp2.ename} and salary is: {emp2.salary}')
print()

# (ii). 1. Parameter raised constructor:-
# In python a parameter raised constructor is a constructor method (__init__)
# that takes arguments, it allows us to initialize object variable
# inside constructor method.
# Example:

class employee_param:
    def __init__(self, name, sal):
        self.name = name  # instance variable
        self.sal = sal    # instance variable

    def display(self):
        print(f'Employee Name: {self.name}')
        print(f'Employee Sal: {self.sal}')

e1 = employee_param('smith', 'manager')
e1.display()
print()

# (ii). 2. Non-parameter raised constructor:-
class employee:
    def __init__(self):  # non parameter constructor
        pass

    def display(self):
        print(f'Employee name is: {self.ename}')
        print(f'Employee dept: {self.dept}')

e1 = employee()
e1.ename = 'Smith'
e1.dept = 10
e1.display()
print()

# Types of variables in oops:-
# (i) Instance Variable
# (ii) Class Variable (Static variable)
# (iii) Local Variables

# (i) Instance Variables:-
# Instance variables are also called as object level variables.
# If the value of variables will be different from one object to another object,
# those variables are called as Instance variables.
# Declaring Instance Variable:
# - Inside the constructor method using self variable
# - We can declare inside the instance method by using self variable
# - Outside of the class by using object reference variable.

class Employee_Instance:
    def __init__(self, ename, job):
        self.ename = ename
        self.job = job

    def display(self):
        print(f'Employee Name: {self.ename}')
        print(f'Job: {self.job}')

# Creating employee object
emp1_i = Employee_Instance('Smith', 'Manager')
emp2_i = Employee_Instance('Martin', 'Python Developer')

# Display employee details
emp1_i.display()
emp2_i.display()
print()

# (ii) Static Variables:
# - Static Variables are also called as class level variable, the value of variable will not
# be different from one object to another object.
# - We can access static variables using class Name and object reference.
# Declaring Static variables:-
# - We can declare a static variable inside a class.
# - We can declare a static variable inside class method using cls instead of self.
# - Inside static method, created variables, we can access from outside the class with the help
# of class-name.

class Employee_Static:
    company_name = "Techcrop"  # Static variable

    def __init__(self, ename, job):
        self.ename = ename  # Instance variable
        self.job = job      # Instance variable

    def display(self):
        print(f'Name: {self.ename}, Job: {self.job}, Company: {Employee_Static.company_name}')

emp1_s = Employee_Static("Smith", "Manager")
emp2_s = Employee_Static("Martin", "Salesman")
emp1_s.display()
emp2_s.display()
print()

# (iii) Local Variables:-
# - Local variables are also called as temporary variables. In order to perform additional
# implementation, we can create temporary variables.
# - Local variables are not associated with either self or cls (either object or class).
# - Local variables, we cannot access outside the class.

# Example:
class Employee_Local:
    def __init__(self, ename, monthly_salary, job):
        self.ename = ename
        self.monthly_salary = monthly_salary
        self.job = job

    def calculate_annual_sal(self):
        annual_salary = self.monthly_salary * 12
        print(f'Employee {self.ename}, Job: {self.job}')
        print(f'Annual Salary {annual_salary}')

emp_l = Employee_Local('Smith', 9000, "SQL Developer")
emp_l.calculate_annual_sal()
print()

# Types of methods in oops:-
# (i) Object method (self)
# (ii) Class Method (cls) (@classmethod)
# (iii) Static Method (@staticmethod)

# (i) Object Method:-
# - Object Method is also called as instance method.
# - Object Method, it is used to access and modify members of objects. (Instance variables)
# - For all the object methods, passing self is mandatory.
# - If we are calling an object method using class, then we have to pass address of an object.

# Question: WAP to create object method.
class BankAccount_ObjMethod:
    def __init__(self, cname, balance):
        self.balance = balance
        self.cname = cname

    def deposite(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"'{amount}' has been deposited")
            print(f'Updated Balance {self.balance}')
        else:
            print('Amount must be greater than 0')

b1_om = BankAccount_ObjMethod('Martin', 98000)
b1_om.deposite(1000)
print()

# (ii) Class Method:-
# - It is a method which is used to access and modify the members of class.
# - For class method, we have to decorate with @classmethod.
# - For all the class method, passing cls is mandatory to store address of class.
# Example:

class BankAccount_ClassMethod:
    bankname = 'ICICI'

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def change_bankname(cls, new_bankname):  # class_method
        print(f'before modify bank name is: {BankAccount_ClassMethod.bankname}')
        cls.bankname = new_bankname
        print(f'After modify bank name is: {BankAccount_ClassMethod.bankname}')

    def deposite(self, amount):  # instance method
        self.balance = self.balance + amount
        print(f'{amount} has been deposited')
        print(f'After deposite, updated balance: {self.balance}')

    def display(self):  # instance method
        print(f'customer name: {self.name}')
        print(f'initial balance: {self.balance}')

b1_cm = BankAccount_ClassMethod('smith', 45000)
b1_cm.display()
b1_cm.deposite(1000)
b1_cm.change_bankname('HDFC')
print()

# (iii) Static Method:-
# - It is a method, which is neither belongs to class nor belongs to object.
# - It is used to perform required implementation based on requirement.
# - To create static method, we have to use @staticmethod decorator.
# Example:-

class calculator_demo:
    @staticmethod
    def addition(a, b):
        return a + b

print(calculator_demo.addition(100, 500))
print()

# Question: WAP to create instance method, class method and static method, to display student name, marks and school name.
# Instance variables (student name, marks)
# class variable (school name)
# Instance method (add bonus marks)
# class method (change school name)
# static method (check Pass or Fail) (Pass if marks greater than equal to 35)

class student_demo:
    school_name = 'Pyspiders'

    def __init__(self, sname, marks):
        self.sname = sname
        self.marks = marks

    def initialmarks(self):
        print(f'initial marks: {self.marks}')

    def add_bonus(self, bonus):  # instance method
        self.marks = self.marks + bonus
        print(f'{bonus} marks added')

    @classmethod
    def change_school(cls, new_name):  # class method
        print(f'School Name Before: {cls.school_name}')
        cls.school_name = new_name
        print(f'School Name After: {cls.school_name}')

    @staticmethod
    def check_result(marks):  # static method
        return marks >= 35

    def display(self):
        print(f'Student Name: {self.sname} and marks: {self.marks} and school name is: {student_demo.school_name}')

        if student_demo.check_result(self.marks):
            print('Result: pass')
        else:
            print("Result: Fail")

s1_d = student_demo('Miller', 75)
s1_d.initialmarks()
s1_d.add_bonus(11)
student_demo.change_school('Jspiders')
s1_d.display()
print()


# 14) WAP to Demonstrate Static Method
class Demo:

    @staticmethod
    def display():
        print("This is Static Method")

Demo.display()
print()

# 15) Student Management using Instance, Class and Static Method
class Student:

    school = "Jspiders"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def bonus(self):
        self.marks += 5

    @classmethod
    def changeschool(cls,newschool):
        cls.school = newschool

    @staticmethod
    def result(marks):
        if marks >= 35:
            return "Pass"
        return "Fail"

    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
        print("School:",Student.school)
        print("Result:",Student.result(self.marks))

s1 = Student("Smith",70)

s1.bonus()
Student.changeschool("Pyspiders")

s1.display()
print()

# 16) Single Level Inheritance (Page 28)
# WAP to create parent class as Bank and child class as SavingsAccount to perform deposit operation.
class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print('Customer Name is:', self.name)
        print('Initial Bank Balance is:', self.balance)

class SavingsAccount_Page28(Bank):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('Amount has been deposited')
            print('After deposit, Bank balance is:', self.balance)
        else:
            print('Amount should be greater than zero')

s1 = SavingsAccount_Page28('Smith', 98000)
s1.display()
s1.deposit(1000)
print()

# WAP to display student's name, subject, marks
# and based on marks if marks are (>=35) display
# pass else display fail.

class student:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display(self):
        print(f"Student's Name: {self.name}")
        print(f"Student Subject: {self.subject}")

class Markscount(student):

    def display(self, marks):
        self.marks = marks

        if marks >= 35:
            print(f"{marks} has been displayed")
            print(f"Student pass: {self.marks}")
        else:
            print(f"Student is failed: {self.marks}")

m1 = Markscount("Smith", 39)
m1.display()


# OR

class Student:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Result(Student):

    def update_mark(self, mark):
        self.mark = mark

    def display(self):

        print(f"Student Name is: {self.name}")
        print(f"Student Subject is: {self.subject}")
        print(f"Student scored: {self.mark}")

        if self.mark >= 35:
            print("Status: Pass")
        else:
            print("Status: Fail")

r1 = Result("Smith", "Python")
r1.update_mark(39)
r1.display()

# WAP to create Employee as parent class, Designation as child class and display employee name, salary and designation.

class Employee:

    def __init__(self, ename, salary):
        self.ename = ename
        self.salary = salary

    def display_emp(self):
        print(f"Emp Name : {self.ename} and Salary : {self.salary}")

class Designation(Employee):

    def employee_designation(self, job):
        self.job = job

    def display_job(self):
        print(f"The job is : {self.job}")

obj = Designation("Smith", 40000)

obj.employee_designation("Analyst")

obj.display_emp()
obj.display_job()


# WAP to perform check balance, deposit and withdraw operations using single level inheritance with exception handling validation.

class Bank:

    def __init__(self, acctno, balance):
        self.acctno = acctno
        self.balance = balance

    def account_details(self):
        print(f"Account Number : {self.acctno}")
        print(f"Balance is : {self.balance}")

class SavingAccount(Bank):

    def deposit(self, amount):
        try:

            if amount <= 0:
                raise ValueError("Deposit amount must be positive")

            self.balance += amount

            print(f"Deposit Amount : {amount}")

        except ValueError as e:
            print("Deposit Error :", e)

    def withdraw(self, amount):

        try:

            if amount <= 0:
                raise ValueError("Withdraw amount must be positive")

            if amount > self.balance:
                raise ValueError("Insufficient balance")

            self.balance -= amount

            print(f"Withdraw Amount : {amount}")

        except ValueError as e:
            print("Withdraw Error :", e)

    def update(self):
        print(f"Updated Balance : {self.balance}")

b1 = SavingAccount("12345", 50000)
b1.account_details()
b1.deposit(10000)
b1.withdraw(20000)
b1.update()

# 17) Ticket Booking Inheritance
# WAP to create a parent class Ticket and child class FlightTicket that inherits from Ticket.
class Ticket_Page32:
    def set_ticket_details(self, name, ticket_no):
        self.name = name
        self.ticket_no = ticket_no

    def show_ticket_details(self):
        print('Passenger Name:', self.name)
        print('Ticket Number:', self.ticket_no)

class FlightTicket_Page32(Ticket_Page32):
    def set_flight_details(self, flight_name, seat_no):
        self.flight_name = flight_name
        self.seat_no = seat_no

    def show_flight_details(self):
        print('Flight Name:', self.flight_name)
        print('Seat Number:', self.seat_no)

# User input simulation
ft = FlightTicket_Page32()
ft.set_ticket_details("Smith", "T12345")
ft.set_flight_details("Indigo", "24B")
ft.show_ticket_details()
ft.show_flight_details()
print()

# Constructor Chaining in Python
# Definition
# Constructor chaining is a concept where one constructor calls another constructor within the same class or from a parent class.
# It is mainly used in inheritance to ensure that the parent class constructor is executed before the child class constructor.
# To achieve constructor chaining, we use the super() keyword.
# It avoids code duplication and improves readability and structure of the program.
# If super() is not used, the parent constructor will not execute automatically.
# Example (1): Without Using super() Keyword

class Parent:

    def __init__(self):
        print("This is parent class")

class Child(Parent):

    def __init__(self):
        print("This is child class")

obj = Child()


# Since super() is not used, the parent constructor is not executed.

# Example (2): Using super() Keyword (Constructor Chaining)
class Parent:

    def __init__(self):
        print("This is parent class")

class Child(Parent):

    def __init__(self):
        super().__init__()
        print("This is child class")

obj = Child()

# 18) Constructor Chaining - Student/College (Page 35)
# WAP to display student name, age, and subject using single level inheritance with constructor chaining.
class College_Page35:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student_Page35(College_Page35):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        print('Student Name:', self.name)
        print('Age:', self.age)
        print('Subject:', self.subject)

s1 = Student_Page35('Smith', 25, 'Python')
s1.display()
print()

# 19) Bank with Constructor Chaining (Page 35-36)
# WAP to display initial bank balance, customer account number, bank name, and perform deposit and withdraw operations using single level inheritance and constructor chaining.
class Bank_Page35:
    def __init__(self, bankname, name):
        self.bankname = bankname
        self.name = name

    def details(self):
        print('Bank Name:', self.bankname)
        print('Customer Name:', self.name)

class Account_Page35(Bank_Page35):
    def __init__(self, bankname, name, balance, acctno):
        super().__init__(bankname, name)
        self.balance = balance
        self.acctno = acctno

    def display(self):
        super().details()
        print('Account Number:', self.acctno)
        print('Initial Bank Balance:', self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('Amount has been deposited. After deposit, Balance:', self.balance)
        else:
            print('Amount should be greater than zero')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print('Amount has been withdrawn. After withdrawal, Balance:', self.balance)
        else:
            print('Insufficient Balance')

obj = Account_Page35('ICICI', 'Smith', 98000, 12345)
obj.display()
obj.deposit(1000)
obj.withdraw(500)
print()

# 20) Employee Details with Constructor Chaining (Page 37)
# WAP to display employee name, salary, and designation using constructor chaining.
class Employee_Page37:
    def __init__(self, empno, ename):
        self.empno = empno
        self.ename = ename

class EmployeeDetails_Page37(Employee_Page37):
    def __init__(self, empno, ename, salary, job):
        super().__init__(empno, ename)
        self.salary = salary
        self.job = job

    def display(self):
        print('Employee No.:', self.empno)
        print('Employee Name:', self.ename)
        print('Employee Salary:', self.salary)
        print('Employee Job:', self.job)

e1 = EmployeeDetails_Page37(7839, 'Smith', 98000, 'Analyst')
e1.display()
print()

# 21) Method Chaining in Bank (Page 38)
# Perform single-level inheritance to display customer name, balance, deposit, withdrawal, and enforce a maximum withdrawal limit of 10,000 using method chaining.
class Bank:
    def __init__(self, bankname, name):
        self.bankname = bankname
        self.name = name
        self.balance = 0

    def details(self):
        print(f"Customer Name: {self.name}, Bank Name: {self.bankname}")
        return self

class account(Bank):
    def __init__(self, bankname, name, balance, accountno):
        super().__init__(bankname, name)
        self.balance = balance
        self.accountno = accountno

    def display(self):
        print(f"Account Number: {self.accountno}, Balance: {self.balance}")
        return self

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount deposited: {amount}. Updated Balance: {self.balance}")
        else:
            print("Amount should be greater than zero")
        return self

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Amount withdrawn: {amount}. Updated Balance: {self.balance}")
        else:
            print("Insufficient balance")
        return self

b1 = account('SBI', 'Anil', 299999, 123456)
b1.details().display().deposit(99999999).withdraw(123)

# wap to perform single level inheritance to display customer name balance and to perform deposit and withdraw operations and raise value error(maximum withdraw limit is 10000) using method chaining

class Bankaccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount should be greater than zero")
        self.balance += amount
        print(f"Amount deposited: {amount}. Updated Balance: {self.balance}")
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        if amount <= 0:
            raise ValueError("Amount should be greater than zero")
        self.balance -= amount
        print(f"Amount withdrawn: {amount}. Updated Balance: {self.balance}")

class savingbankaccount(Bankaccount):
    def __init__(self, name, balance, accountno):
        super().__init__(name, balance)
        self.accountno = accountno

    def withdraw(self, amount):
        if amount > 10000:
            raise ValueError("Maximum withdrawal limit is 10000")
        super().withdraw(amount)
        return self

b1 = savingbankaccount('Anil', 299999)
b2 = savingbankaccount('John', 299999)

b1.deposit(99999999)
b2.withdraw(20000)
# try:
# c1.deposit(5000)
# c2.withdraw(15000)
# except ValueError as e:
#     print(e)
# c2.withdraw(15000)



# multilevel inheritance
# method overriding

# syntax:
class grandparent:
    pass
class parent(grandparent):
    pass
class child(parent):
    pass
obj = child()


# wap to dispaly stud name and marks ND PASS OR fail status based on marks
class student: #grand parent class
    def get_name(self):
        self.name = input("Enter your name: ")
        return self

class marks(student):
    def get_marks(self):
        self.marks = int(input("Enter your marks: "))
        return self

class result(marks):
    def display(self):
        print(f'student name is {self.name}')
        print(f'student marks is {self.marks}')

        if self.marks >= 35:
            print('studnet is pass')
        else:
            print('student is fail')
        return self

obj = result()
obj.get_name().get_marks().display()

# waptp bankname, balance and perform deposit and withdraw operations 

class bank:
    def bank_name(self):
        self.bank_name = 'icici'
        print(f'bank name {self.bank_name}')
        return self

class account(bank):
    def __init__(self,amount):
        self.amount = amount
        print(f'balance {self.amount}')
        return self
    
class transactions(account):
    def deposit(self,amount):
        self.balance+=amount
        print(f'{amount} has been deposited')
        print(f'after deposit balance is {self.balance}')
        return self
    
    def withdraw(self,amount):
        self.balance-=amount
        print(f'{amount} has been withdrawn')
        print(f'after withdraw balance is {self.balance}')
        return self

    def display(self):
        print('customer name is {self.name}')
        print('balance is {self.balance}')
        return self
t1 = transactions('Anil',20000)
t1.display()
t1.deposit(5000)
t1.withdraw(900)


# 29) Employee, Department, Project Multi-level Inheritance (Page 42)
# WAP to display employee name, number, salary, department name, and project name using multi-level inheritance.
class Employee_Page42:
    def __init__(self, empno, ename, salary):
        self.empno = empno
        self.ename = ename
        self.salary = salary

    def display_employee(self):
        print(f"Employee number: {self.empno}")
        print(f"Employee name: {self.ename}")
        print(f"Employee salary: {self.salary}")

class Department_Page42(Employee_Page42):
    def __init__(self, empno, ename, salary, dname):
        super().__init__(empno, ename, salary)
        self.dname = dname

    def display_department(self):
        print(f"Department name: {self.dname}")

class Project_Page42(Department_Page42):
    def __init__(self, empno, ename, salary, dname, pid, project_name):
        super().__init__(empno, ename, salary, dname)
        self.pid = pid
        self.project_name = project_name

    def display_project(self):
        self.display_employee()
        self.display_department()
        print(f"Project ID: {self.pid}")
        print(f"Project name: {self.project_name}")

p1 = Project_Page42(7839, 'Smith', 98000, 'Research', 12345, 'Development')
p1.display_project()
print()
#######################################################99#################################################
# 30) Multilevel Inheritance using Constructor
class A_Batch2:
    def __init__(self):
        print("A Constructor")

class B_Batch2(A_Batch2):
    def __init__(self):
        super().__init__()
        print("B Constructor")

class C_Batch2(B_Batch2):
    def __init__(self):
        super().__init__()
        print("C Constructor")

obj_b2 = C_Batch2()
print()

# 31) Student Result using Multilevel Inheritance (Page 40)
class Student_Page40:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class Result_Page40(Student_Page40):
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        if self.marks >= 35:
            print("Status: Pass")
        else:
            print("Status: Fail")

r_b2 = Result_Page40("Smith", 78)
r_b2.display()
print()

# 32) Bank with Multiple Inheritance (Page 41)
# Create classes CheckBalance, Deposit, Withdrawal, and then Bank that inherits from all three.
class CheckBalance_Page41:
    def show_balance(self):
        print(f"Current Balance: {self.balance}")

class Deposit_Page41:
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
        else:
            self.balance += amount
            print(f"Deposited: {amount}")

class Withdrawal_Page41:
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient Bank Balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

class Bank_Page41(CheckBalance_Page41, Deposit_Page41, Withdrawal_Page41):
    def __init__(self, name, acctno, balance):
        self.name = name
        self.acctno = acctno
        self.balance = balance

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Account Number: {self.acctno}")
        print(f"Opening Balance: {self.balance}")

customer = Bank_Page41("Smith", 1234, 12300)
customer.display_details()
customer.deposit(3000)
customer.withdraw(3000)
customer.show_balance()
print()

# 33) BankDetails and AccountDetails Multiple Inheritance (Page 59)
# Create BankDetails and AccountDetails classes, then Customer inherits from both.
class BankDetails_Page59:
    def set_bank(self, bank_name):
        self.bank_name = bank_name
    def show_bank(self):
        print("Bank Name:", self.bank_name)

class AccountDetails_Page59:
    def set_balance(self, balance):
        self.balance = balance
    def show_balance(self):
        print("Balance:", self.balance)

class Customer_Page59(BankDetails_Page59, AccountDetails_Page59):
    def deposit(self, amount):
        self.balance += amount
        print("After deposit:", self.balance)
    def withdraw(self, amount):
        self.balance -= amount
        print("After withdrawal:", self.balance)

c = Customer_Page59()
c.set_bank("SBI")
c.set_balance(5000)
c.show_bank()
c.show_balance()
c.deposit(2000)
c.withdraw(1000)
print()

# 34) Method Resolution Order (MRO)
class A_Batch2_MRO:
    def display(self):
        print("Class A")

class B_Batch2_MRO:
    def display(self):
        print("Class B")

class C_Batch2_MRO(A_Batch2_MRO, B_Batch2_MRO):
    pass

obj_b2_mro = C_Batch2_MRO()
obj_b2_mro.display()
print()

# 35) Check MRO
class A_Batch2_MROCheck:
    pass

class B_Batch2_MROCheck:
    pass

class C_Batch2_MROCheck(A_Batch2_MROCheck, B_Batch2_MROCheck):
    pass

print(C_Batch2_MROCheck.mro())
print()

# 36) Multiple Inheritance Person and Job Details (Page 43)
# Create PersonDetails and JobDetails classes, then Employee inherits from both.
class PersonDetails_Page43:
    def set_name(self, name):
        self.name = name
    def show_name(self):
        print("Name:", self.name)

class JobDetails_Page43:
    def set_salary(self, salary):
        self.salary = salary
    def show_salary(self):
        print("Salary:", self.salary)

class Employee_Page43(PersonDetails_Page43, JobDetails_Page43):
    def show_details(self):
        self.show_name()
        self.show_salary()

e_emp = Employee_Page43()
e_emp.set_name("Muhsin")
e_emp.set_salary(50000)
e_emp.show_details()
print()

# 37) Hierarchical Inheritance Employee Roles (Page 44)
# Create parent class Employee and child classes Manager, Developer, Tester using hierarchical inheritance.
class Employee_Page44:
    def work(self):
        print("Employee works")

class Manager_Page44(Employee_Page44):
    def manage(self):
        print("Manager manages the team")

class Developer_Page44(Employee_Page44):
    def code(self):
        print("Developer writes code")

class Tester_Page44(Employee_Page44):
    def test(self):
        print("Tester tests the application")

m_p44 = Manager_Page44()
d_p44 = Developer_Page44()
t_p44 = Tester_Page44()
m_p44.work()
m_p44.manage()
d_p44.code()
t_p44.test()
print()

# 38) Hierarchical Bank Accounts (Page 51 & 67)
# Create CurrentAccount and SavingsAccount under parent BankAccount.
class BankAccount_Page51:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")

class SavingsAccount_Page51(BankAccount_Page51):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def display(self):
        super().display()
        print(f"Interest Rate: {self.interest_rate}%")

class CurrentAccount_Page51(BankAccount_Page51):
    def __init__(self, name, balance, overdraft):
        super().__init__(name, balance)
        self.overdraft = overdraft

    def display(self):
        super().display()
        print(f"Overdraft Limit: {self.overdraft}")

sa_p51 = SavingsAccount_Page51("John", 15000, 4)
ca_p51 = CurrentAccount_Page51("King", 25000, 1000)
sa_p51.display()
ca_p51.display()
print()

# 39) Employee Bonus Method Overriding (Page 56 & 65)
# Create Employee class with get_bonus(). Create Developer and Manager that override get_bonus().
class Employee_Page56:
    def get_bonus(self, salary):
        self.salary = salary
        print(f"Employee salary is {self.salary}")
        print(f"Employee bonus is {self.salary * 0.1}")

class Developer_Page56(Employee_Page56):
    def get_bonus(self, salary, extra_bonus):
        self.salary = salary
        total = (self.salary * 0.1) + extra_bonus
        print(f"Developer bonus (including extra) is {total}")

class Manager_Page56(Employee_Page56):
    def get_bonus(self, salary, extra_bonus):
        self.salary = salary
        total = (self.salary * 0.15) + extra_bonus
        print(f"Manager bonus (including extra) is {total}")

dev_p56 = Developer_Page56()
mgr_p56 = Manager_Page56()
dev_p56.get_bonus(65000, 5000)
mgr_p56.get_bonus(75000, 10000)
print()

# 40) BankAccount with Constraints Method Overriding (Page 52 & 66)
# Create parent BankAccount with validation. Child SavingsAccount overrides withdraw (limit 100k).
# Child SalaryAccount overrides deposit (minimum 2000).
class BankAccount_Page52:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        print(f"Withdrawn: {amount}")

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")

class SavingsAccount_Page52(BankAccount_Page52):
    def withdraw(self, amount):
        if amount > 100000:
            raise ValueError("Maximum withdrawal limit is 100,000 for savings account")
        super().withdraw(amount)

class SalaryAccount_Page52(BankAccount_Page52):
    def __init__(self, name, balance, accno):
        super().__init__(name, balance)
        self.accno = accno

    def deposit(self, amount):
        if amount < 2000:
            raise ValueError("Minimum deposit for salary account is 2000")
        super().deposit(amount)

    def display(self):
        super().display()
        print(f"Account Number: {self.accno}")


# 41) BankAccount Transactions and Exceptions Handling (Page 53)
# Create objects of SavingsAccount and SalaryAccount, perform deposit/withdraw, and handle exceptions.
try:
    c1_p53 = SavingsAccount_Page52('Smith', 30000)
    c2_p53 = SalaryAccount_Page52('Allen', 10000, 12345)
    print("=== Savings Account Transaction ===")
    c1_p53.deposit(2000)
    c1_p53.withdraw(12000)  # Safe
    c1_p53.withdraw(120000) # This raises error
except ValueError as e:
    print("Error:", e)

try:
    print("\n=== Salary Account Transaction ===")
    c2_p53.deposit(1000)  # This raises error
except ValueError as e:
    print("Error:", e)
print()

# 42) Constructor Overriding using super()
class Child_Batch2_CO(Parent_Batch2_CO):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

c_b2_co = Child_Batch2_CO()
print()

# 43) Hybrid Inheritance Example (Page 50 & 54 & 61)
# Demonstrate hybrid inheritance with SavingsAccount, PremiumSavings, Loan, and CustomerAccount.
class BankAccount_Page50:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class SavingsAccount_Page50(BankAccount_Page50):
    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest

class PremiumSavings_Page50(SavingsAccount_Page50):
    def __init__(self, name, balance, interest, bonus):
        super().__init__(name, balance, interest)
        self.bonus = bonus

class Loan_Page50:
    def __init__(self, loan_amount):
        self.loan_amount = loan_amount

class CustomerAccount_Page50(PremiumSavings_Page50, Loan_Page50):
    def __init__(self, name, balance, interest, bonus, loan_amount):
        PremiumSavings_Page50.__init__(self, name, balance, interest, bonus)
        Loan_Page50.__init__(self, loan_amount)

    def display(self):
        print(f"Customer Name: {self.name}")
        print(f"Balance: {self.balance}")
        print(f"Interest Rate: {self.interest}%")
        print(f"Bonus Marks: {self.bonus}")
        print(f"Loan Amount: {self.loan_amount}")

c_p50 = CustomerAccount_Page50("Martin", 20000, 7, 1000, 5000)
c_p50.display()
print()

# 44) Person -> Employee Program
class Person_Batch2_PE:
    def __init__(self,name):
        self.name = name

class Employee_Batch2_PE(Person_Batch2_PE):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

e_pe = Employee_Batch2_PE("Smith",50000)
e_pe.display()
print()

# 45) Vehicle Hierarchy Program and Abstraction (Page 60)
from abc import ABC, abstractmethod

class Vehicle_Page60(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car_Page60(Vehicle_Page60):
    def start_engine(self):
        print("Car engine started: Vroom!")

c_p60 = Car_Page60()
c_p60.start_engine()
print()
# ==============================================================================
# Important Viva Questions from Section 2 (Pages 46–67)
# ==============================================================================
# What is Multilevel Inheritance?
# When a class inherits from another derived class, it is called Multilevel Inheritance.
#
# What is Multiple Inheritance?
# A child class inherits properties from more than one parent class.
#
# What is Hierarchical Inheritance?
# Multiple child classes inherit from the same parent class.
#
# What is Hybrid Inheritance?
# Combination of two or more inheritance types.
#
# What is Method Overriding?
# Redefining a parent class method in the child class with the same name.
#
# What is MRO?
# Method Resolution Order determines the order in which Python searches for methods in inheritance hierarchies.


# ==============================================================================
# BATCH 3 (PAGES 68–87): PROBLEMS 46 TO 68 & VIVA QUESTIONS
# ==============================================================================

# 46) Encapsulation Example
class Employee_Batch3_Enc:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

e_enc = Employee_Batch3_Enc("Smith",50000)

e_enc.display()
print()

# 47) Public Access Modifier
class Student_Batch3_Pub:

    def __init__(self):
        self.name = "Smith"

s_pub = Student_Batch3_Pub()

print(s_pub.name)
# Output
# Smith
print()

# 48) Public Variables and Methods
class Employee_Batch3_PVM:

    def __init__(self):
        self.name = "Allen"

    def display(self):
        print(self.name)

e_pvm = Employee_Batch3_PVM()

print(e_pvm.name)

e_pvm.display()
print()

# 49) Protected Access Modifier
class Employee_Batch3_Prot:

    def __init__(self):
        self._salary = 50000

class Developer_Batch3_Prot(Employee_Batch3_Prot):

    def show(self):
        print(self._salary)

d_prot = Developer_Batch3_Prot()

d_prot.show()
print()

# 50) Protected Variable Example
class Bank_Batch3_Prot:

    def __init__(self):
        self._balance = 10000

class Customer_Batch3_Prot(Bank_Batch3_Prot):

    def checkbalance(self):
        print("Balance:",self._balance)

c_prot = Customer_Batch3_Prot()

c_prot.checkbalance()
print()

# 51) Protected Method Example
class Parent_Batch3_Prot:

    def _display(self):
        print("Protected Method")

class Child_Batch3_Prot(Parent_Batch3_Prot):

    def show(self):
        self._display()

c_prot_m = Child_Batch3_Prot()

c_prot_m.show()
print()

# 52) Private Access Modifier
class Employee_Batch3_Priv:

    def __init__(self):
        self.__salary = 50000

e_priv = Employee_Batch3_Priv()

# print(e_priv.__salary)
# Output
# AttributeError
print()

# 53) Access Private Variable using Method
class Employee_Batch3_PrivAcc:

    def __init__(self):
        self.__salary = 50000

    def getsalary(self):
        print(self.__salary)

e_priv_acc = Employee_Batch3_PrivAcc()

e_priv_acc.getsalary()
print()

# 54) Private Method Example
class Demo_Batch3_PrivM:

    def __show(self):
        print("Private Method")

    def access(self):
        self.__show()

d_priv_m = Demo_Batch3_PrivM()

d_priv_m.access()
print()

# 55) Name Mangling Example
class Employee_Batch3_NM:

    def __init__(self):
        self.__salary = 60000

e_nm = Employee_Batch3_NM()

print(e_nm._Employee_Batch3_NM__salary)
print()

# 56) Getter Method Example
class Student_Batch3_Getter:

    def __init__(self):
        self.__marks = 80

    def getmarks(self):
        return self.__marks

s_getter = Student_Batch3_Getter()

print(s_getter.getmarks())
print()

# 57) Setter Method Example
class Student_Batch3_Setter:

    def __init__(self):
        self.__marks = 0

    def setmarks(self,marks):
        self.__marks = marks

    def getmarks(self):
        return self.__marks

s_setter = Student_Batch3_Setter()

s_setter.setmarks(90)

print(s_setter.getmarks())
print()

# 58) Getter and Setter Program
class Employee_Batch3_GS:

    def __init__(self):
        self.__salary = 0

    def setsalary(self,salary):
        self.__salary = salary

    def getsalary(self):
        return self.__salary

e_gs = Employee_Batch3_GS()

e_gs.setsalary(70000)

print(e_gs.getsalary())
print()

# 59) Bank Account Encapsulation Program
class BankAccount_Batch3_Enc:

    def __init__(self):
        self.__balance = 10000

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

    def getbalance(self):
        return self.__balance

b_b3_enc = BankAccount_Batch3_Enc()

b_b3_enc.deposit(5000)

print(b_b3_enc.getbalance())
print()

# 60) Student Result using Encapsulation
class Student_Batch3_ResEnc:

    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks

    def result(self):

        if self.__marks >= 35:
            print("Pass")
        else:
            print("Fail")

s_res_enc = Student_Batch3_ResEnc("Smith",80)

s_res_enc.result()
print()

# 61) Employee Bonus Program
class Employee_Batch3_Bonus:

    def __init__(self,salary):
        self.__salary = salary

    def bonus(self):
        print("Bonus:",self.__salary*0.10)

e_bonus = Employee_Batch3_Bonus(50000)

e_bonus.bonus()
print()

# 62) ATM Program using Encapsulation
class ATM_Batch3_ATM:

    def __init__(self):
        self.__pin = 1234

    def validate(self,pin):

        if pin == self.__pin:
            print("Login Successful")
        else:
            print("Invalid PIN")

a_atm = ATM_Batch3_ATM()

a_atm.validate(1234)
print()

# 63) Property Decorator Example
class Student_Batch3_Prop:

    def __init__(self):
        self.__marks = 85

    @property
    def marks(self):
        return self.__marks

s_prop = Student_Batch3_Prop()

print(s_prop.marks)
print()

# 64) Property Setter Example
class Student_Batch3_PropSetter:

    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,value):
        self.__marks = value

s_propset = Student_Batch3_PropSetter()

s_propset.marks = 95

print(s_propset.marks)
print()

# 65) Polymorphism Example
class Dog_Batch3_Poly:

    def sound(self):
        print("Bark")

class Cat_Batch3_Poly:

    def sound(self):
        print("Meow")

d_poly = Dog_Batch3_Poly()
c_poly = Cat_Batch3_Poly()

d_poly.sound()
c_poly.sound()
print()

# 66) Method Overloading Style Example
class Demo_Batch3_MO:

    def add(self,a,b,c=0):
        print(a+b+c)

d_mo_b3 = Demo_Batch3_MO()

d_mo_b3.add(10,20)
d_mo_b3.add(10,20,30)
print()

# 67) Method Overriding Example
class Parent_Batch3_MO:

    def display(self):
        print("Parent")

class Child_Batch3_MO(Parent_Batch3_MO):

    def display(self):
        print("Child")

c_mo_b3 = Child_Batch3_MO()

c_mo_b3.display()
print()

# 68) Final Comprehensive OOP Program
class Employee_Batch3_Final:

    company = "Infosys"

    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.__salary)
        print("Company:",Employee_Batch3_Final.company)

    @classmethod
    def changecompany(cls,name):
        cls.company = name

    @staticmethod
    def greet():
        print("Welcome Employee")

e_final = Employee_Batch3_Final("Smith",50000)

Employee_Batch3_Final.greet()

e_final.display()

Employee_Batch3_Final.changecompany("TCS")

e_final.display()
print()

# ==============================================================================
# Important Viva Questions from Section 3 (Pages 68–87)
# ==============================================================================
# What is Encapsulation?
# Wrapping data and methods into a single unit (class) is called Encapsulation.
#
# What are Access Modifiers in Python?
# - Public
# - Protected
# - Private
#
# Symbol for Public Variable:
# name
#
# Symbol for Protected Variable:
# _name
#
# Symbol for Private Variable:
# __name
#
# What is Data Hiding?
# Restricting direct access to data members using private variables.
#
# What is Polymorphism?
# One interface with multiple implementations.
#
# What is Method Overloading?
# Using the same method name with different parameters (simulated in Python using default arguments).
#
# What is Method Overriding?
# Redefining a parent class method in the child class.
#
# Pillars of OOP:
# - Encapsulation
# - Inheritance
# - Polymorphism
# - Abstraction
