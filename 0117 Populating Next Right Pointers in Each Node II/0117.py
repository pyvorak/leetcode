class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = [root] if root else []

        while q:
            next_q = []

            for i, node in enumerate(q):
                if i < len(q) - 1:
                    node.next = q[i+1]
                
                if node.left:
                    next_q.append(node.left)

                if node.right:
                    next_q.append(node.right)
            
            q = next_q

        return root
