class Solution:
    def trap(self, height: List[int]) -> int:
        #first create an array that has the largest upcoming right wall for each position i
        
        maxRightHeights = []
        currRightMax = 0
        for i in range(len(height)-1,-1,-1): #start from end of arr

            if height[i] >= currRightMax: #whenever we ecnounter >= max add it
                currRightMax = height[i]
                maxRightHeights.append(currRightMax)
        
        

        
        
        maxRightHeights.reverse() #we reverse it to get the highest when scanning left to right

        maxRightHeights.append(0) # the end of the trap has always 0 height (end of array+1)
        # print([maxRightHeights, lastLargestInd])
        
        
        sumWater = 0 #running sum
        leftMax = 0 #highest left wall
        rightMaxInd = 0 #tells us the index of which right wall we should be using

        for i in range(len(height)):
            currWater = 0
            leftMax = max(height[i],leftMax)

            if rightMaxInd < len(maxRightHeights)-1 and height[i] == maxRightHeights[rightMaxInd]: 
                rightMaxInd+=1 #this part moves onto the next right tallest when current catches up
            
            
            if i == 0 or i == len(height)-1: #the ends of the trap have no left/right bounds
                continue
            
            currWater = min(leftMax,maxRightHeights[rightMaxInd]) - height[i]

            # print([i, height[i]],[leftMax, maxRightHeights[rightMaxInd]],[rightMaxInd],currWater)
            if currWater > 0: #only add positive water
                sumWater+=currWater
            
        # print(sumWater)
        return sumWater



            