class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bins = [0]*24

        for x in candidates:
            i = 0
            while x:
                if x % 2 == 1:
                    bins[i] += 1
                i += 1
                x //= 2
        
        return max(bins)
