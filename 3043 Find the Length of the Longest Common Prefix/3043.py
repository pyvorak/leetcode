class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def prefix_set(arr):
            seen = set()
            for num in arr:
                s = str(num)
                for i in range(len(s)+1):
                    seen.add(s[:i])
            return seen

        return len(max(prefix_set(arr1) & prefix_set(arr2), key=len))
