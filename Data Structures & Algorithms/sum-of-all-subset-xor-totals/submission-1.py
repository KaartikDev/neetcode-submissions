class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        net = [0]
        subset = []

        def dfs(i):
            if i >= len(nums):
                cur = 0
                for v in subset:
                    cur^=v
                net[0]+=cur
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return net[0]
    

            
