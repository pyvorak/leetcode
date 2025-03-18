class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = prev = 0
        for cur in rungs:
            diff = cur - prev
            if diff > dist:
                ans += (diff - 1) // dist
            prev = cur
        return ans
