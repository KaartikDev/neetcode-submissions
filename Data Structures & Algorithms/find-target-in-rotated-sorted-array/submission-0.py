class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Idea 1: 

        #Find the partion --> do two binary searches on the left and right side
        #How do we find the partition?
        #if the right > left we have arrived at a sorted subarray --> normal binary sear
        l = 0
        r = len(nums)-1
        while l < r:
            
            mid = (l+r)//2

            print(nums[l],nums[mid],nums[r])

            if nums[l] == target:
                print("ITS RIGHT")
                # return l
            elif nums[r] == target:
                print("ITS LEFT")
                # return r
            elif nums[mid] == target:
                print("ITS MID")
                # return mid
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
        
        pivotIndex = l


        search_l = 0
        search_r = 0

        if target >= nums[pivotIndex] and target <= nums[len(nums)-1]:
            search_l = pivotIndex #target in right sub array
            search_r = len(nums)-1
        else: #target in left sub array
            search_l = 0
            search_r = max(search_l,pivotIndex-1)

        while search_l <= search_r:
            mid = (search_l + search_r)//2

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                search_l = mid+1 #search right
            else:
                search_r = mid-1 #search left

        return -1