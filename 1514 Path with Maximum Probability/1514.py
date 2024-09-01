class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], probs: List[float], start: int, end: int) -> float:
        dp = [0] * n
        dp[start] = 1

        while n:
            valid = False
            for i, (u, v) in enumerate(edges):
                p = probs[i]
                p1, p2 = dp[u] * p, dp[v] * p
                if p1 > dp[v]: dp[v] = p1; valid = True
                if p2 > dp[u]: dp[u] = p2; valid = True
            if not valid: break
            n -= 1

        return dp[end]
