class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], a: int, b: int, t: int) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        wild = []

        for i, (u, v, w) in enumerate(edges):
            if w > 0:
                adj[u].append([v, w])
                adj[v].append([u, w])
            else:
                wild.append(i)

        def dijkstra():
            INF = float('inf')
            dp = [INF] * n
            pq = [[0, a]]

            while pq:
                d, u = heapq.heappop(pq)
                if u == b: return d
                for v, w in adj[u]:
                    d2 = d + w
                    if d2 < dp[v]:
                        dp[v] = d2
                        heapq.heappush(pq, [d2, v])

            return INF

        d = dijkstra()
        if d < t: return []

        for i in wild: edges[i][2] = t + 1
        if d == t: return edges

        for i in wild:
            u, v, w = edges[i]
            edges[i][2] = 1
            adj[u].append([v, 1])
            adj[v].append([u, 1])
            d = dijkstra()
            if d <= t:
                edges[i][2] += t - d
                return edges

        return []
