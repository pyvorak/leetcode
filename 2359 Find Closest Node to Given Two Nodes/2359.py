class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node, d, depth):
            if node != -1 and d[node] is None:
                d[node] = depth
                dfs(edges[node], d, depth + 1)
        
        n = len(edges)

        d1 = [None] * n
        dfs(node1, d1, 0)
        
        d2 = [None] * n
        dfs(node2, d2, 0)

        ans = None
        best = float('inf')
        
        for i, (x, y) in enumerate(zip(d1, d2)):
            if x is not None and y is not None:
                cur = max(x, y)
                if cur < best:
                    best = cur
                    ans = i

        return ans if ans is not None else -1
