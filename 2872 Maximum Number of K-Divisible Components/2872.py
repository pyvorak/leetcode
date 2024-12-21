class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj_list = [[] for _ in range(n)]
        
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        seen = set()

        self.ans = 0

        def dfs(node):
            total = values[node]
            for next_node in adj_list[node]:
                if next_node not in seen:
                    seen.add(next_node)
                    next_value = dfs(next_node)
                    if next_value % k == 0:
                        self.ans += 1
                    else:
                        total += next_value
            return total
        
        dfs(0)
    
        return max(self.ans, 1)
