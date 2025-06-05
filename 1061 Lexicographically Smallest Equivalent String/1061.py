class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = defaultdict(str)
        
        for c in string.ascii_lowercase:
            d[c] = c

        def get(c):
            if c == d[c]:
                return c
            else:
                d[c] = get(d[c])
                return d[c]

        for a, b in zip(s1, s2):
            x = get(a)
            y = get(b)
            if x > y:
                x, y = y, x
            d[y] = x
        
        return "".join(get(c) for c in baseStr)
