class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #skip +1
        #take +1
        #transfrom +1
        # re, thetre
        memo = {}

        def dp(i,j):
            if i == len(word1) and j == len(word2):
                return 0
            if i >= len(word1): #ret remaining in w2 via inserts
                return len(word2) - j
            if j >= len(word2): #ret remaining in w1 via inserts
                return len(word1) - i
            if (i,j) in memo:
                return memo[(i,j)]
            
            res = 0
            if word1[i] == word2[j]:
                res = dp(i+1,j+1)
            else:
                # insert char to w1
                insert = 1+dp(i,j+1)
                # delete char in w1
                delete = 1+dp(i+1,j)
                # replace char in w1
                replace = 1+dp(i+1,j+1)
                res = min(insert,delete,replace)
            memo[(i,j)] = res
            return memo[(i,j)]
        
        return dp(0,0)






