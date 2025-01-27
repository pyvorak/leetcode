class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for i, j in prerequisites:
            adj[i].append(j)

        flat = [set() for _ in range(n)]

        def dfs(i):
            for j in adj[i]:
                if j not in flat[i]:
                    flat[i].add(j)
                    flat[i].update(dfs(j))
            return flat[i]
        
        for i in range(n):
            dfs(i)
        
        ans = []
        for i, j in queries:
            ans.append(j in flat[i])
        return ans
