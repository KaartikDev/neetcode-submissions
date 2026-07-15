class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        row = [None]*len(text2)
        table = [row.copy() for _ in range(len(text1))]
        
        def dfs(i,j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if table[i][j] is not None:
                return table[i][j]
            
            #skip from 1
            #skip from 2
            res = max(dfs(i+1,j),dfs(i,j+1))

            #equal we take from both and inc count
            if text1[i] == text2[j]:
                res = max(1+dfs(i+1,j+1),res)
            
            table[i][j] = res

            return table[i][j]
        
        return dfs(0,0)