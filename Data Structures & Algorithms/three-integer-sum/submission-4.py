class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        i = 0
        res = []

        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]: #skip any duplicates after process first example
                continue
            
            one = nums[i]
            target = 0 - one
            #now just sorted 2 sum reduction
            l = i+1
            r = len(nums)-1

            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    res.append([one,nums[l],nums[r]])

                    l+=1 #move l and skip duplicates
                    while l<r and nums[l-1] == nums[l]:
                        l+=1
                elif curr > target:
                    r-=1
                else:
                    l+=1
        
        return res
                
                