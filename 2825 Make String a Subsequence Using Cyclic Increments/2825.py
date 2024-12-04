class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        j, n = 0, len(str2)

        for c in str1:
            if 0 <= (ord(str2[j]) - ord(c)) % 26 <= 1:
                j += 1
                if j == n:
                    return True
            
        return False
