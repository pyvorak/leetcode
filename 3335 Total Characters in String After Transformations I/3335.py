class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        x = [0] * 26

        def idx(c):
            return ord(c) - ord('a')

        for c in s:
            x[idx(c)] += 1

        for _ in range(t):
            y = [0] * 26
            y[idx('a')] = y[idx('b')] = x[idx('z')]
            for i in range(25):
                y[i+1] = (y[i+1] + x[i]) % MOD
            x = y

        return sum(x) % MOD
