class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2: #Empty or single day price
            return 0

        l = 0
        r = 1
        maxCalc = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l=r
                r+=1
            else:
                maxCalc = max(maxCalc,prices[r]-prices[l])
                r+=1
        return maxCalc
            

        """
        O(N) time O(1) space
        """