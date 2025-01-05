class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = [0] * (n+1)

        for start, end, direction in shifts:
            change = 1 if direction == 1 else -1
            d[start] += change
            d[end+1] -= change
        
        ans = []
        change = 0

        for i in range(n):
            c = s[i]
            idx = ord(c) - ord('a')
            change += d[i]
            ans.append(chr(ord('a') + (idx + change) % 26))

        return "".join(ans)
