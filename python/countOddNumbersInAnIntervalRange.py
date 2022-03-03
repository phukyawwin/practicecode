def countOdds1( low: int, high: int) -> int:
    alist=[]
    for x in range(low,high+1):
        print(x)
        if not (x%2==0):
            alist.append(x)
    astring=f'The odd numbers between {low} and {high} are {alist}.'
    print(astring)
    return(len(alist))


def countOdds2(low: int, high: int) -> int:
    return (high-low)//2 if (high%2==0 and low%2==0) else ((high-low)//2)+1

print(countOdds2(3,7))
