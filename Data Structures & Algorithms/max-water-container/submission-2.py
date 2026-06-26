class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights)-1
        maxFound = 0

        while r > l:
            maxFound = max(maxFound,(r-l)*min(heights[l],heights[r]))
            if heights[r] < heights[l]:
                r-=1
            else:
                l+=1
        
        return maxFound