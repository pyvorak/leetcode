class Solution:
    def minLength(self, s: str) -> int:
        ans = []

        for c in s:
            if ans and (ans[-1] == "A" and c == "B" or ans[-1] == "C" and c == "D"):
                ans.pop()
            else:
                ans.append(c)

        return len(ans)
