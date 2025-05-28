class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def adj(edges):
            a = defaultdict(list)
            for u, v in edges:
                a[u].append(v)
                a[v].append(u)
            return a

        def dfs(node, parent, adj, depth):
            if depth < 0:
                return 0
            cnt = 1
            for next_node in adj[node]:
                if next_node != parent:
                    cnt += dfs(next_node, node, adj, depth-1)
            return cnt

        def target(edges, k):
            a = adj(edges)
            return [dfs(node, -1, a, k) for node in range(len(a))]

        y = max(target(edges2, k-1))
        return [x + y for x in target(edges1, k)]
