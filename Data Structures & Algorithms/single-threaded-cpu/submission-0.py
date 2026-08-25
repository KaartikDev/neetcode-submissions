class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()

        res = []
        heapByProcTime = []
        currTime = 0
        count = 0

        while count < len(tasks) or heapByProcTime:
            if not heapByProcTime and currTime < tasks[count][0]: #jump ahead to when cpu not idle
                currTime = tasks[count][0]

            while count < len(tasks) and tasks[count][0] <= currTime:
                heapq.heappush(heapByProcTime,tasks[count][1:])
                count+=1
            
            procT, i = heapq.heappop(heapByProcTime)
            currTime+=procT
            res.append(i)
        return res

       
