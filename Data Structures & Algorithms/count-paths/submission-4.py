class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        row = [0]*n
        table = [row.copy() for _ in range(m)]

        # print(table)
        def dfs(r,c):
            if r == m-1 and c == n-1:
                return 1
            if table[r][c] != 0:
                return table[r][c]

            count = 0
            if r+1<m:
                count+=dfs(r+1,c)
            if c+1<n:
                count+=dfs(r,c+1)
            table[r][c] = count
            return table[r][c]
    
        
        
        return dfs(0,0)
        #(m-1)+(n-1) choose n-1

        # def factorial(i):
        #     if i <= 1:
        #         return 1
        #     else:
        #         return i * factorial(i-1)
        
        # net_fact = factorial(n+m-2)
        # row_fact = factorial(m-1)
        # col_fact = factorial(n-1)

        # return net_fact//(row_fact*col_fact)

        # O(m+n) time
        # O(m+n) space