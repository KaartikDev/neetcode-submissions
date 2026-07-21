class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        def dp(l,r): #both l and r are exclusive s.t. they are not part of og array
            if r-l==1:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            best = 0
            
            for curr in range(l+1,r):
                coins = nums[curr]*nums[r]*nums[l]
                coins+= dp(l,curr) + dp(curr,r)
                best = max(best,coins)

            
            
            memo[(l,r)] = best
            return best

            

        
        return dp(0,len(nums)-1)
