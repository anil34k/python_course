# Data types in Python

# single value data types

# 1. int - represents integer values, such as 1, 2, 3, etc.
a=10
print(a)
# Output: 10
print(type(a))
# Output: <class 'int'>

b=-20
print(b)
# Output: -20
print(type(b))
# Output: <class 'int'>

c=int()
print(c)
# Output: 0
print(type(c))
# Output: <class 'int'>

# 2. float - represents floating-point numbers, such as 1.5, 2.5, etc.
d=1.5
print(d)
# Output: 1.5
print(type(d))
# Output: <class 'float'>
e=-2.5
print(e)
# Output: -2.5
print(type(e))
# Output: <class 'float'>
f=float()
print(f)
# Output: 0.0
print(type(f))
# Output: <class 'float'>
# 3. complex - represents complex numbers, such as 1+2j, 3-4j, etc.
g=1+2j
print(g)
# Output: (1+2j)
print(type(g))
# Output: <class 'complex'> 
h=3-4j
print(h)
# Output: (3-4j)
print(type(h))
# Output: <class 'complex'>

i=complex()
print(i)
# Output: 0j
print(type(i))
# Output: <class 'complex'>

j1= 15+20j
j2= 25-30j
print(j1+j2)
# Output: (40-10j)

# 4. bool - represents boolean values, such as True and False.   
a=True
print(a)
# Output: True
print(type(a))
# Output: <class 'bool'>

b=False
print(b)
# Output: False
print(type(b))
# Output: <class 'bool'>

c=bool()
print(c)
# Output: False
print(type(c))
# Output: <class 'bool'>

a=10
b=20
print(a>b)
# Output: False
print(a<b)
# Output: True
print(True == a)
# Output: False
print(20 == True)
# Output: False

# 5. NoneType - represents the absence of a value, such as None.

none_value = None
print(none_value)
# Output: None
print(type(none_value))
# Output: <class 'NoneType'>


# multiple value data types

# 1. str - represents a sequence of characters, such as "Hello", "World", etc.
s1="Hello"
print(s1)
# Output: Hello
print(type(s1))
# Output: <class 'str'>

# wap to print the length of a string
s2="Python programming"
print(len(s2))
# Output: 18

msg = "python"
print(msg[0])
# Output: p
print(msg[1])
# Output: y
print(msg[2])
# Output: t
print(msg[3])
# Output: h
print(msg[4])
# Output: o
print(msg[5])
# Output: n
print(msg[-1])
# Output: n
print(msg[-2])
# Output: o
print(msg[-3])
# Output: h
print(msg[-4])
# Output: t
print(msg[-5])
# Output: y
print(msg[-6])
# Output: p
print(msg[-7])
# Output: 
print(msg[0] + msg[1])

# slicing on string
# EDUCATION
msg='education'
print(msg[::])
#education

msg='education'
print(msg[::3])
#eio

msg='education'
print(msg[::5])
#e


msg='education'
print(msg[1:6:1])
#ducat

msg='education'
print(msg[1:14:2])
#dtao

msg='education'
print(msg[0::4])
#eio


msg='education'
print(msg[::-1])
#noitacude

msg='education'
print(msg[-3::-2])
#tcae


msg='education'
print(msg[1:6:1])
#ducat

msg='education'
print(msg[-1:-9:-1])
#noitacude

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#-------------------------------
# part 1:positive slicing
#-------------------------------

string='welcome to python class'


print(string[0:7])
#welcome
print(string[8:10])
#to
print(string[11:17])
#python
print(string[18:23])
#class
print(string[0:11])
#welcome to
print(string[11:23])
#python class
print(string[3:9])
#come t
print(string[5:15])
#ome to p
print(string[:7])
#welcome
print(string[8:])
#to python class



#------------------------
#part 2: negative slicing
#-------------------------

print(string[-5:])
#class
print(string[-12:-6])
#python
print(string[-23:-16])
#wlecome
print(string[-15:-13])
#to
print(string[-11:-7])
#pyth
print(string[-23:-1])
#wlecome to python clas
print(string[:-6])
#wlecome to python
print(string[-6:])
#class
print(string[-10:-5])
#thon


#----------------------
# part 3: reversing
#----------------------

print(string[:-1])
#wlecome to python clas
print(string[2:-1])
#lecome to python clas
print(string[16:10:-1])
#nohtyp ot emoclew
print(string[-1:-6:-1])
#ssalc
print(string[9:-1])
#to python clas

