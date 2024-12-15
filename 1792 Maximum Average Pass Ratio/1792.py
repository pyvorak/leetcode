class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):            
            return (p+1)/(t+1) - p/t
        
        h = [[-gain(p, t), p, t] for p, t in classes]
        heapify(h)

        for _ in range(extraStudents):
            g, p, t = heappop(h)
            p, t = p+1, t+1
            heappush(h, [-gain(p, t), p, t])

        return sum(p/t for g, p, t in h)/len(h)
