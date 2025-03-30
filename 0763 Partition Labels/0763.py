class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {c: i for i, c in enumerate(s)}
        ans = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, d[c])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        
        return ans
