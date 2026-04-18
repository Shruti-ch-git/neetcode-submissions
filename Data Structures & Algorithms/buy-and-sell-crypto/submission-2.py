class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        l=0
        for i in range(len(prices)):
            if prices[i] > prices[l]:
                p=prices[i]-prices[l]
                m=max(p,m)
            else:
                l=i
        return m
        