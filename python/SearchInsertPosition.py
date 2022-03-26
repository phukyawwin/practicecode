def searchInsert( nums, target) -> int:
    if (target in nums):
        return nums.index(target)
    else:
        if nums[len(nums)-1]<target:
            return len(nums)
        for i in range (len(nums)):
            if nums[i]>target:
                return i

def searchInsert1( nums, target) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)
        
nums = [1,3,5,6]
target = 2
print(searchInsert1(nums,target))
