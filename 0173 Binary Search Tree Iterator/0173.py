class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stk = [root]
        self.expandLeft()

    def expandLeft(self):
        while self.stk[-1].left:
            self.stk.append(self.stk[-1].left)

    def next(self) -> int:
        cur = self.stk.pop()
        val = cur.val

        if cur.right:
            self.stk.append(cur.right)
            self.expandLeft()

        return val

    def hasNext(self) -> bool:
        return len(self.stk) > 0
