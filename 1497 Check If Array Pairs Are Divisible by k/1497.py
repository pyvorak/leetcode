class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = Counter([(x % k + k) % k for x in arr])

        if c[0] % 2 == 1:
            return False

        for i in range(1, k//2 + 1):
            if c[i] != c[k-i]:
                return False

        return True
