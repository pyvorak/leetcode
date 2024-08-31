class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], probs: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]

        for i, (u, v) in enumerate(edges):
            adj[u].append([v, probs[i]])
            adj[v].append([u, probs[i]])

        dp = [0 for _ in range(n)]
        pq = [[-1, start]]

        while pq:
            p, u = heappop(pq)
            if u == end: break
            for v, q in adj[u]:
                if (p2 := p * q) < dp[v]:
                    dp[v] = p2
                    heappush(pq, [p2, v])

        return -dp[end]
