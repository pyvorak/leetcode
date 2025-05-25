class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = m = 0
        d = Counter(words)
        
        for w, cnt in d.items():
            r = w[::-1]

            if r == w:
                ans += cnt//2*4
                if cnt % 2 == 1:
                    m = 1
            else:
                cnt = min(d[w], d[r])
                ans += cnt*4//2
        
        return ans + m * 2
