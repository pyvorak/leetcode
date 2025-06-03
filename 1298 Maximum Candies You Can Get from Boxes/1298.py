class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque(initialBoxes)
        ans = cnt = 0
        
        while q and cnt < len(q):
            cur = q.popleft()
            if status[cur] == 0:
                q.append(cur)
                cnt += 1
            else:
                cnt = 0
                ans += candies[cur]
                q.extend(containedBoxes[cur])
                for k in keys[cur]:
                    status[k] = 1

        return ans
