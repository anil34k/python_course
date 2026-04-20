# Copy Operations

# It is a process of copying the contents of one object into another object is called as copy operation.

# Types of Copy operations
# General copy
# Shallow copy
# Deep copy
# 1) General copy:

# In general copy modification of elements inside the object, it will impact on original object & copied object.

list1 = [10, 20, 30, 40]
list2 = list1

print(list1)# o/p: [10, 20, 30, 40]
print(list2)# o/p: [10, 20, 30, 40]

list2 = [10, 20, 30, 40]
list2 = list1

print(id(list1))# o/p: 185829245782
print(id(list2))# o/p: 185829245782

# modification of elements in copied object

list1 = [10, 20, 30, 40]
list2 = list1

list2[3] = 99

print(list1)# o/p: [10, 20, 30, 99]
print(list2)# o/p: [10, 20, 30, 99]

# 2) Shallow copy:

# In shallow copy modification of elements in copied object it will impact both original object & shallow copied object. (It performs on nested list)

# To perform shallow copy & deep copy operation we have to import copy module.

import copy

# eg:

original_list = [10, 20, [1, 2, 3, 4]]
shallow_copy_list = copy.copy(original_list)
shallow_copy_list[2][3] = 98
print(original_list)      # o/p: [10, 20, [1, 2, 3, 98]]
print(shallow_copy_list)  # o/p: [10, 20, [1, 2, 3, 98]]

# 3) Deep copy:

# Deep copy will not impact on original list object, it will only impact on copied list object after doing modification in elements.

# eg:

import copy

original_list = [10, 20, [1, 2, 3, 4]]
deep_copy_list = copy.deepcopy(original_list)
deep_copy_list[2][3] = 98
print(original_list)   # o/p: [10, 20, [1, 2, 3, 4]]
print(deep_copy_list)  # o/p: [10, 20, [1, 2, 3, 98]]