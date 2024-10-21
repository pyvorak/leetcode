class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        self.ans = 1

        def dfs(i, seen):
            if i == n:
                self.ans = max(self.ans, len(seen))
            elif len(seen) + n - i > self.ans:
                for j in range(i+1, n+1):
                    cur = s[i:j]
                    if cur not in seen:
                        dfs(j, seen + [cur])
        
        dfs(0, [])
        return self.ans
