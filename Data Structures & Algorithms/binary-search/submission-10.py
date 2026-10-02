class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (r+l)//2
        # i = 0
        while l < r:
            mid = (r+l)//2
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
            
            # i+=1
        
        if nums[l] == target:
            return l
        else:
            return -1