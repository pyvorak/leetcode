class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans, total = 0, 0
        banned = set(banned)

        for i in range(1, n+1):
            if total > maxSum or total + i > maxSum:
                return ans
            
            if i not in banned:
                ans += 1
                total += i

        return ans
