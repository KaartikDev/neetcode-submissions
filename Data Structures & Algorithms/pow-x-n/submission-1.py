class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recurPow(x,n):
            if n == 0:
                return 1
            half = recurPow(x,n//2)
            result = half*half
            if n%2==1: #odd power correction
                result*=x
            return result

        if n < 0: #negative power correction
            x = 1/x
            n = -n
                    
        return recurPow(x,n)