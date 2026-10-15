# selection sort 
#  [5,3,8,6,7,2]
                   
def selection_sort(nums):     
    n = len(nums) 
    for i in range(n-1): 
        mini = i
        for j in range(i+1,n): 
            if nums[j] < nums[mini]: 
                mini = j 
        nums[i], nums[mini] = nums[mini], nums[i]                     
    
nums = [24,41,33,42,17,21]  
selection_sort(nums)             
print(nums)  