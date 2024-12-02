class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ans = -1
        words = sentence.split()

        for i in range(len(words)):
            word = words[i]
            if word.startswith(searchWord):
                ans = i + 1
                break

        return ans
