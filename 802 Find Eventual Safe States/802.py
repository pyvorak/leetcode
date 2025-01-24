class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        n = len(graph)
        rev = [set() for _ in range(n)]
        q = deque()

        for a in range(n):
            if len(graph[a]) == 0:
                q.append(a)
            else:
                for b in graph[a]:
                    rev[b].add(a)

        while q:
            cur = q.popleft()
            ans.append(cur)      
            for x in rev[cur]:
                graph[x].remove(cur)
                if len(graph[x]) == 0:
                    q.append(x)
              
        return sorted(ans)
