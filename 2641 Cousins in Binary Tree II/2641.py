class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([(TreeNode(left=root), 0)])

        while q:
            total = 0
            
            for replace in [False, True]:
                for _ in range(len(q)):
                    parent, curTotal = q.popleft()

                    for child in [parent.left, parent.right]:
                        if child:
                            if replace:
                                child.val = total - curTotal
                                q.append((child, 0))
                            else:
                                curTotal += child.val

                    if not replace:
                        q.append((parent, curTotal))  
                        total += curTotal

        return root
