import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks= {}
        self.pq = []

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.pq, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.tasks[taskId][0]
        self.tasks[taskId] = (userId, newPriority)
        heapq.heappush(self.pq, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.tasks:
            del self.tasks[taskId] 

    def execTop(self) -> int:
        while self.pq:
            priority_neg, taskId_neg = heapq.heappop(self.pq)
            taskId = -taskId_neg

            if taskId not in self.tasks:
                continue #removed

            if -priority_neg!=self.tasks[taskId][1]:
                continue #edited

            userId = self.tasks[taskId][0]
            del self.tasks[taskId]
            return userId

        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()