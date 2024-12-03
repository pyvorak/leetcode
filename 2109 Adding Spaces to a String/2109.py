class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i, ans = 0, []
        
        for space in spaces:
            ans.append(s[i: space])
            i = space

        return " ".join(ans + [s[i:]])
