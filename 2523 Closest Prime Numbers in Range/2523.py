class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        valid = [True] * (right+1)
        valid[1] = False

        num = 2
        while num * num <= right:
            if valid[num]:
                for invalid_num in range(num * num, right+1, num):
                    valid[invalid_num] = False
            num += 1
        
        primes = [num for num in range(left, right+1) if valid[num]]
        
        if len(primes) >= 2:
            ans = [primes[0], primes[1]]
            for a, b in zip(primes[1:-1], primes[2:]):
                if b - a < ans[1] - ans[0]:
                    ans = [a, b]
            return ans
        else:
            return [-1, -1]
