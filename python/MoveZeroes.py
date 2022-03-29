#Move Zeroes to end of array

def moveZeroes(nums):
    count=0
    n=len(nums)
    for i in range(n):
        if(nums[i]!=0):
           nums[count]=nums[i]
           count+=1
    while count<n:
        nums[count]=0
        count+=1

def moveZeroesSwap(nums):
    left=0
    for i in range(len(nums)):
        if(nums[i]!=0):
            temp=nums[i]
            nums[i]=nums[left]
            nums[left]=temp
            left+=1
        
        
nums = [0,1,0,3,12]
#nums=[0,0,1]
moveZeroesSwap(nums)
print(nums)
