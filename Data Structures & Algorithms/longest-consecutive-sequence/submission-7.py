class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #dp sol?
        if len(nums) < 2:
            return len(nums)
            
        mySet = set(nums)
        curr = max(mySet)
        end = min(mySet)

        longestRun = 0
        currRun = 0
        
        while curr >= end:

            if curr in mySet and curr-1 in mySet:
                curr-=1
                currRun+=1
            else:
                curr-=1
                currRun = 0

            longestRun = max(longestRun,currRun+1)
        
        return longestRun

            
            

        