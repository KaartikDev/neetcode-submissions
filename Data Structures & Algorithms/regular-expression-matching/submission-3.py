class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #i,j are states
        #we need to take from both if equal
        #we can also skip and reset j to 0
        # else false?

        #s only has lower english no . or *, pattern can have . or *
        # * always has valid char before it

        #we assume anchor tags on p due to problem def
        memo = {}

        def dp(i,j):
            if j == len(p) and i == len(s):
                return True
            if j == len(p): #we reached end of pattern but target not done
                return False
            if (i,j) in memo:
                return memo[(i,j)]

            
            res = False
            #special case *
            if j+1<len(p) and p[j+1] == "*":
                #we need to check zero count
                res = res or dp(i,j+2)

                #we need to take all possible counts 1 to inf by not moving j forward
                if i < len(s) and (s[i] == p[j] or p[j]=='.'):
                    res = res or dp(i+1,j)
                

            
            if i < len(s) and (s[i] == p[j] or p[j]=='.'): #take
                res = res or dp(i+1,j+1)
            
            

            memo[(i,j)] = res
            return memo[(i,j)]
        
        return dp(0,0)
            
            
