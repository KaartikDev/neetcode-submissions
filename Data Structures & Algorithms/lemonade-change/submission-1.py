class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bankMap = {}
        bankMap[5] = 0
        bankMap[10] = 0
        bankMap[20] = 0

        for t in bills:
            # print("curr bill=",t, "curr bankMap is=",bankMap)
            if t == 5:
                bankMap[5]+=1
            elif (t == 10 and bankMap[5] >= 1):
                bankMap[5]-=1
                bankMap[10]+=1
            elif (t==20 and (bankMap[5] >= 3 or (bankMap[10] >= 1 and bankMap[5] >= 1))):
                if bankMap[10] >= 1 and bankMap[5] >= 1:
                    bankMap[5]-=1
                    bankMap[10]-=1
                elif bankMap[5] >= 3:
                    bankMap[5]-=3

                bankMap[20]+=1
            else:
                return False
        return True