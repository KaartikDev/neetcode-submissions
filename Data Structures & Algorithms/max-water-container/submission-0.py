class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #greedy plus 2 pointer

        l = 0
        r = len(heights) -1
        maxArea = 0

        while l < r:
            currArea = (r - l) * min(heights[l],heights[r])
            maxArea = max(maxArea, currArea)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        
        return maxArea
        