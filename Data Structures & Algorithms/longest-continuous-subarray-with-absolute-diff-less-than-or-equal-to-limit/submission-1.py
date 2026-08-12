class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l,r = 0,0
        best = 0

        windowMaxes = deque() #monotonically increasing
        windowMins = deque() #montonically decreasing
        
        while r < len(nums):
            
            while windowMaxes and windowMaxes[-1] < nums[r]: #kill any smaller values in increasing window
                windowMaxes.pop()
            windowMaxes.append(nums[r])

            while windowMins and windowMins[-1] > nums[r]: #kill any bigger values in decreasing window
                windowMins.pop()
            windowMins.append(nums[r])

            # shrink while (smallest_max - biggest_min) > limit
            while windowMaxes and windowMins and windowMaxes[0] - windowMins[0] > limit: 
                # print("bad",l,r,nums[l],nums[r],windowMaxes,windowMins)
                if nums[l] == windowMaxes[0]: # if left was this max get rid of it 
                    windowMaxes.popleft() 
                if nums[l] == windowMins[0]: # if left was this min get rid of it
                    windowMins.popleft()
                l+=1
            
            r+=1
            best = max(best,r-l)
        return best