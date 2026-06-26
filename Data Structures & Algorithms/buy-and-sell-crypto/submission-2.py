class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2: #empty/single day history gaurd
            return 0
        
        l = 0
        r = 1

        maxProfit = 0
        while r < len(prices):
            print(prices[l],prices[r])
            if prices[r] < prices[l]: 
                l = r  # we can now start checking good deals from this new min
                r += 1 #reset window
                
            else: #we have a good deal so record it and keep looking for better ones
                print("GOOD DEAL")
                maxProfit = max(maxProfit, prices[r]-prices[l])
                r+=1 #make window bigger
        
        return maxProfit
        