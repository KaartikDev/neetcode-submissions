class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #(m-1)+(n-1) choose n-1

        def factorial(i):
            if i <= 1:
                return 1
            else:
                return i * factorial(i-1)
        
        net_fact = factorial(n+m-2)
        row_fact = factorial(m-1)
        col_fact = factorial(n-1)

        return int(net_fact/(row_fact*col_fact))