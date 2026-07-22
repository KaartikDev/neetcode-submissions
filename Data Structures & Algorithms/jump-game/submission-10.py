class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: #trivial case
            return True
        if nums[0] == 0: #only one element case
            return len(nums) == 1
        
        jumpsLeft = nums[0]
        nextIndex = 1 #is the next reachable index to check

        while nextIndex < len(nums) and jumpsLeft > 0:
            #consume a jump to get to next index
            jumpsLeft-=1

            #we take the jumps at pos nextIndex if its greater than jumps left
            if nums[nextIndex] > jumpsLeft: 
                jumpsLeft = nums[nextIndex]
            nextIndex+=1
        
        return nextIndex == len(nums) #if next index is len we can def reach len-1
        

