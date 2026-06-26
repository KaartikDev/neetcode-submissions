class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        best = 0

        while r < len(prices):
            currProft = prices[r] - prices[l]

            if currProft > best:
                best = currProft
            
            if prices[r] < prices[l]:
                l = r
            
            r+=1
    
        return best
        