class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        coinSet = set(coins)
        smallestCoin = min(coinSet)
        
        def dfs(amt):
            if amt == 0:
                return 0
            elif amt in coinSet:
                return 1
            elif amt < smallestCoin:
                return -1
            elif amt in memo:
                return memo[amt]
            best = float('inf')
            for c in coins:
                remaining = dfs(amt-c)
                if remaining != -1 and remaining is not None:
                    best = min(best,1+remaining)
            memo[amt] = best if best < float('inf') else -1
            return memo[amt]
        
        return dfs(amount)

                    
