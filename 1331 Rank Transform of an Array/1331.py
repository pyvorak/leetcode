class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {x: i + 1 for i, x in enumerate(sorted(set(arr)))}
        return [d[x] for x in arr]
