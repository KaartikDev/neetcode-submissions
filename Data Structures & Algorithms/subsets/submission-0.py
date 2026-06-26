class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        
         

        #so my idea is we either include an element or we dont
        #the cardinatlity of the set of all subsets is 2^n
        
        
        #this is a backatracking solution 
        res = []
        #dfs

        curSubset = []
        def dfs(index):
            if index >= len(nums):
                # print(curSubset)
                res.append(curSubset.copy())
                return None
            
            #include nums[i]
            #left branch of decison tree (add number)
            curSubset.append(nums[index])
            dfs(index+1)
        
            #right branch of deciton tree(dont add number)
            curSubset.pop()
            dfs(index+1)
        
        dfs(0)

        return res
