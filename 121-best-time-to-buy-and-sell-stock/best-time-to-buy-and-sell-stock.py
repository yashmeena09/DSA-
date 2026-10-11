class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        b=0
        max=0
        k=0
        for i in range(1,n):
            if prices[b]<prices[i]:
                k=prices[i]-prices[b]
            else:
                b=i
            if max<k:
                max=k 
        return max   