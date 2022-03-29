def twoSum(nums, target):
    
    for n in nums:
        if (target-n) in nums:
            #ans=[]
            #ans.append(nums.index(n))
            #ans.append(len(nums)-nums[::-1].index((target-n))-1)
            #if(ans[0]!=ans[1]):
                #return ans
            firstDigit=nums.index(n)
            secondDigit=len(nums)-nums[::-1].index((target-n))-1
            if(firstDigit!=secondDigit):
                return [firstDigit,secondDigit]

#Two Sum II - Input Array Is Sorted
def twoSum2Dic(numbers, target):
    hist = {}

    for i, n in enumerate(numbers):
        print(i,n)
        if target - n in hist:
            return [hist[target-n]+1, i+1]
        hist[n] = i
        print(hist)

def twoSum2TwoPointer(nums,target):
    start=0
    end=len(nums)-1

    while start != end:
        sum = nums[start] + nums[end]
        if sum > target:
            end -= 1
        elif sum < target:
            start += 1
        else:
            return [start + 1, end + 1]
    

#nums = [2,7,11,15]
#target = 9
#nums = [3,2,4]
#target = 6
nums = [3,3]
target = 6
#print(twoSum2Dic(nums,target))
print(twoSum2TwoPointer(nums,target))
