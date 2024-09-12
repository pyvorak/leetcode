class Solution:
    def update_valid(self, allowed):
        self.valid = [False] * 26
        for c in allowed:
            self.valid[ord(c) - ord('a')] = True
    
    def is_consistent(self, word):
        for c in word:
            if not self.valid[ord(c) - ord('a')]:
                return False
        return True

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        self.update_valid(allowed)
        ans = 0
        for word in words:
            if self.is_consistent(word):
                ans += 1
        return ans
            
