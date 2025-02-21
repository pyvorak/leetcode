class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()

        def dfs(node, x):
            if not node:
                return 

            self.seen.add(x)
            dfs(node.left, 2 * x + 1)
            dfs(node.right, 2 * x + 2)
        
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen
