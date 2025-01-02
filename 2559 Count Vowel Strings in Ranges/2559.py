class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWELS = set("aeiou")
        dp = [0]
        cnt = 0
        
        for word in words:
            if word[0] in VOWELS and word[-1] in VOWELS:
                cnt += 1
            dp.append(cnt)
        
        return [dp[r+1] - dp[l] for l, r in queries]
