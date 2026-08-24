class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        
         

        #so my idea is we either include an element or we dont
        #the cardinatlity of the set of all subsets is 2^n
        curr = []
        allSubsets = []
        def dfs(i):
            if i >= len(nums):
                allSubsets.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            dfs(i+1)

        dfs(0)
        return allSubsets
        
        