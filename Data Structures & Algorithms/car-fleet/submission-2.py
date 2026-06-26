class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #positions are unique
        
        speedMap = {}

        for i in range(len(position)):
            speedMap[position[i]] = speed[i]
        
        position.sort()

        timeStack = []
        for p in position:
            t = (target-p)/speedMap[p]

            while timeStack and t >= timeStack[-1]:
                timeStack.pop()
            timeStack.append(t)
        return len(timeStack)