class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bit_mask = {c: 1 << i for i, c in enumerate('aeiou')}
        seen, ans, cnt = {0: -1}, 0, 0

        for i in range(len(s)):
            cnt ^= bit_mask.get(s[i], 0)
            ans = max(ans, i - seen.get(cnt, i))
            seen.setdefault(cnt, i)

        return ans
