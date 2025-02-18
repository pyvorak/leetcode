class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stk = []
        ans = ""

        for i in range(len(pattern)+1):
            stk.append(str(i+1))
            if i == len(pattern) or pattern[i] == 'I':
                while stk:
                    ans += stk.pop()

        return ans
