class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        else:
            v1, v2 = [0]*26, [0]*26

            for i in range(len(s1)):
                v1[ord(s1[i]) - ord('a')] += 1
                v2[ord(s2[i]) - ord('a')] += 1
            
            if v1 == v2:
                return True
            else:
                for i in range(len(s1), len(s2)):
                    v2[ord(s2[i]) - ord('a')] += 1
                    v2[ord(s2[i-len(s1)]) - ord('a')] -= 1
                    
                    if v1 == v2:
                        return True

                return False
