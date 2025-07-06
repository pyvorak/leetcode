class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.d1 = Counter(nums1)
        self.d2 = Counter(nums2)
        self.k = sorted(self.d1.keys())
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.d2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.d2[self.nums2[index]] += 1      

    def count(self, tot: int) -> int:
        ans = 0
        for x in self.k:
            if x > tot:
                break
            else:
                y = tot - x
                ans += self.d1[x] * self.d2[y]
        return ans
