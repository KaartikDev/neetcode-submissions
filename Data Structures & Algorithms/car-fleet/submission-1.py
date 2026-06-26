class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedMap = {}

        for i in range(len(position)):
            speedMap[position[i]] = speed[i]
        
        position.sort()

        # print(speedMap)
        # print(position)

        fleets = 0

        timeMap = {}
        for p in position:
            timeMap[p] = (target-p) / float(speedMap[p])
        # print(timeMap)

        st = [] #we are storing car pos
        for p in position:
            while st and timeMap[p] >= timeMap[st[-1]]:
                # print(timeMap[p],timeMap[st[-1]] )
                st.pop()
            st.append(p)
            # print(st)

        return len(st)