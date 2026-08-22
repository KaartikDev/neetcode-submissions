class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #idea: find min index (pivot poit)
        #then check above and below for specifc target


        pivot = -1
        l = 0
        r = len(nums)-1

        while l < r:
            while l < r-1 and nums[l] == nums[l+1]:
                l+=1
            while r > l+1 and nums[r] == nums[r-1]:
                r-=1
            

            mid = (l+r)//2

            # if nums[mid] < nums[l] and nums[mid] < nums[r]:
            #     pivot = mid
            #     break
            if nums[mid] == target:
                print(l)
                return True
            
            
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid

        

        #do binary search in either bottom half or top half

        pivot = l
        print(pivot)

        searchTop = False
        if nums[pivot] <= target <= nums[-1]:
            searchTop = True
        
        if searchTop:
            l = pivot
            r = len(nums)-1
        else:
            l = 0
            r = pivot-1
        
        while l < r:
            
            while l < r-1 and nums[l] == nums[l+1]:
                l+=1
            while  r > l+1 and nums[r] == nums[r-1]:
                r-=1
            
            mid = (l+r)//2

            if nums[mid] == target:
                return True
            
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid
            
        return nums[l] == target



