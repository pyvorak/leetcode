class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        n = len(s)

        for j in range(n):
            if s[i] == s[n-1-j]:
                i += 1

        if i == n:
            return s

        return s[i:][::-1] + self.shortestPalindrome(s[:i]) + s[i:]
