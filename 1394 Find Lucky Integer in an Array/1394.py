class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1

        d = Counter(arr)

        for x, cnt in d.items():
            if x == cnt:
                ans = max(ans, cnt)

        return ans
