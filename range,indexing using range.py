# range 
# the range data type in python is a built in immutable sequence type that represents a sequence of numbers.
# it is commonly used for looping statements
# it supports indexing and slicing by converting to list or tuple data type

# syntax of range data type
# range(stop)
# range(start, stop)
# range(start, stop, step)
# start - it is optional and the default value is 0
# stop - it is required and it is the end value of the sequence. the sequence ends before this number
# step - it is optional and the default value is 1. it is the difference between each number in the sequence the default value is 1
# which means that the sequence will include every number from start to stop with a step of 1

r1 = range(10)
print(r1) # range(0, 10)
print(list(r1)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(r1)) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# example of range data type with start and stop

r2 = range(1, 7)
updated = list(r2)
print(updated) # [1, 2, 3, 4, 5, 6]
print(tuple(r2)) # (1, 2, 3, 4, 5, 6)

# example of range data type with start, stop and step
r4 = range(1, 10, 1)
print(list(r4)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(r4)) # (1, 2, 3, 4, 5, 6, 7, 8, 9)

r3 = range(1, 11, 2)
print(list(r3)) # [1, 3, 5, 7, 9]
print(tuple(r3)) # (1, 3, 5, 7, 9)

# example to generate sequence of numbers in decending order

r5 = range(10, 0, -1)
print(list(r5)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

r6 = range(10, 0, -2)
print(list(r6)) # [10, 8, 6, 4, 2]

r7 = range(10, 0, -3)
print(list(r7)) # [10, 7, 4, 1]

# indexing using range data type
# the process of extracting single digit from the sequence is called indexing

r8 = range(10, 101, 10)
update = list(r8)
print(update) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(update[0]) # 10
print(update[1]) # 20
print(update[2]) # 30
print(update[3]) # 40
print(update[4]) # 50
print(update[5]) # 60
print(update[6]) # 70
print(update[7]) # 80
print(update[8]) # 90
print(update[9]) # 100

# slicing positive 

print(update[0:5]) # [10, 20, 30, 40, 50]
print(update[2:7]) # [30, 40, 50, 60, 70]
print(update[1:9:2]) # [20, 40, 60, 80, 100]
print(update[0:10:3]) # [10, 40, 70, 100]
print(update[0:10:4]) # [10, 50, 90]
print(update[3:8]) # [40, 50, 60, 70, 80]
print(update[3:8:2]) # [40, 60, 80]
print(update[4:9:2]) # [50, 70, 90]

# negative slicing

print(update[-1]) # 100
print(update[-2]) # 90
print(update[-3]) # 80
print(update[-5:-1]) # [60, 70, 80, 90]
print(update[-5:-1:2]) # [60, 80]
print(update[-6:]) # [50, 60, 70, 80, 90]
print(update[-6::2]) # [50, 70, 90]
print(update[-10:-1:3]) # [10, 40, 70, 100]

