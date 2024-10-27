class Solution:
    def build(self, inorder, postorder, l, r, mp):
        if l > r: return None

        value = postorder[self.postorder_index]
        self.postorder_index -= 1

        node = TreeNode(value)
        i = mp[value]

        node.right = self.build(inorder, postorder, i+1, r, mp)
        node.left = self.build(inorder, postorder, l, i-1, mp)

        return node


    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        self.postorder_index = n-1
        mp = {inorder[i] : i for i in range(n)}
        return self.build(inorder, postorder, 0, n-1, mp)
