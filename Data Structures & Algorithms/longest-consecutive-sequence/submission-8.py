class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)
        

        uniqueNums = set(nums)
        best = 0
        for e in uniqueNums:
            if e-1 not in uniqueNums:
                #start run
                currLen = 1
                currStart = e
                while currStart+1 in uniqueNums:
                    currLen+=1
                    currStart+=1
                best=max(currLen,best)
        return best

        
        
        # if len(nums) < 2:
        #     return len(nums)

        # mySet = set(nums)
        # curr = max(mySet)
        # end = min(mySet)

        # longestRun = 0
        # currRun = 0
        
        # while curr >= end:

        #     if curr in mySet and curr-1 in mySet:
        #         curr-=1
        #         currRun+=1
        #     else:
        #         curr-=1
        #         currRun = 0

        #     longestRun = max(longestRun,currRun+1)
        
        # return longestRun

            
            

        