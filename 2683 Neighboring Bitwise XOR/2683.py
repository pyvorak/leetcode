class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return not sum(derived) & 1
