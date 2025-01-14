class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        self.cur = 0
        cnt = [0] * (len(A)+1)
        ans = []

        def inc(num):
            cnt[num] += 1
            if cnt[num] == 2:
                self.cur += 1

        for a, b in zip(A,B):
            inc(a)
            inc(b)
            ans.append(self.cur)
            
        return ans
