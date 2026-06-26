class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # l = 0
        # r = len(heights)-1
        # maxSeen = 0
        # while l < r:
            # maxSeen = max((l))

        #lets do brute force
        maxSeen = 0
        for i in range(len(heights)):
            # print(f"Starting at{i,heights[i]}")
            currTotal = heights[i]
            broken = False
            for j in range(i+1,len(heights)):
                if j < len(heights) and heights[j] >= heights[i] and not broken:
                    # print(f"good{j,heights[j]}")
                    currTotal+=heights[i]
                else:
                    # print(f"BROKEN{j,heights[j]}")
                    broken = True
            broken = False
            # print(' bottom half \n')
            for j in range(i-1,-1,-1):
                
                if j >= 0 and heights[j] >= heights[i] and not broken:
                    currTotal+=heights[i]
                    # print(f"Good{j,heights[j]}")
                else:
                    # print(f"BROKEN{j,heights[j]}")
                    broken = True
            maxSeen = max(maxSeen, currTotal)
        return maxSeen