# 2. list - represents an ordered sequence of items, such as [1, 2, 3, 4, 5], etc.
# types of list 
# homogeneous list - same data types values
# example: [1,2,3,4,5]
# heterogeneous list - different data types values
# example: [1,"python",3.14,True,[1,2],{"a":1},(5,6)]
# syntax: list_name=[index_value]


# indexing in list - means process of extracting single element from given collection
# positive indexing - means process of extracting single element from given collection
# negative indexing - means process of extracting single element from given collection

list1 = [10,20,30,40,50]
print(list1)
print(type(list1))
print(list1[0])
print(list1[1])
print(list1[3])
print(list1[-1])
print(list1[-3])
print(list1[9])

# example for nested list
list2 = [10,20,['smith',100,200],98,270]
print(list2)
print(type(list2))
print(list2[2])
print(list2[2][1])
print(list2[2][2])
print(list2[2][-1])
print(list2[2][-2])

# slicing in list - process of extracting multiple elements from given collection
# positive slicing - means process of extracting multiple elements from given collection
# negative slicing - means process of extracting multiple elements from given collection
# syntax: list_name[start:stop:step]
# start - means starting index
# stop - means stopping index
# step - means step value

list=[10,"python",3.14,True,[1,2],{"a":1},(5,6)]
print(list)
print(type(list))
# positive slicing
print(list[0:3:1])#[10, 'python', 3.14]
print(list[1:4:1])#['python', 3.14, True]
print(list[2:6:1])#[3.14, True, [1, 2], {'a': 1}]
print(list[3:7:1])#[True, [1, 2], {'a': 1}, (5, 6)]
print(list[0:4:1])#[10, 'python', 3.14, True]
print(list[2:7:1])#[3.14, True, [1, 2], {'a': 1}, (5, 6)]
print(list[0:7:2])#[10, 3.14, [1, 2], (5, 6)]
print(list[1:6:2])#['python', True, {'a': 1}]
print(list[0:7:3])#[10, True, (5, 6)]
print(list[4:7:1]) #[[1, 2], {'a': 1}, (5, 6)]
# negative slicing
print(list[-6:-3:1])#[10, 'python', 3.14]
print(list[-5:-2:1])#['python', 3.14, True]
print(list[-4:-1:1])#[3.14, True, [1, 2], {'a': 1}]
print(list[-3:7:1])#[True, [1, 2], {'a': 1}, (5, 6)]
print(list[-7:7:2])#[10, 3.14, [1, 2], (5, 6)]
print(list[-6:6:2])#[10, 3.14, [1, 2], (5, 6)]
print(list[-5:6:1])#['python', 3.14, True, [1, 2], {'a': 1}]
print(list[-4:6:1])#[3.14, True, [1, 2], {'a': 1}]
print(list[-7:-1:1])#[10, 'python', 3.14, True, [1, 2], {'a': 1}]
# reverse slicing
print(list[6::-1])#(5, 6), {'a': 1}, [1, 2], True, 3.14, 'python', 10]
print(list[6:0:-1])#(5, 6), {'a': 1}, [1, 2], True, 3.14, 'python']
print(list[5:1:-1])#{'a': 1}, [1, 2], True, 3.14]
print(list[4::-1])#[1, 2], True, 3.14, 'python', 10]
print(list[6:2:-2])#(5, 6), [1, 2], 'python']

# 3. tuple - represents an ordered sequence of items, such as (1, 2, 3, 4, 5), etc.
tup=(10,20,30,40,50)
print(tup)
print(type(tup))

t2=(10,98,100,True,False,3.14)
print(t2)
print(type(t2))

# indexing in tuple
print(t2[0])
print(t2[1])
print(t2[3])
print(t2[-1])
print(t2[-3])
print(t2[9])

# slicing in tuple - process of extracting multiple elements from given collection
# positive slicing - means process of extracting multiple elements from given collection
# negative slicing - means process of extracting multiple elements from given collection
# syntax: tuple_name[start:stop:step]
# start - means starting index
# stop - means stopping index
# step - means step value

t1=(1,2,3,4,5)
print(t1) #(1, 2, 3, 4, 5)

t1=(1,2,3,4,5,6,7,8,9,10)
print(type(t1)) #<class 'tuple'>

t1=(900,800,700,600,500,[10,20,30,40],'smith','martin')

