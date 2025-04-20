class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum((cnt + k) // (k + 1) * (k + 1) for k, cnt in Counter(answers).items())
