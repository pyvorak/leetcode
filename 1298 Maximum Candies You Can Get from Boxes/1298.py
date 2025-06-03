class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque(initialBoxes)
        valid = set([i for i in range(len(status)) if status[i] == 1])
        ans = cnt = 0
    
        while q and cnt < len(q):
            cur = q.popleft()
            if cur in valid:
                cnt = 0
                ans += candies[cur]
                q.extend(containedBoxes[cur])
                valid.update(keys[cur])    
            else:
                q.append(cur)
                cnt += 1

        return ans
