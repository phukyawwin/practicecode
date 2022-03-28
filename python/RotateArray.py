#given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums,k):
    #while(len(nums)<=k):
    #   k=k-len(nums)
    #nums[::]=nums[len(nums)-k::]+nums[0:len(nums)-k]
    k %= len(nums)
    nums[:]=nums[-k:]+nums[:-k]

#nums = [1,2,3,4,5,6,7]
#k = 3
nums=[-1,-100,3,99]
k =2
#nums=[1]
#k=5  
rotate(nums,k)
print(nums)
