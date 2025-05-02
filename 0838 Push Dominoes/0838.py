class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = r = -1
        ans = list(dominoes)
        n = len(dominoes)

        for i in range(n):
            d = dominoes[i]
            if d == "R":
                if r > l:
                    for j in range(r + 1, i):
                        ans[j] = "R"
                r = i
            elif d == "L":
                if r > l:
                    x = (i - r - 1) // 2
                    for j in range(r + 1, r + 1 + x):
                        ans[j] = "R"
                    for j in range(i - 1, i - 1 - x, -1):  
                        ans[j] = "L"
                else:
                    for j in range(l + 1, i):
                        ans[j] = "L"
                l = i

        if r > l:
            for i in range(r, n):
                ans[i] = "R"

        return "".join(ans)
