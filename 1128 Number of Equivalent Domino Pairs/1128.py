class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = Counter()
        ans = 0
        for a,b in dominoes:
            x = f"{a}{b}" if a <= b else f"{b}{a}"                
            ans += d[x]
            d[x] += 1
        return ans
