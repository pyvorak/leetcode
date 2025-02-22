class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nums = [int(s) for s in re.findall(f'(\d+)', traversal)]
        depths = [len(s) for s in re.findall(f'(-+)', traversal)]

        stk = [TreeNode(nums.pop(0))]

        for depth, num in zip(depths, nums):
            while len(stk) > depth:
                stk.pop()
            
            prev = stk[-1]
            cur = TreeNode(num)

            if prev.left is None:
                prev.left = cur
            else:
                prev.right = cur
            
            stk.append(cur)

        return stk[0]
