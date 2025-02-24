class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        self.ans = -float('inf')
        self.bob_moves = [None] * n
        self.alice_moves = [None] * n
        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def bob_dfs(cur, moves):
            self.bob_moves[cur] = moves

            if cur == 0: 
                return True

            for next_node in adj[cur]:
                if self.bob_moves[next_node] is None:
                    if bob_dfs(next_node, moves+1):
                        return True
            
            self.bob_moves[cur] = None

            return False

        def alice_dfs(cur, moves, income):
            self.alice_moves[cur] = moves

            if len(adj[cur]) == 1 and self.alice_moves[adj[cur][0]] is not None:
                self.ans = max(self.ans, income)

            moves += 1

            for next_node in adj[cur]:
                if self.alice_moves[next_node] is None:
                    add = amount[next_node]

                    if self.bob_moves[next_node] is not None:
                        if moves == self.bob_moves[next_node]:
                            add //= 2
                        elif moves > self.bob_moves[next_node]:
                            add = 0

                    alice_dfs(next_node, moves, income + add)

            self.alice_moves[cur] = None

        bob_dfs(bob, 0)
        alice_dfs(0, 0, amount[0])
        return self.ans
