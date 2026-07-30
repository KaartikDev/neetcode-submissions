class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        #convert int to string, split, sqaure and sum elements, add to seen, repeat


        def recurCheck(n):
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            stringN = str(n)
            cycleSum = sum([int(d)*int(d) for d in stringN])
            
            return recurCheck(cycleSum)

        
        return recurCheck(n)