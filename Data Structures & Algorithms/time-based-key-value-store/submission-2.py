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

        closestInd = -1
        
        #do a binary search on a monotonic increasing time to find the closest time

        if key not in self.timeStampMap:
            return ""
        
        l = 0
        r = len(self.timeStampMap[key]) - 1

        while l <= r:
            mid = (l+r)//2

            
            if self.timeStampMap[key][mid] == timestamp:
                return self.valueMap[key][mid]
            

            if self.timeStampMap[key][mid] < timestamp:
                closestInd = mid
            
            if self.timeStampMap[key][mid] > timestamp:
                r = mid - 1 #search left
            else:
                l = l+1 #search right
        
        if closestInd < 0:
            return ""
        else:
            return self.valueMap[key][closestInd]




        
