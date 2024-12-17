class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = sorted(Counter(s).items(), reverse=True)
        ans = ""

        while counts:
            c, cnt = counts[0]
            if cnt <= repeatLimit:
                ans += c * cnt
                counts.pop(0)
            else:
                ans += c * repeatLimit
                counts[0] = (c, cnt - repeatLimit)
                if len(counts) >= 2:
                    next_c, next_cnt = counts[1]
                    ans += next_c
                    if next_cnt > 1:
                        counts[1] = (next_c, next_cnt - 1)
                    else:
                        counts.pop(1)
                else:
                    break

        return ans
