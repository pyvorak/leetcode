class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        else:
            v = [0]*26

            for i in range(len(s1)):
                v[ord(s1[i]) - ord('a')] -= 1
                v[ord(s2[i]) - ord('a')] += 1
            
            if set(v) == {0}:
                return True
            else:
                for i in range(len(s1), len(s2)):
                    v[ord(s2[i]) - ord('a')] += 1
                    v[ord(s2[i-len(s1)]) - ord('a')] -= 1
                    
                    if set(v) == {0}:
                        return True

                return False
