class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #we just do what a bubble sort?
        l = 0
        r = len(nums)-1
        
        count = 0

        while r >= 0 and nums[r] == val:
            count+=1
            r-=1
        
        
        
        while l < r:
            if nums[l] == val:
                nums[l] = nums[r]
                nums[r] = val
                
                while r >= 0 and nums[r] == val:
                    count+=1
                    r-=1
            l+=1
        print(nums, count)
        return len(nums)- count
        
        