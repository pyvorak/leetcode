class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        d1 = Counter(basket1)
        d2 = Counter(basket2)
        key = set(basket1 + basket2)
        a1 = []
        a2 = []
        
        for k in key:
            cnt = abs(d1[k] - d2[k])

            if cnt % 2 != 0:
                return -1

            if d1[k] != d2[k]:
                cur = [k] * (cnt // 2)
                
                if d1[k] > d2[k]:
                    a1.extend(cur)
                else:
                    a2.extend(cur)
        
        x = min(key)
        a1.sort()
        a2.sort(reverse = True)
        
        return sum(min(a, b, x*2) for a, b in zip(a1, a2))
