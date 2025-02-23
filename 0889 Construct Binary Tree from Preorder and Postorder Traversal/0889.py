class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        node = TreeNode(postorder.pop())

        if postorder:
            preorder.pop(0)
            i = postorder.index(preorder[0]) + 1
            node.left = self.constructFromPrePost(preorder[:i], postorder[:i])
            node.right = self.constructFromPrePost(preorder[i:], postorder[i:])

        return node 
