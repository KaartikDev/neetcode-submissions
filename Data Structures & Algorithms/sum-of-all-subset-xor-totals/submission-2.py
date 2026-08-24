class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        #backtracking on subset

        # net = [0]
        # subset = []

        # def dfs(i):
        #     if i >= len(nums):
        #         cur = 0
        #         for v in subset:
        #             cur^=v
        #         net[0]+=cur
        #         return
            
        #     subset.append(nums[i])
        #     dfs(i+1)
        #     subset.pop()
        #     dfs(i+1)
        # dfs(0)
        # return net[0]


        #way 2: just mainting the xor
        def dfs(i,cur_xor):
            if i >= len(nums):
                return cur_xor

            include = dfs(i+1,cur_xor^nums[i])
            exclude = dfs(i+1,cur_xor)

            return include + exclude
        return dfs(0,0)
    

            
