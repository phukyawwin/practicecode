def firstBadVersion(n) -> int:
    if(n==1):
        return 1
    high=n
    low=1
    while low<=high:
        mid = ((high+low)) //2
        if isBadVersion(mid):
            if not isBadVersion(mid -1 ):
                return mid
            high = mid - 1
        else:
            low = mid +1
def isBadVersion(version) -> bool:
    if version >=1:
        return True
    else:
        return False

print(firstBadVersion(1))
