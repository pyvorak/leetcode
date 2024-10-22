class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q, v = [root], []

        while q:
            next_q, total = [], 0

            for cur in q:
                if cur.left: next_q.append(cur.left)
                if cur.right: next_q.append(cur.right)
                total += cur.val
            
            v.append(total)
            q = next_q

        if k > len(v):
            return -1
        else:
            v.sort(reverse = True)
            return v[k-1]
