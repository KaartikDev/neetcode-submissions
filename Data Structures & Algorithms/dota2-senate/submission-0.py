class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D,R = deque(), deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while D and R:
            currD = D.popleft()
            currR = R.popleft()
            if currR < currD:
                R.append(currR+len(senate))
            else:
                D.append(currD+len(senate))
        if D:
            return "Dire"
        else:
            return "Radiant"
    
            
        
    

      #i see n^2 sol

