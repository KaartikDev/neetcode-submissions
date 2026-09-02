class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deadEndSet = set(deadends)
        if "0000" in deadEndSet: #ensure that our starting state not dead end
            return -1


        #codes one digit apart have edge between them
        #starting from 0000 see if we can get to target without hitting a deadend node?

        #we need someway to breadth first add all unseen codes one digit apart

        def getNeighborCodes(currCode):
            digits = list(currCode)
            res = []
            for i in range(len(digits)):
                temp = int(digits[i])
                
                if temp == 9:
                    digits[i] = "0"
                    res.append("".join(digits))
                    digits[i] = "8"
                    res.append("".join(digits))
                elif temp == 0:
                    digits[i] = "1"
                    res.append("".join(digits))
                    digits[i] = "9"
                    res.append("".join(digits))
                else:
                    digits[i] = str(temp-1)
                    res.append("".join(digits))
                    digits[i] = str(temp+1)
                    res.append("".join(digits))
                
                digits[i] = str(temp)
            return res
        
        # print(getNeighborCodes("0000"))

        #now need to perform bfs while make sure we never hit deadend
        
        
        pathLen = 0
        queue = deque(["0000"])
        seen = set("0000")

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == target:
                    return pathLen
                
                neighbors = getNeighborCodes(curr)
                for nei in neighbors:
                    if nei not in deadEndSet and nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
            pathLen+=1
        
        return -1






