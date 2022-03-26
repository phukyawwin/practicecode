def maxSubArray(nums) -> int:
    max_sum=min(nums)
    cur=0
    for x in nums:
        if(cur<0):
            cur=0
        cur +=x
        max_sum=max(max_sum,cur)
        print("max_sum : %d, cur : %d" % (max_sum, cur))
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [1]
#nums = [5,4,-1,7,8]
print(maxSubArray(nums))
