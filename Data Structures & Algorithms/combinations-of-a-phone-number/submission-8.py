class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #this is basically nPr where r is len(digits) and n = len(chats)
        #need to write out all possible permutations

        #max is 16P4 == 16*15*14*13 ~ 10k
        charMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        charStr = ""
        for num in digits:
            charStr+=charMap[num]
        
        if charStr == "":
            return []
        

        res = []
        curr = []
        # chosenArr = [False]*len(charStr)
        
        
        def dfs(i):
            if i >= len(digits):
                res.append("".join(curr))
                return None
            
            for c in charMap[digits[i]]:
                curr.append(c)
                dfs(i+1)
                curr.pop()
        
        
        dfs(0)

        return res

        # #we genere all possible perumutaiton now check for correct ordering
        # #first get rid of duplicated
        # uniquePerm = list(set(allPerm))
        # i = 0
        # badIndexSet = set()
        # for i in range(len(uniquePerm)):
        #     perm = uniquePerm[i]
        #     # print(perm)
        #     for j in range(len(digits)):
        #         currDigit = digits[j]
        #         currChar = perm[j]
        #         # print("digit=",currDigit,"permChar=",currChar,"map=",charMap[currDigit])
        #         if currChar not in charMap[currDigit]:
        #             # print("***BAD***", i)
        #             badIndexSet.add(i)
        #             break
        
        # validPerm = []
        # for i in range(len(uniquePerm)):
        #     if i not in badIndexSet:
        #         validPerm.append(uniquePerm[i])
        # return validPerm

        
        
        
        # #misundertood approahc below
        # #make all possible combinations of digits
        # #make all possible subsets
        # #make all possible permutations of each subsets

        # # allSubsets = []
        # # currSubset = []
        
        # # def dfs_Susbet(i):
        # #     if i >= len(digits):
        # #         allSubsets.append(currSubset.copy())
        # #         return None
        # #     currSubset.append(digits[i])
        # #     dfs_Susbet(i+1)
        # #     currSubset.pop()
        # #     dfs_Susbet(i+1)

        # # def permute(nums):
        # #     res = []
        # #     curPerm = []
        # #     chosenArr = [False]*len(nums)

        # #     def dfs():
        # #         if len(curPerm) == len(nums):
        # #             res.append()