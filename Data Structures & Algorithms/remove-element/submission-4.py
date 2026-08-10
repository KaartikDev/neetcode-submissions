class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)-1
        
        deletedCount = 0

        while r >= 0 and nums[r] == val:
            r-=1 #forget by moving right down
        
        
        #scan left to right and swap as needed
        while l < r:
            if nums[l] == val: 
                nums[l] = nums[r]
                nums[r] = val
                
                #forget by moving right down
                while r >= 0 and nums[r] == val:
                    r-=1
            
            l+=1 #move scan forward

        return r+1 #r+1 is num valid elements as r is in 0 index
        
        