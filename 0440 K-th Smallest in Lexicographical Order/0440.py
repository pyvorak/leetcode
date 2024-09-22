class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        num = 1
        k -= 1

        def count(a, b):
            cnt = 0

            while a <= n:
                cnt += min(n + 1, b) - a
                a *= 10
                b *= 10
            
            return cnt

        while k > 0:
            cnt = count(num, num + 1)

            if k >= cnt:
                num += 1
                k -= cnt
            else:
                num *= 10
                k -= 1

        return num 
