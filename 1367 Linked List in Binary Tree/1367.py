class Solution:
    def isSubPath(self, h: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def valid(p, q):
            return not q or p and p.val == q.val and (valid(p.left, q.next) or valid(p.right, q.next))

        def dfs(p):
            return p and (valid(p, h) or dfs(p.left) or dfs(p.right))

        return dfs(root)
