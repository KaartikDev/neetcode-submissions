class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}

        def dfs(height):
            
            if height in memo:
                return memo[height]
            if height == 0:
                return cost[0]
            if height == 1:
                return cost[1]
            

            
            memo[height] = min(dfs(height-1), dfs(height-2))+cost[height]
            return memo[height]
        
        
        # print(memo, len(cost))
        return min(dfs(len(cost)-1), dfs(len(cost)-2))

                