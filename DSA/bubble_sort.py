# bubble sort algorithm
# iteration 1
# 538672
# 358672
# 358672
# 356872
# 356782
# 356728

# iteration 2
# 356728
# 356728
# 356728
# 356278
# 356278

# iteration 3
# 356278
# 352678
# 352678
# 352678
# 352678

# iteration 4
# 352678
# 325678
# 325678
# 325678
# 325678

# iteration 5
# 325678
# 235678
# 235678
# 235678
# 235678

# final iteration
# 235678

def sort(nums):                        # define a function called 'sort' that takes a list 'nums'
    for i in range(len(nums)-1,0,-1):  # outer loop: controls how many passes are done (from last index down to 1)
        for j in range(i):             # inner loop: compares adjacent elements from index 0 up to i-1
            if nums[j] > nums[j+1]:    # if the current element is greater than the next element, they are out of order
                temp = nums[j]         # store the current element in a temporary variable
                nums[j] = nums[j+1]    # replace current element with the next (smaller) element
                nums[j+1] = temp       # place the larger element in the next position (swap complete)

nums = [5,3,8,6,7,2]  # input list of unsorted numbers
sort(nums)             # call the sort function to sort 'nums' in-place (modifies the original list)
print(nums)            # print the sorted list