class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        groups = []
        group = 0
        parity = None
        
        for num in nums:
            if num % 2 == parity:
                group += 1
            groups.append(group)
            parity = num % 2

        return [groups[start] == groups[end] for start, end in queries]
