class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        d = Counter(digits)
        ans = set()

        def dfs(i, cur):
            if i == 0:
                for x in [0, 2, 4, 6, 8]:
                    if d[x] > 0:
                        d[x] -= 1
                        dfs(i+1, str(x))
                        d[x] += 1
            elif i == 1:
                for x in range(10):
                    if d[x] > 0:
                        d[x] -= 1
                        dfs(i+1, cur + str(x))
                        d[x] += 1
            elif i == 2:
                for x in range(1, 10):
                    if d[x] > 0:
                        d[x] -= 1
                        dfs(i+1, cur + str(x))
                        d[x] += 1
            else:
                ans.add(int(cur[::-1]))

        dfs(0, "")
        return sorted(ans)
