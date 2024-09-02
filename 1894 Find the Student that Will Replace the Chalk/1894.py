class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        return next(i for i, x in enumerate(chalk) if (k := k - x) < 0)
