def maxProfit(prices):
    if len(prices)==0:
        return 0
    maxProfit=0
    minPrice=prices[0]
    for i in range(len(prices)):
        profit=prices[i]-minPrice
        maxProfit=max(profit,maxProfit)
        minPrice=min(minPrice,prices[i])
    return maxProfit

#Time Limit Exceeded
def maxProfit1( prices):
    maxProfit=0
    if len(prices) <= 1:
        return 0
    for i in range(1, len(prices)):
        for j in range(0,i):
            profit=prices[i]-prices[j]
            maxProfit=max(profit,maxProfit)
    return maxProfit


prices = [7,1,5,3,6,4]
#prices = [1,2]
print(maxProfit1(prices))
