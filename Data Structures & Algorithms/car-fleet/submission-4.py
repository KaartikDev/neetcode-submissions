class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate time of arrival for each car
        # maintain montoncially decreasing stack of arrival times.
        # if a car has a BIGGER position than top and worse arrival time, pop. 

        PosIndexMap = {}
        w = 0
        for p in position:
            PosIndexMap[p] = w
            w+=1
        
        position.sort()

        
        fleetTimePosStack = []
        for i in range(len(speed)):
            currArrivalTime = (target - position[i])/float(speed[PosIndexMap[position[i]]])
            while fleetTimePosStack and position[i] > fleetTimePosStack[-1][1] and currArrivalTime >= fleetTimePosStack[-1][0]:
                # print(f"PREV FLEET {fleetTimePosStack[-1]} TRAPPED BEHIND NEW CAR {(currArrivalTime,position[i])}")
                fleetTimePosStack.pop()
            fleetTimePosStack.append((currArrivalTime,position[i]))
            # print(f"NEW FLEET IS {fleetTimePosStack}")
        return len(fleetTimePosStack)