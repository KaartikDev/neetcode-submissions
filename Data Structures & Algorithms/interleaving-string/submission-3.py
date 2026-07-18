class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #i,j --> index into s1 and s2
        
        if s1 == "" and s2 == "" and s3 == "":
            return True
        if s1 == "" and s2 == "" and s3 != "":
            return False
        
        memo = {}

        def dp(i,j):
            if i == len(s1) and j == len(s2) and i+j == len(s3):
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            
            res = False

            #take from s1:
            if i+j < len(s3) and i < len(s1) and s3[i+j] == s1[i]:
                res = res or dp(i+1,j)
            #take from s2
            if i+j<len(s3) and j < len(s2) and s3[i+j] == s2[j]:
                res = res or dp(i,j+1)
            
            memo[(i,j)] = res
            return memo[(i,j)]
        
        return dp(0,0)

