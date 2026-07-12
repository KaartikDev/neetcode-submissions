class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #feels similar to coin change
        #dp(i) means if s[i:] buildable
        #dp(i) checks s[i:i+c] and dp(i+c) 

        memo = {}

        def dp(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            res = False
            for word in wordDict:
                c = len(word)

                if s[i:i+c] == word and i+c <= len(s):
                    res = res or dp(i+c)
            
            memo[i] = res
            return memo[i]

        ans = dp(0)
        return ans
    