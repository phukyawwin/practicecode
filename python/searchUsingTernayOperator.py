def search(nums, target) -> int:
        return nums.index(target) if (target in nums) else -1

# nums = [-1,0,3,5,9,12]
# target = 9
nums = [-1,0,3,5,9,12]
target = 2
print(search(nums,target))
