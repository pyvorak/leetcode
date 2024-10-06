class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        w1 = deque(s1.split())
        w2 = deque(s2.split())
        
        while w1 and w2 and w1[0] == w2[0]:
            w1.popleft()
            w2.popleft()

        while w1 and w2 and w1[-1] == w2[-1]:
            w1.pop()
            w2.pop()

        return not w1 or not w2
