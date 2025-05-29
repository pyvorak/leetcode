class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def adj(edges):
            a = defaultdict(list)
            for u, v in edges:
                a[u].append(v)
                a[v].append(u)
            return a

        def bfs(edges):
            n = len(edges) + 1
            a = adj(edges)
            odd = even = 0
            d = [None] * n
            seen = [False] * n

            q = [0]
            is_even = True

            while q:
                next_q = []

                if is_even:
                    even += len(q)
                else:
                    odd += len(q)
                    
                for node in q:
                    seen[node] = True
                    d[node] = is_even
                    for next_node in a[node]:
                        if not seen[next_node]:
                            next_q.append(next_node)

                q = next_q
                is_even = not is_even
            
            return d, odd, even 
        
        d1, odd1, even1 = bfs(edges1)
        d2, odd2, even2 = bfs(edges2)
        extra = max(odd2, even2)

        return [(even1 if cur else odd1) + extra for cur in d1]
