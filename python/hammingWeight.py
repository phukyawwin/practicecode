def convertBinaryToDecmail( n):
    res = [int(x) for x in n[::-1]]
    sum=0
    for i in range(len(res)):
        if(res[i]==1):
            sum+=pow(2,i)
    print(sum)
def hammingWeight( n):
    res = [int(x) for x in n]
    print( sum(res))
        
n = "00000000000000000000000000001011"
convertBinaryToDecmail( n)
hammingWeight(n)
