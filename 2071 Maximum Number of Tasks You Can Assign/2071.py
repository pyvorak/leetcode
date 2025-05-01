class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        n, m = len(tasks), len(workers)
        
        def valid(k):
            p = pills
            ws = workers[m - k:]

            for t in tasks[:k][::-1]:
                if ws[-1] >= t:
                    ws.pop()
                else:
                    if p == 0:
                        return False

                    i = bisect_left(ws, t - strength)

                    if i >= len(ws):
                        return False

                    ws.pop(i)
                    p -= 1
            return True

        l, r, ans = 1, min(m, n), 0
        
        while l <= r:
            m = (l+r)//2

            if valid(m):
                ans = m
                l = m + 1
            else:
                r = m - 1
        
        return ans
