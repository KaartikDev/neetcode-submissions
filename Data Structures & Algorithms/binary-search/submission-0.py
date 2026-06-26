class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + int((r - l)/2)
            # print(l, mid, r)
            # print(nums[l], nums[mid], nums[r])
            # print()

            
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        
        return -1
            
            
        
        
    
