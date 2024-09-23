class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = defaultdict(list)
        n = len(s)
        start = n

        for w in dictionary:
            start = min(start, len(w))
            d[w[-1]].append(w)
        
        dp = [i for i in range(start)]
        
        for end in range(start, n + 1):
            best = dp[end-1] + 1

            for w in d[s[end-1]]:
                if len(w) > end:
                    continue
                if s[end-len(w):end] == w:
                    best = min(best, dp[end-len(w)])
            
            dp.append(best)

        return dp[-1]
