def intersect(nums1,nums2):
    m={}

    if len(nums1)<len(nums2):
        nums1,nums2=nums2,nums1
    for i in nums1:
        if i not in m:
            m[i]=1
        else:
            m[i]+=1
    #{1:2,2:2}
    result=[]
    for i in nums2:
        if i in m: # if i in m and m[i]: do not need to pop
            m[i]-=1
            result.append(i)
            if m[i]<=0: 
                m.pop(i)
    return result
    
def intersect1(nums1,nums2):
    from collections import Counter
    return list((Counter(nums1) & Counter(nums2)).elements())

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect1(nums1,nums2))
