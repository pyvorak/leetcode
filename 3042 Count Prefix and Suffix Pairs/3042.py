class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        n = len(words)

        for i in range(n):
            for j in range(i+1, n):
                a, b = words[i], words[j]
                if b.startswith(a) and b.endswith(a):
                    ans += 1
        
        return ans
