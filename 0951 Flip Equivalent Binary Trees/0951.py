class Solution:
    def flipEquiv(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        elif not a or not b or a.val != b.val:
            return False
        else:
            return (self.flipEquiv(a.left, b.left) and self.flipEquiv(a.right, b.right) 
                or self.flipEquiv(a.left, b.right) and self.flipEquiv(a.right, b.left))
