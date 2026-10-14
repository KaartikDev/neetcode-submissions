class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        memo = {}

        def dp(i):
            if i == len(s):
                return 1
            
            if i in memo:
                return memo[i]
            

            curr = 0
            if int(s[i]) > 0: #we take curr
                # print("s=",s[i])
                curr+=dp(i+1)
            # print(i)
            if i < len(s)-1 and 10 <= int(s[i:i+2]) <= 26: #we take two
                # print("s=",s[i:i+2])
                curr+=dp(i+2)
            
            memo[i] = curr
            return memo[i]
        return dp(0)
