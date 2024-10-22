class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        v = []

        def inorder(cur):
            if cur.left: inorder(cur.left)
            v.append(cur.val)
            if cur.right: inorder(cur.right)

        inorder(root)

        ans = v[-1] - v[0]

        for i in range(1, len(v)):
            ans = min(ans, v[i] - v[i-1])

        return ans
