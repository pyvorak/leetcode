class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return root
        
        if root.left:
            cur = root.left
            
            while cur.right:
                cur = cur.right

            cur.right = root.right
            root.right = root.left
            root.left = None

        self.flatten(root.right)
