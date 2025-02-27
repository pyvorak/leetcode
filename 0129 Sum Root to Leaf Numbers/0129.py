class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node, cur):
            if not node:
                return  

            cur += str(node.val)

            if not node.left and not node.right:
                self.ans += int(cur)
            
            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, "")

        return self.ans
