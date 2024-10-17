class Solution(object):
    def maximumSwap(self, num):
        s = str(num)
        last = {x: i for i, x in enumerate(s)}

        for i, c in enumerate(s):
            for x in range(9, int(c), -1):
                j = last.get(str(x), -1)
                if j > i:
                    ans = list(s)
                    ans[i], ans[j] = ans[j], ans[i]
                    return int("".join(ans))
        
        return num
        
