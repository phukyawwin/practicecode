def kWeakestRows(mat, k) :
    ans={}
    for i in range(len(mat)):
        ans[i]=sum(mat[i])
    ans=sorted(ans,key=ans.get)
    return ans[:k]



#mat = [[1,1,0,0,0],
# [1,1,1,1,0],
# [1,0,0,0,0],
# [1,1,0,0,0],
# [1,1,1,1,1]] 
#k = 3
mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2

print(kWeakestRows(mat, k))
