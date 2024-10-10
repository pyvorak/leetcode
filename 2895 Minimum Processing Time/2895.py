class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        ans = 0
        
        for i in range(len(processorTime)):
            ans = max(ans, processorTime[i] + tasks[i*4])

        return ans
