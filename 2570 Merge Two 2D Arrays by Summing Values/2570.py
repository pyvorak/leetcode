class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = Counter(dict(nums1)) + Counter(dict(nums2))
        return [[i, d[i]] for i in sorted(d.keys())]
