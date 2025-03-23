class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        dist = [float("inf")] * n
        dist[0] = 0

        ways = [0] * n
        ways[0] = 1
        
        pq = [(0, 0)]
        adj = [[] for _ in range(n)]

        for u, v, time in roads:
            adj[u].append([v, time])
            adj[v].append([u, time])

        while pq:
            d, u = heappop(pq)

            if d > dist[u]:
                continue
            
            for v, time in adj[u]:
                if dist[u] + time < dist[v]:
                    dist[v] = dist[u] + time
                    ways[v] = ways[u]
                    heappush(pq, (dist[v], v))
                elif dist[u] + time == dist[v]:
                    ways[v] += ways[u]
                    ways[v] %= MOD

        return ways[n-1]
