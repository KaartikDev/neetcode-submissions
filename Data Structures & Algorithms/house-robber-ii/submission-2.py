class Solution:
    def rob(self, nums: List[int]) -> int:        
        if len(nums) < 1:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        

        
        #exclude first or last --> two sperate cases to transform into linear again
        noLast = nums[:-1]
        noFirst = nums[1:]
        # print(evenHouses)
        # print(oddHouses)
        
        def helper(houses):
            memo = {}
            def dfs(i):
                
                if i < 0:
                    return 0
                if i in memo:
                    return memo[i]
                
                memo[i] = max(houses[i]+dfs(i-2),dfs(i-1))
                return memo[i]
            return dfs(len(houses)-1)

        bestNoFirst = helper(noFirst) 
        bestNolast = helper(noLast)

        return max(bestNoFirst,bestNolast)

        #bottom-up dp sol --> solve increasingly complx porblems
        #
            
            



        #top down dp --> recurisvley solve smaller supbroblems

