class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #feels kinda like permutations
        #spointer,tpointer --> i,j

        memo = {}

        def dp(i,j):
            if j == len(t):
                return 1
            if i >= len(s) or len(s)-i<len(t)-j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            skip = dp(i+1,j)
            take = 0
            if s[i] == t[j]:
                take = dp(i+1,j+1)
            memo[(i,j)] = skip+take
            return memo[(i,j)]
        
        return dp(0,0)


