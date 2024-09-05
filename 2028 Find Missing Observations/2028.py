class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = (n + len(rolls)) * mean - sum(rolls)
        if total < n or total > 6 * n:
            return []
        else:
            q, r = total // n, total % n
            return [q + 1 if i < r else q for i in range(n)]
