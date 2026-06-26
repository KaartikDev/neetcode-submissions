class TimeMap:

    def __init__(self):
        self.timeStampMap = {} #key : [times]
        self.valueMap = {} #key : [vals]
        

    def set(self, key: str, value: str, timestamp: int) -> None:


        if key not in self.timeStampMap:
            self.timeStampMap[key] = [timestamp]
            self.valueMap[key] = [value]
        else:
            self.timeStampMap[key].append(timestamp)
            self.valueMap[key].append(value)

        

    def get(self, key: str, timestamp: int) -> str:
        # print(self.timeStampMap)
        # print(self.valueMap)

        if key not in self.timeStampMap: #no key gaurd
            return ""

        
        
        #do a binary search on a monotonic increasing time to find the closest time and its index

        closestInd = -1
        l = 0
        r = len(self.timeStampMap[key]) - 1

        while l <= r:
            mid = (l+r)//2
            if self.timeStampMap[key][mid] == timestamp: #if exact time was found return the value for that time
                return self.valueMap[key][mid]
            
            if self.timeStampMap[key][mid] < timestamp: #update the closest index if curr time qualifies
                closestInd = mid
            
            if self.timeStampMap[key][mid] > timestamp:
                r = mid - 1 #search left
            else:
                l = mid + 1 #search right
        
        if closestInd < 0: #if we never update closestInd no time qualifes return nothing
            return ""
        else:
            return self.valueMap[key][closestInd]




        
