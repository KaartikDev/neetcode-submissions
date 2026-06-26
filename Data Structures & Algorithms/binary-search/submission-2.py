class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = l+(r-l)//2
        # i = 0
        while l < r and nums[mid] != target  :
            print(l,r,mid,nums[mid])
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
            mid = l+(r-l)//2
            # i+=1
        
        if nums[mid] == target:
            return mid
        else:
            return -1