class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        foundMin = nums[0]
        while l <= r:
            mid = l + (r-l)//2
            # print(nums[l], nums[mid],nums[r])
            #We are searching for the split
            
        
            if nums[l] < nums[r]: #we have a normal sorted subarray
                foundMin = min(foundMin, nums[l])
                break
            

            foundMin = min(foundMin, nums[mid])
            if nums[mid] >= nums[l]: #means middle is part of left side of orignal arr
                l = mid+1 #search the right side
            else:
                r = mid-1
            
        
        # print(nums[l])
        return foundMin
