class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dp(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return -1
            if amt in memo:
                return memo[amt]
            
            best = float("inf")
            for c in coins:
                remaining = dp(amt-c)
                if remaining != -1:
                    best = min(best,1+remaining)
            memo[amt] = best
            return best
        
        
        return dp(amount) if dp(amount) < float("inf") else -1