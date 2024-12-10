class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(list)
        i, n = 0, len(s)
        
        while i < n:
            j = i
            c = s[i]
            while j + 1 < n and s[j + 1] == c: 
                j += 1
            d[c].append(j - i + 1)
            i = j + 1 

        ans = -1
        
        for c, cnt in d.items():
            cnt.sort(reverse = True)

            ans = max(ans, cnt[0] - 2)

            if len(cnt) >= 2:
                ans = max(ans, min(cnt[0] - 1, cnt[1]))
            
            if len(cnt) >= 3:
                ans = max(ans, cnt[2])

        return ans if ans > 0 else -1
