class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        max_cnt = max(counts)
        return max((max_cnt-1) * (n+1) + counts.count(max_cnt), len(tasks))
