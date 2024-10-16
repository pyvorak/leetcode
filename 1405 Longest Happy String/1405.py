class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ""
        pq = [(-x, chr(ord('a') + i)) for i, x in enumerate([a, b, c]) if x > 0]
        heapify(pq)

        while pq:
            cnt, x  = heappop(pq)

            if len(s) >= 2 and s[-2] == s[-1] and s[-1] == x:
                if not pq: 
                    break
                else:
                    cnt_2, x_2  = heappop(pq)
                    s += x_2
                    cnt_2 += 1
                    if cnt_2 < 0:
                        heappush(pq, (cnt_2, x_2))
                    heappush(pq, (cnt, x))
            else:
                s += x
                cnt += 1
                if cnt < 0:
                    heappush(pq, (cnt, x))

        return s
