class Solution:
    def trap(self, height: List[int]) -> int:
        

        #break through: max of trap - current post = curr_water
        # how find max of trap?
        #max of trip is min(prefix max, suffix max)
        
        #build prefix max
        currMax = height[0]
        prefixMaxes = [0] * len(height)
        for i in range(1,len(height)):
            if height[i] > currMax:
                prefixMaxes[i] = height[i]
                currMax = height[i]
            else:
                prefixMaxes[i] = currMax

        #build suffix max
        currMax = height[len(height)-1]
        suffixMax = [0]*len(height)
        suffixMax[len(height)-1] = currMax
        for i in range(len(height)-2,-1,-1):
            if height[i] > currMax:
                suffixMax[i] = height[i]
                currMax = height[i]
            else:
                suffixMax[i] = currMax
        totalWater = 0
        #calc water
        for i in range(len(height)):
            currWater = min(suffixMax[i],prefixMaxes[i]) - height[i]
            totalWater+=max(currWater,0)
        
        return totalWater