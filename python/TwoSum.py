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
    

#nums = [2,7,11,15]
#target = 9
#nums = [3,2,4]
#target = 6
nums = [3,3]
target = 6
print(twoSum(nums,target))
