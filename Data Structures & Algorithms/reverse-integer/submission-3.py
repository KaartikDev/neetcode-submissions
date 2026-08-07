class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        
        MIN = -2147483648
        MAX = 2147483647

        sign = -1 if x < 0 else 1
        absX = abs(x)
        while absX > 0:
            mod = absX % 10
            if res > MAX / 10:
                return 0
            if res == MAX / 10 and mod > MAX % 10:
                return 0
            # if res == MIN / 10 and mod < MIN % 10:
            #     return 0
            
            res = res * 10 + mod
            absX = absX // 10 #truncate towards ZERO 
            #(absX always psotive so we can do // and int() not needed) 
            
        
        return res*sign
            
            