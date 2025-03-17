class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(cnt % 2 == 0 for cnt in Counter(nums).values())
        
