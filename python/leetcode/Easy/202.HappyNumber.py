def isHappy1(n):
    s=set()
    while True:
        product=0
        while(n>0):
            num=n%10
            product += (num*num)
            n //=10
        n=product
        if(n==1):return True
        if( n in s):return False
        s.add(n)
        

def isHappy(n):
    s=set()
    while n!=1:
        if n in s: return False
        s.add(n)
        n=sum([int(i)**2 for i in str(n)])
    else:
        return True
#n=1111111
#n = 19
n=2
print(isHappy(n))
