class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        
        n = len(word)
        i = 0
        
        while i < n:
            cnt = 1
            c = word[i]

            while cnt < 9 and i+1 < n and word[i+1] == c:
                i += 1
                cnt += 1

            ans += str(cnt)
            ans += c
            i += 1

        return ans
