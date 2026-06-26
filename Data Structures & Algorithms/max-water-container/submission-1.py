class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftP = 0
        rightP = len(heights)-1

        maxWater = 0

        while leftP < rightP:
            # print(rightP)
            currWater = min(heights[leftP],heights[rightP]) * (rightP-leftP)
            maxWater = max(maxWater, currWater)
            
            if heights[leftP] < heights[rightP]:
                leftP+=1
            else:
                rightP-=1
        
        return maxWater