# // positive slicing //

print(t1[0:5:1]) #[900, 800, 700, 600, 500]
print(t1[1:7:1]) #[800, 700, 600, 500, [10, 20, 30, 40], 'smith']
print(t1[0:7:2]) #[900, 700, 500, 'smith']
print(t1[0:7:3]) #[900, 600, 'martin']
print(t1[0:7:4]) #[900, 500]
print(t1[0:7:5]) #[900, 'smith']
print(t1[0:7:6]) #[900, 'martin']

# // negative slicing //

print(t1[-8:-1:1]) #[900, 800, 700, 600, 500, [10, 20, 30, 40], 'smith']
print(t1[-7:-1:2]) #[800, 600, [10, 20, 30, 40], 'martin']
print(t1[-8:-1:3]) #[900, 600, 'smith']
print(t1[-8:-1:4]) #[900, 500]
print(t1[-8:-1:5]) #[900, 'smith']
print(t1[-8:-1:6]) #[900, 'martin']
print(t1[-8:-1:7]) #[900]

# // reverse slicing //

print(t1[::-1])#('martin', 'smith', [10, 20, 30, 40], 500, 600, 700, 800, 900)
print(t1[2::-2])# (700, 900)
print(t1[-2:0:-2])# ('smith', 500, 700,)


# // set data type - represents an ordered sequence of items, such as {1, 2, 3, 4, 5}, etc.//

s1={1,2,3,4,5}
print(s1) #{1, 2, 3, 4, 5}

s1={1,2,3,4,5,6,7,8,9,10}
print(type(s1)) #<class 'set'>

s2={100,200,300,400,50,70,}
li=list(s2)
print(li) #[400, 50, 100, 70, 200, 300]

print(li[0])#400
print(li[1])#50
print(li[2])#100
print(li[3])#70

# // dictionary data type - represents an ordered sequence of items, such as {1, 2, 3, 4, 5}, etc.// 

d1={'a':10,'b':20,'c':30}
print(d1)# {'a': 10, 'b': 20, 'c': 30}

d1={'a':10,'b':20,'c':30}
print(type(d1))# <class 'dict'>

data={'name':'john','age':25,'city':'new york'}
print(type(data))# <class 'dict'>

print(data.values())# dict_values(['john', 25, 'new york'])
print(data.keys())# dict_keys(['name', 'age', 'city'])
print(data.items())# dict_items([('name', 'john'), ('age', 25), ('city', 'new york')])

# nested dictionary - dictionary inside dictionary
employee={'emp1':{'ename':'john','salary':25000},
          'emp2':{'ename':'jennie','salary':30000},
          'emp3':{'ename':'jim','salary':28000},
          'emp4':{'ename':'jake','salary':26000},
          'emp5':{'ename':'jimmy','salary':27000},
          }

# wap to print employee 3 details
print(employee['emp3']) # {'ename': 'jim', 'salary': 28000}
# wap to print name of employee 3
print(employee['emp3']['ename']) # jim
# wap to print name of 2nd employee 
print(employee['emp2']['ename']) # jennie
# wap to print name of 4 and 5th employee
print(employee['emp4']['ename'],employee['emp5']['ename']) # jake jimmy
# wap to print salary of 1,3 and 5th employee
print(employee['emp1']['salary'],employee['emp3']['salary'],employee['emp5']['salary']) # 25000 28000 27000
# wap to print name of 4th employee and sal of 5th employee
print(employee['emp4']['ename'],employee['emp5']['salary']) # jake 27000

print(employee.keys())#dict_keys(['emp1', 'emp2', 'emp3', 'emp4', 'emp5'])
print(employee['emp1'].keys())#dict_keys(['ename', 'salary'])
print(employee.values())#dict_values([{'ename': 'john', 'salary': 25000}, {'ename': 'jennie', 'salary': 30000}, {'ename': 'jim', 'salary': 28000}, {'ename': 'jake', 'salary': 26000}, {'ename': 'jimmy', 'salary': 27000}])
print(employee.items())#dict_items([('emp1', {'ename': 'john', 'salary': 25000}), ('emp2', {'ename': 'jennie', 'salary': 30000}), ('emp3', {'ename': 'jim', 'salary': 28000}), ('emp4', {'ename': 'jake', 'salary': 26000}), ('emp5', {'ename': 'jimmy', 'salary': 27000})])

