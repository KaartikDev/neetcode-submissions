class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        #step one: add index to every task
        for i in range(len(tasks)):
            tasks[i].append(i)
        

        #step 2: sort by enq time
        tasks.sort()


        res = []
        activeTasksHeap = []
        currTime = 0
        taskIndex = 0

        while taskIndex < len(tasks) or activeTasksHeap:
            #move time ahead if cpu idle to next enq time
            if not activeTasksHeap and currTime < tasks[taskIndex][0]:
                currTime = tasks[taskIndex][0]

            #whiel all of the taks enqued before curr time add them to active heap
            while taskIndex < len(tasks) and tasks[taskIndex][0] <= currTime:
                heapq.heappush(activeTasksHeap,tasks[taskIndex][1:]) # add both proc time and index
                taskIndex+=1
            
            #now we do one task form activeTasksHeap
            if activeTasksHeap: #should always be true on every iter
                procTime,index = heapq.heappop(activeTasksHeap)
                currTime+=procTime
                res.append(index)
        return res




       
