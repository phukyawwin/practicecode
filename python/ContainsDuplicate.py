def containsDuplicate(nums) -> bool:
    nums.sort()
    for i in range (len(nums)-1):
        if(nums[i]==nums[i+1]):
            return True
    return False
    
    
#nums = [1,2,3,1]
#nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
