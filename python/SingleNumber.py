def singleNumber(nums) -> int: 
    for ele in nums:
        if (nums.count(ele) == 1):
            return ele
print(singleNumber([2,3,4,1,2,3,4]))
