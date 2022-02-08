def addDigits(num: int) -> int:
    sum=0
    for x in str(num):
        sum+=int(x)
    if(len(str(sum))==1):
        return (sum)
    else:
        return addDigits(sum)

print(addDigits(38))
