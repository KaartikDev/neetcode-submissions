class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy

        #sell

        #curr index, bought index

        row = [None]*2
        table = [row.copy() for _ in range(len(prices))]

        def dp(currDay, ownCoin):
            if currDay >= len(prices):
                return 0
            if table[currDay][ownCoin] is not None:
                return table[currDay][ownCoin]

            skip = dp(currDay+1,ownCoin)
            buy = 0
            sell = 0
            #we can buy if ownCoin == 0 (false)
            if ownCoin == 0:
                buy = dp(currDay+1,1) - prices[currDay]
            else: #incrment by two to account for cool down
                sell = dp(currDay+2,0) + prices[currDay]
            

            table[currDay][ownCoin] = max(buy,sell,skip)
            return table[currDay][ownCoin]
        
        return dp(0,0)

