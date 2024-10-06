class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        w1 = s1.split()
        w2 = s2.split()
        n, m = len(w1), len(w2)
        i, j = 0, 0

        while i < n and i < m and w1[i] == w2[i]:
            i += 1

        while j < n-i and j < m-i and w1[n-1-j] == w2[m-1-j]:
            j += 1

        return i + j == min(n, m)
