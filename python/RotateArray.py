#given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums,k):
    #while(len(nums)<=k):
    #   k=k-len(nums)
    #nums[::]=nums[len(nums)-k::]+nums[0:len(nums)-k]
    k %= len(nums)
    nums[:]=nums[-k:]+nums[:-k]

#nums = [1,2,3,4,5,6,7]
#k = 3
#nums=[-1,-100,3,99]
#k =2
#nums=[1]
#k=5  
#rotate(nums,k)
#print(nums)

#88. Merge Sorted Array
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
#and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

def merge(nums1, m, nums2, n):
    nums1[::]=nums1[0:m]
    print(nums1)
    slicNum2=nums2[0:n]
    print(slicNum2)
    nums1[::]=nums1+slicNum2
    nums1.sort()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
