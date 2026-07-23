class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0 #trivial gaurd
        

        if len(nums) == 1: #no jumps needed
            return 0


        # always gaurnteed possible solution
        res = 0
        l,r = 0,0
        while r < len(nums)-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i+nums[i])
            l = r+1
            r = farthest
            res+=1
        return res