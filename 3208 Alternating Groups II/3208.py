class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k])
        start = 0
        ans = 0

        for i, (a, b) in enumerate(zip(colors[:-1], colors[1:])):
            if a == b:
                start = i
            if i - start + 1 >= k:
                ans += 1
        
        return ans

