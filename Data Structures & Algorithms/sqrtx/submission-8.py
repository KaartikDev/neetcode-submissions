class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left = 0
        right = x
        valid_res = 0
        print("x=",x)
        while left <= right:
            mid = (left+right)//2
            print("l=",left,"r=",right,"mid=",mid,"mid_sq=",mid*mid)

            if (mid*mid) > x:
                right = mid-1
            else:
                valid_res = mid
                left = mid + 1
        
        return valid_res
