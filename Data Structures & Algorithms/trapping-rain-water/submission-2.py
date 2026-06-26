class Solution:
    def trap(self, height: List[int]) -> int:
        # l = 0
        # r = l+1
        # negativeWalls = []
        # sumWater = 0
        # currLeft = 0
        # currRight = 0
        # while r < len(height):
            
        #     if l + 1 >= r:

        lastLargestInd = 0
        maxRightHeights = []
        currRightMax = 0
        for i in range(len(height)-1,-1,-1):

            if height[i] >= currRightMax:
                currRightMax = height[i]
                maxRightHeights.append(currRightMax)
        
        

        
        
        maxRightHeights.reverse()
        maxRightHeights.append(0) # the end of the tank has always 0 height(off the array)
        print([maxRightHeights, lastLargestInd])
        
        
        sumWater = 0
        leftMax = 0
        rightMaxInd = 0

        for i in range(len(height)):
            currWater = 0
            leftMax = max(height[i],leftMax)

            if rightMaxInd < len(maxRightHeights)-1 and height[i] == maxRightHeights[rightMaxInd]:
                rightMaxInd+=1 #this part moves to the next hieght right when current catches up
            
            
            if i == 0 or i == len(height)-1:
                continue
            

            

            currWater = min(leftMax,maxRightHeights[rightMaxInd]) - height[i]

            print([i, height[i]],[leftMax, maxRightHeights[rightMaxInd]],[rightMaxInd],currWater)
            if currWater > 0:
                sumWater+=currWater
            
        print(sumWater)
        return sumWater



            