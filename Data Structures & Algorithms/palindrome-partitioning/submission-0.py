class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # try all possible subtring splits from size 1 to len(s)
        # verify all of the strings are palindromes
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]
        res = []
        currPartion = []

        def dfs(i):
            if i >= len(s):
                res.append(currPartion.copy())
                return None
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    currPartion.append(s[i:j+1])
                    dfs(j+1)
                    currPartion.pop()
        
        dfs(0)
        return res


        # at each index in str we can either split or not split --> 2^n diff strings









        #build a program which can give all possible subtring splits from size 1 to len(s)

        # def subtringList(givenString,size):
        #     substringList = []
        #     i = 0
        #     currStr = ""
        #     while i < len(givenString):
        #         if len(currStr) < size:
        #             currStr+=givenString[i]
        #         else:
        #             substringList.append(currStr)
        #             currStr=givenString[i]
        #         i+=1
        #     if currStr:
        #         substringList.append(currStr)
            
        #     return substringList
                
        # allSubstr = []
        # for sz in range(1,len(s)):
            
        #     # print(subtringList(s,sz))
        #     allSubstr.append(subtringList(s,sz))
        
        # print(len(allSubstr)*len(s))
        # print(allSubstr)

        # for strList in allSubstr:
        #     allValid = True
        #     for curStr in strList:
        #         # print(curStr,curStr[::-1])
        #         if curStr != curStr[::-1]:
        #             # print("BAD", curStr)
        #             allValid = False
            
        #     if allValid:
        #         res.append(strList)
        
        # return res

            

