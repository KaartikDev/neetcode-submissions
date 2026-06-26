class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # n! options
        #(omega(n!)) best case time

        res = []
        cur = []
        chosenArr = [False] * len(nums)

        def dfs():
            #if no falses in array we are done
            if len(cur) == len(nums):
                res.append(cur.copy())
                return None

            for j in range(len(chosenArr)):
                if chosenArr[j] == False:
                    chosenArr[j] = True
                    cur.append(nums[j])
                    dfs()
                    cur.pop()
                    chosenArr[j] = False


        dfs()

        return res
            

        



        
            
