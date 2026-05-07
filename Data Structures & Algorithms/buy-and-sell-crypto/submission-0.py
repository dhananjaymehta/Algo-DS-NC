class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0#low buy
        r=1# sell high
        maxP=0 # track total profit
        profit = 0
        while r<len(prices):            
            if prices[l]<prices[r]:
                maxP = max(maxP , prices[r]-prices[l])
            else:
                l=r                
            
            r+=1
        return maxP 
            