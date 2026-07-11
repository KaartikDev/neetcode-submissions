class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #table[a] = min count count to make amt a
        #table[a] = min(table[a],table[a-c]+1)
        memo = {}

        def dp(a):
            if a == 0:
                return 0
            if a in coins:
                return 1
            if a in memo:
                return memo[a]
            if a < 0:
                return float('inf')
            
            temp = float("inf")
            for c in coins:
                temp = min(temp,dp(a-c)+1)
            
            memo[a] = temp
            return memo[a]
        ans = dp(amount)
        
        if ans < float('inf'):
            return ans
        else:
            return -1
            
