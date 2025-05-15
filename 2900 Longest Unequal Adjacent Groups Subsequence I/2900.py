class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        prev = None

        for w, g in zip(words, groups):
            if g != prev:
                ans.append(w)
                prev = g
            
        return ans
