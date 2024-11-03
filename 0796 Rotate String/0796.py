class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        else:
            def valid(i):
                for j in range(len(goal)):
                    if s[i] != goal[j]:
                        return False
                    i = (i + 1) % len(s)
                return True

            for i in range(len(s)):
                if valid(i):
                    return True
            return False
