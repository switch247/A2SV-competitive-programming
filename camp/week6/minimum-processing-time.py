class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # to minimise time 
        tasks.sort(reverse=True)
        processorTime.sort()
        # tasks.length == 4 * n
        # largest tasks to min processorTime, 4 at a time
        # print(processorTime, tasks)
        l = p = 0
        ans = 0
        for r in range(3, len(tasks), 4):
            t = tasks[l:r+1]
            # print(t, processorTime[p], processorTime[p] + max(t))
            ans = max(ans , processorTime[p] + max(t))
            p+=1
            l=r+1
        return ans


        