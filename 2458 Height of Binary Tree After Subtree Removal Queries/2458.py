class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        removed = [0]*(10**5+1)

        def dfs(cur, h):
            if not cur: return

            nonlocal max_h, left_first

            removed[cur.val] = max(removed[cur.val], max_h)
            max_h = max(max_h, h)

            dfs(cur.left if left_first else cur.right, h+1)
            dfs(cur.right if left_first else cur.left, h+1)

        for b in [True, False]:
            max_h = 0
            left_first = b
            dfs(root, 0)

        ans = []

        for q in queries:
            ans.append(removed[q])

        return ans
