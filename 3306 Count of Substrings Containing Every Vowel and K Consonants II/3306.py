class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = "aeiou"
        n = len(word)

        def cnt(k): 
            ans = l = q = 0
            d = [0] * len(vowels)

            for r, cur in enumerate(word):
                if cur in vowels:
                    d[vowels.index(cur)] += 1
                else:
                    q += 1
                
                while d.count(0) == 0 and q >= k:
                    ans += n - r
                    if word[l] in vowels:
                        d[vowels.index(word[l])] -= 1
                    else:
                        q -= 1
                    l += 1
            return ans

        return cnt(k) - cnt(k+1)


