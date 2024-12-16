class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(node, a):
            if not node: return
            dfs(node.left, a)
            a.append(node.val)
            dfs(node.right, a)
        
        def values(node):
            a = []
            dfs(node, a)
            return a
        
        return sorted(values(root1) + values(root2))
