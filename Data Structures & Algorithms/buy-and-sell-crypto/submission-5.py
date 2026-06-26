class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestSeen = 0
        l = 0
        r = 0

        while r < len(prices):
            # print(f"TODAY BOUGHT AT {prices[l]} SOLD AT {prices[r]} PROFIT {prices[r]-prices[l]}")
            if prices[r] - prices[l] >= bestSeen:
                bestSeen = prices[r] - prices[l]
                # print("BEST PROFT YET")
            else:
                if prices[r] < prices[l]:
                    l=r
                    # print("NEW LOW")
            r+=1
        
        return bestSeen